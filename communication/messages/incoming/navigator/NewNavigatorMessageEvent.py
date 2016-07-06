"""
Load new navigator event
Author: Alex (TheAmazingAussie)
"""
import game
from communication.messages.outgoing.navigator.FlatCategoriesMessageComposer import FlatCategoriesMessageComposer
from communication.messages.outgoing.navigator.NavigatorCategoriesComposer import NavigatorCategoriesComposer
from communication.messages.outgoing.navigator.NavigatorMetaDataComposer import NavigatorMetaDataComposer


class NewNavigatorMessageEvent:
    def handle(self, session, message):
        """
        Enable navigator when requested
        :param session: the clients who requests NewNavigatorMessageEvent handler
        :param message: the incoming message
        """

        session.send(FlatCategoriesMessageComposer(game.navigator_manager.categories, session.details.rank))
        session.send(NavigatorCategoriesComposer(game.navigator_manager.categories))
        session.send(NavigatorMetaDataComposer())
