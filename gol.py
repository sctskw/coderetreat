import unittest

def determine_neighbors(x, y):
    """return the set of coordinates for all adjacent neighbors"""
    return set([
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y),             (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
    ])


def find_alive_neighbors(board, pos):
    """return the # of adjacent neighbors that are living"""
    return set(board).intersection(set(determine_neighbors(*pos)))

def should_die(board, pos):
    """return truthy if the position has <2 or >3 neighbors"""
    alive = len(find_alive_neighbors(board, pos))
    return (alive > 3 or alive < 2)

def should_live(board, pos):
    """return truthy if position has >= 2 and <= 3 neighbors"""
    return not should_die(board, pos)

def pluck_board(board, pluck):
    """return a subset of the board by plucking specified coordinates"""
    return set(board).difference(set(pluck))

def redraw_board(board, pluck=None):
    for pos in board:
        if should_die(board, pos):
            pluck_board(board, [pos])

    return board

def draw_board(rows, cols):
    """returns a set of stuple positions with length rows*cols"""
    board = []
    for x in range(0, rows):
        for y in range(0, cols):
            board.append((x,y))
    return set(board)


class TestGOL(unittest.TestCase):

    def setUp(self):
        pass

    def test_determine_neighbors(self):
        n = determine_neighbors(2,2)
        self.assertEquals(set([
            (1,1), (1,2), (1,3),
            (2,1), (2,3),
            (3,1), (3,2), (3,3)
        ]), n)

    def test_find_alive_neighbors(self):
        board = set([
            (0,0), (0,3),
            (2,1), (2,3),
            (3,1), (4,4)
        ])
        n = find_alive_neighbors(board, (2,2))

    def test_draw_board(self):
        small = set([
            (0,0), (0,1),
            (1,0), (1,1)
        ])

        self.assertEquals(draw_board(2,2), small)

    def test_pluck_board(self):
        board = draw_board(2,2)
        plucked = pluck_board(board, [(0,0), (1,0)])

        self.assertNotEquals(board, plucked)
        self.assertEquals(len(plucked), 2)
        self.assertEquals(plucked, set([(0,1), (1,1)]))

    def test_redraw_board(self):
        original = draw_board(3,3)
        redrawn = redraw_board(original)

        print redrawn
        self.assertNotEquals(original, redrawn)


if __name__ == "__main__":
    unittest.main()
