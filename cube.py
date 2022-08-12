from side import Side


class Cube:
    # constructor with solved cube as default parameters and raises exception for invalid setup
    def __init__(self, white_center=Side("w", "w", "w", "w", "w", "w", "w", "w", "w"),
                 green_center=Side("g", "g", "g", "g", "g", "g", "g", "g", "g"),
                 yellow_center=Side("y", "y", "y", "y", "y", "y", "y", "y", "y"),
                 blue_center=Side("b", "b", "b", "b", "b", "b", "b", "b", "b"),
                 orange_center=Side("o", "o", "o", "o", "o", "o", "o", "o", "o"),
                 red_center=Side("r", "r", "r", "r", "r", "r", "r", "r", "r")):
        if white_center.face[1][1] != "w" or green_center.face[1][1] != "g"\
                or yellow_center.face[1][1] != "y" or blue_center.face[1][1] != "b"\
                or orange_center.face[1][1] != "o" or red_center.face[1][1] != "r":
            raise ValueError("Invalid side assignments")
        else:
            self.white_center = white_center
            self.green_center = green_center
            self.yellow_center = yellow_center
            self.blue_center = blue_center
            self.orange_center = orange_center
            self.red_center = red_center

    # U
    def u_upper(self):
        self.green_center.row_left(self.red_center, self.blue_center, self.orange_center, 0)

    # U'
    def unot_upper(self):
        self.green_center.row_right(self.red_center, self.blue_center, self.orange_center, 0)

    # L
    def l_upper(self):
        self.green_center.col_down(self.white_center, self.blue_center, self.yellow_center, 0)

    # L'
    def lnot_upper(self):
        self.green_center.col_up(self.white_center, self.blue_center, self.yellow_center, 0)

    # F
    def f_upper(self):
        self.red_center.col_down(self.white_center, self.orange_center, self.yellow_center, 0)

    # F'
    def fnot_upper(self):
        self.red_center.col_up(self.white_center, self.orange_center, self.yellow_center, 0)

    # R
    def r_upper(self):
        self.green_center.col_up(self.white_center, self.blue_center, self.yellow_center, 2)

    # R'
    def rnot_upper(self):
        self.green_center.col_down(self.white_center, self.blue_center, self.yellow_center, 2)

    # B
    def b_upper(self):
        self.red_center.col_up(self.white_center, self.orange_center, self.yellow_center, 2)

    # B'
    def bnot_upper(self):
        self.red_center.col_down(self.white_center, self.orange_center, self.yellow_center, 2)

    # D
    def d_upper(self):
        self.green_center.row_right(self.red_center, self.blue_center, self.orange_center, 2)

    # D'
    def dnot_upper(self):
        self.green_center.row_left(self.red_center, self.blue_center, self.orange_center, 2)

    # M
    def m_upper(self):
        self.green_center.col_down(self.white_center, self.blue_center, self.yellow_center, 1)

    # M'
    def mnot_upper(self):
        self.green_center.col_up(self.white_center, self.blue_center, self.yellow_center, 1)

    # E
    def e_upper(self):
        self.green_center.row_right(self.red_center, self.blue_center, self.orange_center, 1)

    # E'
    def enot_upper(self):
        self.green_center.row_left(self.red_center, self.blue_center, self.orange_center, 1)

    # S
    def s_upper(self):
        self.red_center.col_down(self.white_center, self.orange_center, self.yellow_center, 1)

    # S'
    def snot_upper(self):
        self.red_center.col_up(self.white_center, self.orange_center, self.yellow_center, 1)

    # u
    def u_lower(self):
        self.green_center.row_left(self.red_center, self.blue_center, self.orange_center, 0)
        self.green_center.row_left(self.red_center, self.blue_center, self.orange_center, 1)

    # u'
    def unot_lower(self):
        self.green_center.row_right(self.red_center, self.blue_center, self.orange_center, 0)
        self.green_center.row_right(self.red_center, self.blue_center, self.orange_center, 1)

    # l
    def l_lower(self):
        self.green_center.col_down(self.white_center, self.blue_center, self.yellow_center, 0)
        self.green_center.col_down(self.white_center, self.blue_center, self.yellow_center, 1)

    # l'
    def lnot_lower(self):
        self.green_center.col_up(self.white_center, self.blue_center, self.yellow_center, 0)
        self.green_center.col_up(self.white_center, self.blue_center, self.yellow_center, 1)

    # f
    def f_lower(self):
        self.red_center.col_down(self.white_center, self.orange_center, self.yellow_center, 0)
        self.red_center.col_down(self.white_center, self.orange_center, self.yellow_center, 1)

    # f'
    def fnot_lower(self):
        self.red_center.col_up(self.white_center, self.orange_center, self.yellow_center, 0)
        self.red_center.col_up(self.white_center, self.orange_center, self.yellow_center, 1)

    # r
    def r_lower(self):
        self.green_center.col_up(self.white_center, self.blue_center, self.yellow_center, 2)
        self.green_center.col_up(self.white_center, self.blue_center, self.yellow_center, 1)

    # r'
    def rnot_lower(self):
        self.green_center.col_down(self.white_center, self.blue_center, self.yellow_center, 2)
        self.green_center.col_down(self.white_center, self.blue_center, self.yellow_center, 1)

    # b
    def b_lower(self):
        self.red_center.col_up(self.white_center, self.orange_center, self.yellow_center, 2)
        self.red_center.col_up(self.white_center, self.orange_center, self.yellow_center, 1)

    # b'
    def bnot_lower(self):
        self.red_center.col_down(self.white_center, self.orange_center, self.yellow_center, 2)
        self.red_center.col_down(self.white_center, self.orange_center, self.yellow_center, 1)

    # d
    def d_lower(self):
        self.green_center.row_right(self.red_center, self.blue_center, self.orange_center, 2)
        self.green_center.row_right(self.red_center, self.blue_center, self.orange_center, 1)

    # d'
    def dnot_lower(self):
        self.green_center.row_left(self.red_center, self.blue_center, self.orange_center, 2)
        self.green_center.row_left(self.red_center, self.blue_center, self.orange_center, 1)

    # X
    def x_upper(self):
        self.green_center.col_up(self.white_center, self.blue_center, self.yellow_center, 0)
        self.green_center.col_up(self.white_center, self.blue_center, self.yellow_center, 1)
        self.green_center.col_up(self.white_center, self.blue_center, self.yellow_center, 2)

    # X'
    def xnot_upper(self):
        self.green_center.col_down(self.white_center, self.blue_center, self.yellow_center, 0)
        self.green_center.col_down(self.white_center, self.blue_center, self.yellow_center, 1)
        self.green_center.col_down(self.white_center, self.blue_center, self.yellow_center, 2)

    # Y
    def y_upper(self):
        self.green_center.row_left(self.red_center, self.blue_center, self.orange_center, 0)
        self.green_center.row_left(self.red_center, self.blue_center, self.orange_center, 1)
        self.green_center.row_left(self.red_center, self.blue_center, self.orange_center, 2)

    # Y'
    def ynot_upper(self):
        self.green_center.row_right(self.red_center, self.blue_center, self.orange_center, 0)
        self.green_center.row_right(self.red_center, self.blue_center, self.orange_center, 1)
        self.green_center.row_right(self.red_center, self.blue_center, self.orange_center, 2)

    # Z
    def z_upper(self):
        self.red_center.col_down(self.white_center, self.orange_center, self.yellow_center, 0)
        self.red_center.col_down(self.white_center, self.orange_center, self.yellow_center, 1)
        self.red_center.col_down(self.white_center, self.orange_center, self.yellow_center, 2)

    # Z'
    def z_down(self):
        self.red_center.col_up(self.white_center, self.orange_center, self.yellow_center, 0)
        self.red_center.col_up(self.white_center, self.orange_center, self.yellow_center, 1)
        self.red_center.col_up(self.white_center, self.orange_center, self.yellow_center, 2)

    # String method
    def __str__(self):
        return f'      {self.white_center.face[0][0]} {self.white_center.face[0][1]} {self.white_center.face[0][2]}\n' \
               f'      {self.white_center.face[1][0]} {self.white_center.face[1][1]} {self.white_center.face[1][2]}\n' \
               f'      {self.white_center.face[2][0]} {self.white_center.face[2][1]} {self.white_center.face[2][2]}\n' \
               f'{self.orange_center.face[0][0]} {self.orange_center.face[0][1]} {self.orange_center.face[0][2]} ' \
               f'{self.green_center.face[0][0]} {self.green_center.face[0][1]} {self.green_center.face[0][2]} ' \
               f'{self.red_center.face[0][0]} {self.red_center.face[0][1]} {self.red_center.face[0][2]} ' \
               f'{self.yellow_center.face[0][0]} {self.yellow_center.face[0][1]} {self.yellow_center.face[0][2]}\n' \
               f'{self.orange_center.face[1][0]} {self.orange_center.face[1][1]} {self.orange_center.face[1][2]} ' \
               f'{self.green_center.face[1][0]} {self.green_center.face[1][1]} {self.green_center.face[1][2]} ' \
               f'{self.red_center.face[1][0]} {self.red_center.face[1][1]} {self.red_center.face[1][2]} ' \
               f'{self.yellow_center.face[1][0]} {self.yellow_center.face[1][1]} {self.yellow_center.face[1][2]}\n' \
               f'{self.orange_center.face[2][0]} {self.orange_center.face[2][1]} {self.orange_center.face[2][2]} ' \
               f'{self.green_center.face[2][0]} {self.green_center.face[2][1]} {self.green_center.face[2][2]} ' \
               f'{self.red_center.face[2][0]} {self.red_center.face[2][1]} {self.red_center.face[2][2]} ' \
               f'{self.yellow_center.face[2][0]} {self.yellow_center.face[2][1]} {self.yellow_center.face[2][2]}\n' \
               f'      {self.blue_center.face[0][0]} {self.blue_center.face[0][1]} {self.blue_center.face[0][2]}\n' \
               f'      {self.blue_center.face[1][0]} {self.blue_center.face[1][1]} {self.blue_center.face[1][2]}\n' \
               f'      {self.blue_center.face[2][0]} {self.blue_center.face[2][1]} {self.blue_center.face[2][2]}'
