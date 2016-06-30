"""
Room instance
Author: Alex (TheAmazingAussie)
"""

import game
from database import database_access as dao
from managers.room.room_data import RoomData
from managers.clients.session import Session
from managers.room.room_tasks import RoomTasks

from communication.messages.outgoing.room.RoomModelMessageComposer import *
from communication.messages.outgoing.room.RoomRatingMessageComposer import *
from communication.messages.outgoing.room.RoomSpacesMessageComposer import *
from communication.messages.outgoing.room.RoomRightsLevelMessageComposer import *
from communication.messages.outgoing.room.HasOwnerRightsMessageComposer import *
from communication.messages.outgoing.room.PrepareRoomMessageComposer import *
from communication.messages.outgoing.room.HotelScreenMessageComposer import *
from communication.messages.outgoing.room.RoomDataMessageComposer import *
from communication.messages.outgoing.room.heightmap.FloorMapMessageComposer import *
from communication.messages.outgoing.room.heightmap.HeightMapMessageComposer import *

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

    def init_features(self):
        """
        Load features of the room, eg thread for walking
        :return:
        """

        # Start thread for room tasks
        self.room_tasks.init_tasks()

    def has_rights(self, user_id, only_owner_check):
        return False

    def load_room(self, session):
        """
        Load room information for player
        :param session: the player entering room
        :return:
        """

        room_user = session.room_user

        room_user.room = self
        room_user.is_loading_room = True
        room_user.statuses.clear()

        session.send(RoomModelMessageComposer(self.get_model().name, self.data.id))
        session.send(RoomRatingMessageComposer(self.data.score))

        floor_data = int(self.data.floor)
        wall_data = int(self.data.wall)

        if floor_data > 0:
            session.send(RoomSpacesMessageComposer("floor", self.data.floor))

        if wall_data > 0:
            session.send(RoomSpacesMessageComposer("wall", self.data.floor))

        session.send(RoomSpacesMessageComposer("landscape", self.data.landscape))

        if self.has_rights(session.details.id, True):
            session.send(RoomRightsLevelMessageComposer(4))
            session.send(HasOwnerRightsMessageComposer())

        if self.has_rights(session.details.id, False):
            session.send(RoomRightsLevelMessageComposer(1))
        else:
            session.send(RoomRightsLevelMessageComposer(0))

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

        # Show room panel again, since it gets disabled
        session.send(RoomDataMessageComposer(self, session, True, True))

        # Set position shit
        room_user.position = self.get_model().get_door_point()
        room_user.set_rotation(self.get_model().door_rotation, True, False)

        # Display self
        self.send(UserDisplayMessageComposer([session]))
        self.send(UserStatusMessageComposer([session]))

        # Add user
        self.data.users_now += 1
        self.entities.append(session)

        # Display users for client
        session.send(UserDisplayMessageComposer(self.entities))
        session.send(UserStatusMessageComposer(self.entities))

        # Load features if no one was in room
        if len(self.entities) > 0:
            self.init_features()

    def leave_room(self, session, hotel_view):
        """
        Kick user from room, will lower room population
        :param session: player to leave room
        :param hotel_view: optional to send them to hotel view
        :return:
        """
        if hotel_view:
            session.send(HotelScreenMessageComposer())

        # Remove user from room
        self.send(RemoveUserMessageComposer(session.room_user.virtual_id))

        room_user = session.room_user
        room_user.stop_walking(False)
        room_user.reset()

        if self.entities is not None:
            if session in self.entities:
                self.data.users_now -= 1
                self.entities.remove(session)

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

        print ("current users: " + str(len(self.get_players())))
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

        self.virtual_counter = -1

        return

    def __erase(self):
        """
        This method is called when both dispose types share same data which needs to be removed
        :return:
        """

        self.room_tasks.dispose()
        del self.room_tasks

        self.entities.clear()
        del self.entities

        game.room_manager.rooms.pop(self.data.id, None)

        self.disposed = True




