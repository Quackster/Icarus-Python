import game


class MyRoomPopulator:
    def generate_listing(self, room_limit, session):
        return game.room_manager.get_player_rooms(session.details.id)