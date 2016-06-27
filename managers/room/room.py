"""
Room instance
Author: Alex (TheAmazingAussie)
"""

from database import database_access as dao
from managers.room.room_data import RoomData
from communication.messages.outgoing.room.RoomModelMessageComposer import *
from communication.messages.outgoing.room.RoomRatingMessageComposer import *
from communication.messages.outgoing.room.RoomSpacesMessageComposer import *
from communication.messages.outgoing.room.RoomRightsLevelMessageComposer import *
from communication.messages.outgoing.room.HasOwnerRightsMessageComposer import *
from communication.messages.outgoing.room.PrepareRoomMessageComposer import *

class Room:
    def __init__(self):
        self.data = RoomData()
        self.entities = []

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
        room_user.load_room = True
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

    def get_model(self):
        """
        Returns the room model instance for this room instance
        :return: room_model.py python module
        """
        return dao.room_dao.room_models[self.data.model]