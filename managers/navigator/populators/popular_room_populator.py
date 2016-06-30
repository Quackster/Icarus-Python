"""
Popular room populator
Author: Alex (TheAmazingAussie)
"""

import game
import operator


class PopularRoomPopulator:
    def generate_listing(self, room_limit, session):

        # Get all rooms
        _rooms = game.room_manager.rooms.values()

        # Only find rooms with at least one user inside
        _rooms = [room for room in _rooms if room.data.users_now > 0]

        # Sort rooms by most popular
        return sorted(_rooms, key=operator.attrgetter('data.users_now'), reverse=True)