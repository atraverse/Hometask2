import random

class Inputer():
    """Take the data from the console and return a list"""
    def inputer():
        i1 = input("Enter row: ")
        i2 = input("Enter col: ")
        lst = [int(i1)-1, int(i2)-1]
        return (lst)
    inputer = staticmethod(inputer)


class Ship:
    """Class that create random ships"""
    def __init__(self):
        self.small_ships = []
        self.mid_ship = []
        self.l_ship = []
        self.xl_ship = []
    def random_ship(self):
        """
        (None)->(list)
        Creates random coordinates of ships
        """
        l4 = 4
        l3 = 3
        l2 = 2
        l1 = 1
        for i in range(l4):
            row = random.randint(0,9)
            col = random.randint(0,9)
            lst = [row, col]
            self.small_ships.append(lst)
        for i in range(l3):
            row = random.randint(0,8)
            col = random.randint(0,8)
            lst = [row, col]
            lst_1 = [row, col+1]
            if lst in self.small_ships or lst in self.mid_ship:
                if lst_1 in self.small_ships or lst_1 in self.mid_ship:
                    l3+=1
            else:
                self.mid_ship.append(lst)
                self.mid_ship.append(lst_1)
        for i in range(l2):
            row = random.randint(0,7)
            col = random.randint(0,7)
            lst = [row, col]
            lst_1 = [row, col+1]
            lst_2 = [row, col+2]
            if lst in self.small_ships or lst in self.mid_ship or lst in self.l_ship:
                if lst_1 in self.small_ships or lst_1 in self.mid_ship or lst_1 in self.l_ship:
                    if lst_2 in self.small_ships or lst_2 in self.mid_ship or lst_2 in self.l_ship:
                        l2+=1
            else:
                self.l_ship.append(lst)
                self.l_ship.append(lst_1)
                self.l_ship.append(lst_2)
        for i in range(l1):
            row = random.randint(0,6)
            col = random.randint(0,6)
            lst = [row, col]
            lst_1 = [row, col+1]
            lst_2 = [row, col+2]
            lst_3 = [row, col+3]
            if lst in self.small_ships or lst in self.mid_ship or lst in self.l_ship or lst in self.xl_ship:
                if lst_1 in self.small_ships or lst_1 in self.mid_ship or lst_1 in self.l_ship or lst in self.xl_ship:
                    if lst_2 in self.small_ships or lst_2 in self.mid_ship or lst_2 in self.l_ship or lst in self.xl_ship:
                        if lst_3 in self.small_ships or lst_3 in self.mid_ship or lst_3 in self.l_ship or lst in self.xl_ship:
                            l1+=1
            else:
                self.xl_ship.append(lst)
                self.xl_ship.append(lst_1)
                self.xl_ship.append(lst_2)
                self.xl_ship.append(lst_3)
        lst_ship = [self.small_ships, self.mid_ship, self.l_ship, self.xl_ship]
        return lst_ship


class Board:
    """Class that create board"""
    def __init__(self):
        self.board = []
        self.f_board = []
    def free_board(self):
        """
        ()->(list)
        Create and return list of '0' of board 10X10
        """
        for i  in range(10):
            self.f_board.append(['0']*10)
        return (self.f_board)
    def set_ship(self):
        """
        ()->(list)
        Set ships on board
        """
        lst_ship = Ship().random_ship()
        small_ships = lst_ship[0]
        mid_ship = lst_ship[1]
        l_ship = lst_ship[2]
        xl_ship = lst_ship[3]
        for i  in range(10):
            self.board.append(['0']*10)
        for i  in range(10):
            self.board.append(['0']*10)
        for i in small_ships:
            self.board[i[0]][i[1]] = '1'
        for i in mid_ship:
            self.board[i[0]][i[1]] = '1'
        for i in l_ship:
            self.board[i[0]][i[1]] = '1'
        for i in xl_ship:
            self.board[i[0]][i[1]] = '1'
        return (self.board)

class Game():
    """Main class for game"""
    def __init__(self):
        self.f_board = Board().free_board()
        self.board = Board().set_ship()
    def game(self):
        """
        None -> None
        Main function that class all Classes and function
        """
        counter = 22
        while counter != 0:
            for line in self.f_board:
                print("".join(line))
            i = Inputer().inputer()

            if self.board[i[0]][i[1]] == '1':
                print("You hit me!")
                counter -=1
                self.f_board[i[0]][i[1]] = "X"
            else:
                print("You missed")
                self.f_board[i[0]][i[1]] = "-"
        else:
            print("You win!")
Game().game()
