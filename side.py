class Side:
    # Constructor for side represented by 3x3 matrix
    def __init__(self, c1, c2, c3, c4, c5, c6, c7, c8, c9):
        self.face = [[c1, c2, c3], [c4, c5, c6], [c7, c8, c9]]

    # rotates selected column down
    def col_down(self, top, back, bottom, col):
        t0 = top.face[0][col]
        t1 = top.face[1][col]
        t2 = top.face[2][col]
        top.face[0][col] = back.face[0][col]
        top.face[1][col] = back.face[1][col]
        top.face[2][col] = back.face[2][col]
        back.face[0][col] = bottom.face[0][col]
        back.face[1][col] = bottom.face[1][col]
        back.face[2][col] = bottom.face[2][col]
        bottom.face[0][col] = self.face[0][col]
        bottom.face[1][col] = self.face[1][col]
        bottom.face[2][col] = self.face[2][col]
        self.face[0][col] = t0
        self.face[1][col] = t1
        self.face[2][col] = t2

    # rotates selected column up
    def col_up(self, top, back, bottom, col):
        t0 = bottom.face[0][col]
        t1 = bottom.face[1][col]
        t2 = bottom.face[2][col]
        bottom.face[0][col] = back.face[0][col]
        bottom.face[1][col] = back.face[1][col]
        bottom.face[2][col] = back.face[2][col]
        back.face[0][col] = top.face[0][col]
        back.face[1][col] = top.face[1][col]
        back.face[2][col] = top.face[2][col]
        top.face[0][col] = self.face[0][col]
        top.face[1][col] = self.face[1][col]
        top.face[2][col] = self.face[2][col]
        self.face[0][col] = t0
        self.face[1][col] = t1
        self.face[2][col] = t2

    # rotates selected row right
    def row_right(self, right, back, left, row):
        t0 = left.face[row][0]
        t1 = left.face[row][1]
        t2 = left.face[row][2]
        left.face[row] = back.face[row]
        back.face[row] = right.face[row]
        right.face[row] = self.face[row]
        self.face[row][0] = t0
        self.face[row][1] = t1
        self.face[row][2] = t2

    # rotates selected row left
    def row_left(self, right, back, left, row):
        t0 = right.face[row][0]
        t1 = right.face[row][1]
        t2 = right.face[row][2]
        right.face[row] = back.face[row]
        back.face[row] = left.face[row]
        left.face[row] = self.face[row]
        self.face[row][0] = t0
        self.face[row][1] = t1
        self.face[row][2] = t2
