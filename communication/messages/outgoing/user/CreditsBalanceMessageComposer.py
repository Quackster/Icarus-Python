import communication.headers.outgoing as outgoing
from communication.data_handlers.response import Response


class CreditsBalanceMessageComposer:
    def __init__(self, currency_balance):
        self.response = Response(outgoing.CreditsBalanceMessageComposer)
        self.response.write_string(str(currency_balance) + ".0")
