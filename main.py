import random
import os


class cell:
    def __init__(self):
        self.bomb = False
        self.neighbor = "<#>"
        self.revealed = False


class grid:
    def __init__(self, rows, cols, bC):
        self.R = max(2, rows)
        self.C = max(2, cols)
        self.bombCount = bC
        self.bombs = []
        self.G = []
        index = []
        for i in range(self.R):
            self.G.append([])
            for j in range(self.C):
                self.G[-1].append(cell())
                index.append((i, j))
        self.__setup(index)

    def __setup(self, index):
        for _ in range(self.bombCount):
            i, j = random.choice(index)
            self.G[i][j].bomb = True
            index.remove((i, j))
            self.bombs.append((i, j))

        for i in range(self.R):
            for j in range(self.C):
                if(self.G[i][j].bomb):
                    continue
                else:
                    if (i == 0):
                        t = 0
                    else:
                        t = -1
                    if (i == self.R - 1):
                        b = 0
                    else:
                        b = 1

                    if (j == 0):
                        l = 0
                    else:
                        l = -1
                    if (j == self.C - 1):
                        r = 0
                    else:
                        r = 1

                    tot = 0
                    for x in range(i + t, i + b + 1):
                        for y in range(j + l, j + r + 1):
                            tot += int(self.G[x][y].bomb)
                    self.G[i][j].neighbor = tot

    def display(self):
        un = 0
        os.system("cls")
        print("\n")
        print(end="   |")
        for i in range(self.C):
            if(i < 10):
                print("", i, end=" |")
            else:
                print(i, end=" |")
        print()
        print("   |"*(self.C+1))
        print("---+"*(self.C+1))
        for i in range(self.R):
            if(i < 10):
                print("", i, end=" |")
            else:
                print(i, end=" |")

            for j in range(self.C):
                if (self.G[i][j].revealed):
                    if (self.G[i][j].bomb):
                        print(self.G[i][j].neighbor + "|", end="")
                    else:
                        print("", self.G[i][j].neighbor, "|", end="")
                else:
                    un += 1
                    print("   |", end="")
            print()
            print("---+"*(self.C+1))
        print()
        return un

    def __explore(self, x, y):
        if (x == 0):
            t = 0
        else:
            t = -1
        if (x == self.R - 1):
            b = 0
        else:
            b = 1

        if (y == 0):
            l = 0
        else:
            l = -1
        if (y == self.C - 1):
            r = 0
        else:
            r = 1

        for i in range(x+t, x+b+1):
            for j in range(y+l, y+r+1):
                if(not self.G[i][j].revealed):
                    self.G[i][j].revealed = True
                    if(self.G[i][j].neighbor == 0):
                        self.__explore(i, j)
        return

    def run(self):
        bombed = False
        won = self.bombCount == self.display()

        while (not bombed and not won):
            print("No.of bombs:", self.bombCount)
            q = input("ENTER i,j TO OPEN CELL or X to quit: ").split()

            if(len(q) == 2):
                i = int(q[0])
                j = int(q[1])
            elif (len(q) == 1 and q[0] in ["X", 'x']):
                break
            else:
                print("invalid input!")
                continue

            if(not 0 <= i < self.R)or(not 0 <= j < self.C):
                print("invalid cell!")
                continue

            self.G[i][j].revealed = True

            if(self.G[i][j].bomb):
                bombed = True
                for r, c in self.bombs:
                    self.G[r][c].revealed = True

            if(self.G[i][j].neighbor == 0):
                self.__explore(i, j)
            won = self.bombCount == self.display()

        if(bombed):
            print("BHOOOOOOOMMM!!!\nYou clicked on a bomb!",
                  (i, j), "\nGAME OVER!!")
        elif(won):
            print("Congratulations!!  You won!")
        else:
            print("you lost!")
    ###############################CLASS ENDS#####################################


def main():
    R = input("Rows (>1, default:6) :")
    try:
        R = int(R)
    except:
        R = 6

    C = input("Columns (>1, default:5) :")
    try:
        C = int(C)
    except:
        C = 5
    bc = input("Number of bombs to plant(<"+str(R*C) +
               ", default:"+str(int(0.15*R*C)+1)+") : ")
    try:
        bc = int(C)
    except:
        bc = int(0.15*R*C)+1

    game = grid(R, C, bc)
    game.run()

    cmd = input("Enter 'R'->restart 'Q'->Quit  (default:restart)")
    if (cmd in ['Q', 'q']):
        pass
    else:
        main()


if (__name__ == "__main__"):
    main()
