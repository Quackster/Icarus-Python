"""
Display my own rooms populator
Author: Alex (TheAmazingAussie)
"""

import game
import operator


class MyRoomPopulator:
    def generate_listing(self, room_limit, session):
        _rooms = game.room_manager.get_player_rooms(session.details.id)
        return sorted(_rooms, key=operator.attrgetter('data.users_now'), reverse=True)