import pygame


def pieceMap():
    pieces = {}
    pieces["bp"] = pygame.image.load('bp.png')
    pieces["wp"] = pygame.image.load('wp.png')
    pieces["br"] = pygame.image.load('br.png')
    pieces["wr"] = pygame.image.load('wr.png')
    pieces["bb"] = pygame.image.load('bb.png')
    pieces["wb"] = pygame.image.load('wb.png')
    pieces["bn"] = pygame.image.load('bn.png')
    pieces["wn"] = pygame.image.load('wn.png')
    pieces["bk"] = pygame.image.load('bk.png')
    pieces["wk"] = pygame.image.load('wk.png')
    pieces["bq"] = pygame.image.load('bq.png')
    pieces["wq"] = pygame.image.load('wq.png')
    return pieces

def draw(x,y,colour):
    pygame.draw.rect(screen,colour,(x*100,y*100,100,100))

def grid():
    alt = True
    for i in range(0,8):
        if alt:
            alt = False
        else:
            alt = True
        for j in range(0,8):
            if alt:
                alt = False
                draw(i,j,(118, 150, 86))
            else:
                alt = True
                draw(i,j,(238, 238, 210))


class piece:
    def __init__(self,pieceType,pos):
        self.type = pieceType 
        self.pos = pos # Tuple (x,y)
    def possibleMoves(self):
        possible = []
        if self.type == "bp":
            possible.append((self.pos[0],self.pos[1] + 1))
            if self.pos[0] - 1 >= 0:
                possible.append((self.pos[0] -1,self.pos[1]+1))
            if self.pos[0] + 1 <= 7:
                possible.append((self.pos[0] + 1, self.pos[1] + 1))
            if self.pos[1] == 1:
                possible.append((self.pos[0],self.pos[1] + 2))
        if self.type == "wp":
            possible.append((self.pos[0],self.pos[1] - 1))
            if self.pos[0] - 1 >= 0:
                possible.append((self.pos[0] -1,self.pos[1]-1))
            if self.pos[0] + 1 <= 7:
                possible.append((self.pos[0] + 1, self.pos[1] - 1))
            if self.pos[1] == 6:
                possible.append((self.pos[0],self.pos[1] - 2))
        if self.type == "bn" or self.type == "wn":
            x = self.pos[0]
            y = self.pos[1]
            if x - 2 >= 0 and y - 1 >=0:
                possible.append((x-2,y-1))
            if x - 1 >= 0 and y - 2 >=0:
                possible.append((x-1,y-2))
            if x + 2 <= 7 and y - 1 >=0:
                possible.append((x+2,y-1))
            if x + 1 <= 7 and y - 2 >=0:
                possible.append((x+1,y-2))
            if x - 2 >= 0 and y + 1 <= 7:
                possible.append((x-2,y+1))
            if x - 1 >= 0 and y + 2 <=7:
                possible.append((x-1,y+2))
            if x + 2 <= 7 and y + 1 <=7:
                possible.append((x+2,y+1))
            if x + 1 <= 7 and y + 2 <=7:
                possible.append((x+1,y+2))
        if self.type == "bk" or self.type == "wk":
            x = self.pos[0]
            y = self.pos[1]
            if x - 1 >= 0:
                possible.append((x-1,y))
                if y - 1 >= 0:
                    possible.append((x-1,y-1))
                    possible.append((x,y-1))
                if y + 1 <= 7:
                    possible.append((x-1,y+1))
                    possible.append((x,y+1))
            
            if x + 1 <= 7:
                possible.append((x+1,y))
                if y - 1 >= 0:
                    possible.append((x+1,y-1))
                if y + 1 <= 7:
                    possible.append((x+1,y+1))


        return possible


