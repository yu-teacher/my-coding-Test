from collections import deque, defaultdict


class Game:
    def __init__(self, board):
        self.board = board
        self.pair_map = dict()
        self._init()
        self.pairs = {k for k, v in self.pair_map.items()}
        self.min_cnt = float("INF")

    def _init(self):
        pairs = defaultdict(lambda: list())
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if val != 0:
                    pairs[val].append((i, j))

        for a, b in pairs.values():
            self.pair_map[a] = b
            self.pair_map[b] = a

    def is_valid_coord(self, x, y):
        return 0 <= x < len(self.board) and 0 <= y < len(self.board[0])

    def can_pass(self, x, y, flipped):
        return self.board[x][y] == 0 or (x, y) in flipped

    def ctrl_coord(self, x, y, cx, cy, flipped):
        while self.is_valid_coord(x + cx, y + cy):
            x += cx
            y += cy
            if not self.can_pass(x, y, flipped):
                return (x, y)
        return (x, y)

    def get_min_cost(self, start, goal, flipped):
        if start == goal:
            return 0
        visited = {start}
        check = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque([(start, 0)])

        while q:
            xy, cnt = q.popleft()
            if xy == goal:
                return cnt
            x, y = xy
            for cx, cy in check:
                nx, ny = x + cx, y + cy
                if self.is_valid_coord(nx, ny) and (nx, ny) not in visited:
                    q.append(((nx, ny), cnt + 1))
                    visited.add((nx, ny))
                ccord = self.ctrl_coord(x, y, cx, cy, flipped)
                if ccord not in visited:
                    visited.add(ccord)
                    q.append((ccord, cnt + 1))

    def flip(self, xy, cnt, flipped):
        if self.board[xy[0]][xy[1]] != 0 and xy not in flipped:
            pxy = self.pair_map[xy]
            cost = self.get_min_cost(xy, pxy, flipped)
            self.dfs_not_selected(pxy, cnt + 2 + cost, flipped | {xy, pxy})

    def move_and_flip(self, xy, cnt, flipped):
        for dxy in self.pairs - flipped:
            cost = self.get_min_cost(xy, dxy, flipped)
            self.flip(dxy, cnt + cost, flipped)

    def dfs_not_selected(self, xy, cnt, flipped):
        if len(flipped) == len(self.pairs):
            self.min_cnt = min(self.min_cnt, cnt)
        self.move_and_flip(xy, cnt, flipped)


def solution(board, r, c):
    g = Game(board)
    g.dfs_not_selected((r, c), 0, set())
    return g.min_cnt