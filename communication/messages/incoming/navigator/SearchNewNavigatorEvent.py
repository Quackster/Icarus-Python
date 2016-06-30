"""
Search new navigaor event
Author: Alex (TheAmazingAussie)
"""

import game
from communication.messages.outgoing.navigator.SearchResultSetComposer import SearchResultSetComposer


class SearchNewNavigatorMessageEvent:
    def handle(self, session, message):
        """
        Enable navigator when requested
        :param session: the clients who requests NewNavigatorMessageEvent handler
        :param message: the incoming message
        """

        tab = message.read_string()
        search_query = message.read_string()

        navigator_tab = game.navigator_manager.get_tab(tab)

        if navigator_tab is None:
            return

        session.send(SearchResultSetComposer(session, navigator_tab, search_query))
