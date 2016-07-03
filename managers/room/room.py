"""
Room instance
Author: Alex (TheAmazingAussie)
"""

import game
from database import database_access as dao
from managers.room.room_data import RoomData
from managers.room.room_tasks import RoomTasks
from managers.room.room_mapping import RoomMapping
from managers.clients.session import Session

from communication.messages.outgoing.room.RoomModelMessageComposer import *
from communication.messages.outgoing.room.RoomRatingMessageComposer import *
from communication.messages.outgoing.room.RoomSpacesMessageComposer import *
from communication.messages.outgoing.room.RightsLevelMessageComposer import *
from communication.messages.outgoing.room.NoRightsMessageComposer import *
from communication.messages.outgoing.room.YouAreOwnerComposer import *
from communication.messages.outgoing.room.PrepareRoomMessageComposer import *
from communication.messages.outgoing.room.HotelViewMessageComposer import *
from communication.messages.outgoing.room.RoomDataMessageComposer import *
from communication.messages.outgoing.room.heightmap.FloorMapMessageComposer import *
from communication.messages.outgoing.room.heightmap.HeightMapMessageComposer import *

from communication.messages.outgoing.room.user.RoomOwnerRightsComposer import *
from communication.messages.outgoing.room.user.UserStatusMessageComposer import *
from communication.messages.outgoing.room.user.UserDisplayMessageComposer import *
from communication.messages.outgoing.room.user.RemoveUserMessageComposer import *


class Room:
    def __init__(self):
        self.data = RoomData()
        self.disposed = False
        self.virtual_counter = -1
        self.entities = []
        self.room_tasks = RoomTasks(self)
        self.room_mapping = RoomMapping(self)

    def init_features(self):
        """
        Load features of the room, eg thread for walking
        :return:
        """

        # Start thread for room tasks
        self.room_tasks.init_tasks()

        # Fill map with points which aren't availiable
        self.room_mapping.regenerate_collision_map()


    def has_rights(self, user_id, only_owner_check):

        return self.data.owner_id == user_id


    def load_room(self, session):
        """
        Load room information for player
        :param session: the player entering room
        :return:
        """

        room_user = session.room_user

        # Leave previous room if the user was already in a different room
        if room_user.room is not None:
            room_user.room.leave_room(session, False)

        room_user.room = self

        room_user.is_loading_room = True
        room_user.statuses.clear()

        # Initalise room loading
        session.send(RoomModelMessageComposer(self.get_model().name, self.data.id))
        session.send(RoomRatingMessageComposer(self.data.score))

        floor_data = int(self.data.floor)
        wall_data = int(self.data.wall)

        # Floor design
        if floor_data > 0:
            session.send(RoomSpacesMessageComposer("floor", self.data.floor))

        # Wall design
        if wall_data > 0:
            session.send(RoomSpacesMessageComposer("wall", self.data.floor))

        # Landscape design
        session.send(RoomSpacesMessageComposer("landscape", self.data.landscape))

        # Send rights
        if  self.has_rights(session.details.id, True):

            session.room_user.statuses["flatctrl"] = "useradmin"
            session.send(YouAreOwnerComposer())
            session.send(RightsLevelMessageComposer(4))

        elif self.has_rights(session.details.id, False):

            session.room_user.statuses["flatctrl"] = "1"
            session.send(RightsLevelMessageComposer(1))
        else:
            session.send(NoRightsMessageComposer())

        session.send(PrepareRoomMessageComposer(self.data.id))

    def load_heightmap(self, session):
        """
        Load all heightmap data, walls and furniture items
        :param session: the player to send the data to
        :return: None
        """

        session.send(HeightMapMessageComposer(self, self.get_model().map_size_x, self.get_model().map_size_y))
        session.send(FloorMapMessageComposer(self))

        room_user = session.room_user
        room_user.virtual_id = self.get_virtual_id()

        # Finished loading room
        room_user.is_loading_room = False

        # Set position shit
        room_user.position = self.get_model().get_door_point()
        room_user.set_rotation(self.get_model().door_rotation, True, False)

        # Display self
        self.send(UserDisplayMessageComposer([session]))
        self.send(UserStatusMessageComposer([session]))

        # Add user
        self.data.users_now += 1
        self.entities.append(session)

        # Load features if no one was in room
        if len(self.get_players()) == 1:
            self.init_features()

        # Display users for client
        session.send(UserDisplayMessageComposer(self.entities))
        session.send(UserStatusMessageComposer(self.entities))

        # Normal has rights for general users
        is_owner = self.has_rights(session.details.id, True)
        session.send(RoomOwnerRightsComposer(self.data.id, is_owner))

    def leave_room(self, session, hotel_view):
        """
        Kick user from room, will lower room population
        :param session: player to leave room
        :param hotel_view: optional to send them to hotel view
        :return:
        """
        if hotel_view:
            session.send(HotelViewMessageComposer())

        if self.entities is not None:
            if session in self.entities:
                self.data.users_now -= 1
                self.entities.remove(session)

        # Remove user from room
        if len(self.get_players()) > 0:
            self.send(RemoveUserMessageComposer(session.room_user.virtual_id))

        room_user = session.room_user
        room_user.stop_walking(False)
        room_user.reset()

        self.dispose(False)

    def get_virtual_id(self):
        """
        Virtual room user identification
        :return: None
        """
        self.virtual_counter += 1
        return self.virtual_counter

    def send(self, message):
        """
        Sends room message to all players in room
        :param message: the message, will be passed through message encoder
        :return: None
        """
        for entity in self.get_players():
            entity.send(message)

    def get_model(self):
        """
        Returns the room model instance for this room instance
        :return: room_model.py python module
        """
        return dao.room_dao.room_models[self.data.model]

    def get_players(self):
        """
        Get all players currently in room
        :return: array of connected sessions
        """

        return [player for player in self.entities if type(player) == Session]

    def dispose(self, force_disposal):
        """
        Dispose all data
        :param force_disposal:
        :return:
        """
        if self.disposed:
            return


        # Force disposal of all data, kick users when user deletes room
        if force_disposal:

            self.data.dispose()
            del self.data

            # Call method to erase data that share common dispose calls
            self.__reset_state()
            self.__erase()

        if len(self.get_players()) == 0:

            # If there's no users, then them we reset the state of the room for items to be loaded again
            #    amongst other things
            self.__reset_state()

            # Delete from room collection if owner goes offline and there's no more users in the room
            if game.session_manager.find_by_id(self.data.owner_id) is None and self.data.type == "private":

                # Call method to erase data that share common dispose calls
                self.__erase()

    def __reset_state(self):
        """
        Reset all states, reset virtual id, clear furniture, AI, pets, etc
        :return:
        """

        print ("[UNLOAD] Room with id (" + str(self.data.id) + ") is unloaded")

        self.virtual_counter = -1
        self.room_mapping.dispose()

        return

    def __erase(self):
        """
        This method is called when both dispose types share same data which needs to be removed
        :return:
        """

        self.room_tasks.dispose()
        self.entities.clear()

        del self.room_tasks
        del self.entities
        del self.room_mapping

        game.room_manager.rooms.pop(self.data.id, None)

        self.disposed = True




