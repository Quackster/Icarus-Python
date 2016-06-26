import game
import communication.headers.incoming as incoming


class SessionConnection:
    def __init__(self, session):
        self.session = session
        self.has_sent_currency = False
        self.has_sent_navigator = False

    def packet_check(self):
        if not self.has_sent_currency:
            game.message_handler.incoming_message(self.session, incoming.GetCurrencyBalanceMessageEvent, None)
            self.has_sent_currency = True

        if not self.has_sent_navigator:
            game.message_handler.incoming_message(self.session, incoming.NewNavigatorMessageEvent, None)
            self.has_sent_navigator = True