class board1:
    def __init__(self):
        self.board = []
        self.turn1 = "w"
        self.inCheck = False
        for i in range(8):
            l = []
            for i in range(8):
                l.append(None)
            self.board.append(l)
    def setup(self):
        # Pawns
        for i in range(8):
            self.board[6][i] = piece("wp",(i,6))
            self.board[1][i] = piece("bp",(i,1))
        #Rooks
        self.board[0][0] = piece("br",(0,0))
        self.board[0][7] = piece("br",(7,0))
        self.board[7][0] = piece("wr",(0,7))
        self.board[7][7] = piece("wr",(7,7))
        #Knights
        self.board[0][1] = piece("bn",(1,0))
        self.board[0][6] = piece("bn",(6,0))
        self.board[7][1] = piece("wn",(1,7))
        self.board[7][6] = piece("wn",(6,7))
        #Bishops
        self.board[0][2] = piece("bb",(2,0))
        self.board[0][5] = piece("bb",(5,0))
        self.board[7][2] = piece("wb",(2,7))
        self.board[7][5] = piece("wb",(5,7))
        #Kings/Queen
        self.board[0][3] = piece("bq",(3,0))
        self.board[0][4] = piece("bk",(4,0))
        self.board[7][3] = piece("wq",(3,7))
        self.board[7][4] = piece("wk",(4,7))
    def legalMoves(self,square):
        moves = []
        if self.board[square[1]][square[0]] is None:
            pass
        else:
            moves = self.board[square[1]][square[0]].possibleMoves()
            moves2 = moves[:]
            pt = self.board[square[1]][square[0]].type
            pp = self.board[square[1]][square[0]].pos
            stop = False
            if pt[1] == "p":
                for i in moves2:
                    if i[0] == pp[0]:
                        if i[1] == pp[1] + 1 or i[1] == pp[1] - 1:
                            if not(self.board[i[1]][i[0]] is None):
                                stop = True
                                moves.remove(i)
                        else:
                            if not(self.board[i[1]][i[0]] is None) or stop:
                                moves.remove(i)
                    else:
                        if not(self.board[i[1]][i[0]] is None):
                            if self.board[i[1]][i[0]].type[0] == pt[0]:
                                moves.remove(i)
                        else:
                            moves.remove(i) 
            if pt[1] == "n" or pt[1] == "k":
                for i in moves2:
                    if not(self.board[i[1]][i[0]] is None):
                        if self.board[i[1]][i[0]].type[0] == pt[0]:
                            moves.remove(i)
            if pt[1] == "b" or pt[1] == "q":
                directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
                for dx, dy in directions:
                    x = pp[0] + dx
                    y = pp[1] + dy
                    while 0 <= x < 8 and 0 <= y < 8:
                        target = self.board[y][x]

                        if target is None:
                            moves.append((x, y))
                        else:
                            if target.type[0] != pt[0]:
                                moves.append((x, y))
                            break
                        x += dx
                        y += dy
            if pt[1] == "r" or pt[1] == "q":
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in directions:
                    x = pp[0] + dx
                    y = pp[1] + dy
                    while 0 <= x < 8 and 0 <= y < 8:
                        target = self.board[y][x]

                        if target is None:
                            moves.append((x, y))
                        else:
                            if target.type[0] != pt[0]:
                                moves.append((x, y))
                            break
                        x += dx
                        y += dy
        return moves
    
    def move(self, square1, square2):
        x1, y1 = square1
        x2, y2 = square2

        selected = self.board[y1][x1]
        if selected is None:
            return False
        if selected.type[0] != self.turn1:
            return False
        if square2 not in self.legalMoves(square1):
            return False
        
        captured = self.board[y2][x2]
        self.board[y2][x2] = selected
        self.board[y1][x1] = None
        selected.pos = (x2, y2)

        c = self.check()
        if c:
            self.board[y1][x1] = selected
            selected.pos = (x1,y1)
            self.board[y2][x2] = captured
            return False

        if self.turn1 == "b":
            self.turn1 = "w"
        else:
            self.turn1 = "b"

        c = self.check()
        if c:
            if self.turn1 == "b":
                print("Blck is in Check")
            else:
                print("White is in Check")
        self.inCheck = c

        return True
    
    def check(self):
        kingPos = None
        for i in self.board:
            for j in i:
                if not(j is None):
                    if j.type[1] == "k" and j.type[0] == self.turn1:
                        kingPos = j.pos
                        break
            if kingPos is not None:
                break

        enemy = "b"
        if self.turn1 == "b":
            enemy = "w"

        for i in self.board:
            for j in i:
                if j is not None:
                    if j.type[0] == enemy:
                        if kingPos in self.legalMoves(j.pos):
                            return True
        return False
        


    
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
board = board1()
board.setup()
pieces = pieceMap()
square = None
prev = None
while running:
    wrongPiece = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            clicked = (mouse_pos[0] // 100, mouse_pos[1] // 100)

            if square is None:
                selected_piece = board.board[clicked[1]][clicked[0]]

                if selected_piece is not None:
                    if selected_piece.type[0] == board.turn1:
                        square = clicked
            else:
                if board.move(square, clicked):
                    square = None
                else:
                    selected_piece = board.board[clicked[1]][clicked[0]]

                    if selected_piece is not None:
                        if selected_piece.type[0] == board.turn1:
                            square = clicked

    screen.fill("black")    
    grid()
    if square is None:
        pass
    else:
        if board.board[square[1]][square[0]] is None:
            draw(square[0],square[1],(100,100,100))
        else:
            if board.board[square[1]][square[0]].type[0] == board.turn1:
                draw(square[0],square[1],(100,200,100))
            else:
                draw(square[0],square[1],(100,100,100))
                
    for i in board.board:
        for j in i:
            if j is None:
                pass
            else:
                screen.blit(pieces[j.type], (j.pos[0] * 100, j.pos[1] * 100))

    if square is None:
        pass
    else:
        if wrongPiece == False:
            spaces = board.legalMoves(square)
            for i in spaces:
                pygame.draw.circle(screen, (150,150,150),(i[0] * 100 + 50, i[1] * 100 + 50), 25)
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()