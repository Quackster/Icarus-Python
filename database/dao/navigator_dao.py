class NavigatorDao:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def get_tabs(self, parent_id):
        """
        Returns tabs specified by parent_id
        :param parent_id: the parent id, if -1 will show all tabs with no parents
        """

        tabs = []

        return tabs
