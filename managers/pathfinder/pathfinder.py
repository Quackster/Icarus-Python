"""
Pathfinder
Ported from Java by Alex (Quackster/TheAmazingAussie)
"""
from managers.pathfinder.point import Point
from managers.pathfinder.pathfinder_node import PathfinderNode


"""
All 8 compass points around a tile
"""
MOVE_POINTS = [
    Point(0, -1, 0),
    Point(0, 1, 0),
    Point(1, 0, 0),
    Point(-1, 0, 0),
    Point(1, -1, 0),
    Point(-1, 1, 0),
    Point(1, 1, 0),
    Point(-1, -1, 0)
]


def make_path(position, end, room):
    """
    Create programming path
    :param position:
    :param end:
    :param room:
    :return:
    """
    squares = []
    nodes = make_path_reversed(position, end, room)

    if nodes is not None:
        while nodes.next_node is not None:
            squares.append(Point(nodes.position.x, nodes.position.y, 0))
            nodes = nodes.next_node

    return squares[::-1] # Reverse list


def make_path_reversed(position, end, room):

    open_list = []
    map = room.get_model().get_2d_array(None)
    node = None
    tmp = None
    cost = 0
    diff = 0

    current = PathfinderNode(position)
    current.cost = 0

    finish = PathfinderNode(end)
    map[position.x][position.y] = current
    open_list.append(current)

    while len(open_list) > 0:
        current = poll_first(open_list)
        current.in_close = True

        for temp_point in MOVE_POINTS:
            tmp = current.position.add_point(temp_point)

            is_final_move = (tmp.x == end.x) and (tmp.y == end.y)

            if room.room_mapping.is_valid_step(Point(current.position.x, current.position.y, current.position.z), tmp, is_final_move):

                if map[tmp.x][tmp.y] is None:
                    node = PathfinderNode(tmp)
                    map[tmp.x][tmp.y] = node
                else:
                    node = map[tmp.x][tmp.y]

                if node.in_close is not True:
                    diff = 0

                    if current.position.x != node.position.x:
                        diff += 1

                    if current.position.y != node.position.y:
                        diff += 1

                    cost = current.cost + diff + node.position.get_distance_squared(end)

                    if cost < node.cost:
                        node.cost = cost
                        node.next_node = current

                    if node.in_open is not True:
                        if node.position.x == finish.position.x and node.position.y == finish.position.y:
                            node.next_node = current
                            return node

                        node.in_open = True
                        open_list.append(node)

    return None


def poll_first(list):

    first_item = None

    if len(list) > 0:
        first_item = list[0]
        list.pop(0)

    return first_item
