"""
Check release of SWF version
Author: Alex (TheAmazingAussie)
"""

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

        categories = ["No Category", "School, Daycare & Adoption Rooms", "Help Centre, Guide & Service Rooms", "Hair Salons & Modelling Rooms", "Gaming & Race Rooms", "Trading & Shopping Rooms", "Maze & Theme Park Rooms", "Chat, Chill & Discussion Rooms", "Club & Group Rooms", "Restaurant, Bar & Night Club Rooms", "Themed & RPG Rooms", "Staff Rooms"]

        session.send(FlatCategoriesMessageComposer(categories))
        session.send(NavigatorCategoriesComposer(categories))
        session.send(NavigatorMetaDataComposer())
