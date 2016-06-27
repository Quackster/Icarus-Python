import database.database_access as dao
import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class RequestHeightmapMessageEvent:
    def handle(self, session, message):

        return