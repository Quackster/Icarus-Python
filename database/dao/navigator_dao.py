from managers.navigator.navigator_tab import NavigatorTab

class NavigatorDao:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def get_tabs(self, child_id):
        """
        Returns tabs specified by child_id
        :param child_id: the child id, if -1 will show all tabs with no parents
        """

        db_con = self.database_connection.create_connection()
        db_cur = db_con.cursor()
        db_cur.execute("SELECT id, child_id, tab_name, title, button_type, closed, thumbnail, room_populator FROM navigator_tabs WHERE child_id = %s", (child_id))

        tabs = []

        for row in db_cur:
            tab = NavigatorTab()
            tab.id = row[0]
            tab.child_id = row[1]
            tab.tab_name = row[2]
            tab.title = row[3]
            tab.button_type = row[4]
            tab.closed = (row[5] == 1)
            tab.thumbnail = (row[6] == 1)

            tabs.append(tab) # Add parent tab
            tabs += self.get_tabs(tab.id) # Add child tabs

        db_con.close()
        db_cur.close()

        return tabs
