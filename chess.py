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
        if self.type == "br" or self.type == "wr":
            for i in range(8):
                if i != self.pos[1]:
                    possible.append((self.pos[0],i))
                if i != self.pos[0]:
                    possible.append((i,self.pos[1]))
        if self.type == "bb" or self.type == "wb":
            for x in range(8):
                if x != self.pos[0]:
                    y = abs(self.pos[0] - x)
                    ya = self.pos[1] - y
                    yb = self.pos[1] + y
                    if ya >= 0:
                        possible.append((x,ya))
                    if yb <= 7:
                        possible.append((x,yb))
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
        if self.type == "bq" or self.type == "wq":
            for i in range(8):
                if i != self.pos[1]:
                    possible.append((self.pos[0],i))
                if i != self.pos[0]:
                    possible.append((i,self.pos[1]))
            for x in range(8):
                if x != self.pos[0]:
                    y = abs(self.pos[0] - x)
                    ya = self.pos[1] - y
                    yb = self.pos[1] + y
                    if ya >= 0:
                        possible.append((x,ya))
                    if yb <= 7:
                        possible.append((x,yb))
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
            pt = self.board[square[1]][square[0]].type
            pp = self.board[square[1]][square[0]].pos
            if pt[1] == "r":
                closestx1 = 100
                closestx2 = 100
                for i in range(8):
                    if not (self.board[pp[1]][i] is None):
                        if i < pp[0]:
                            if (pp[0] - i) < closestx1:
                                closestx1 = pp[0] - i
                                
                        if i > pp[0]:
                            if (i - pp[0]) < closestx2:
                                closestx2 = i - pp[0]
                for i in moves:
                    if i[0] < pp[0]:
                        if (pp[0] - i[0]) > closestx1:
                            moves.remove(i)
                    elif i[0] > pp[0]:
                        if (i[0] - pp[0]) > closestx2:
                            moves.remove(i)
                    else:
                        print("r1")
                        if not (self.board[i[1]][i[0]] is None):
                            print(self.board[i[1]][i[0]].type[0])
                            print(i)
                            if self.board[i[0]][i[1]].type[0] == pt[0]:
                                print("r3")
                                moves.remove(i)


        return moves
    def move(self,square1, square2):
            self.board[square2[1]][square2[0]] = self.board[square1[1]][square1[0]]
            self.board[square1[1]][square1[0]] = None
            self.board[square2[1]][square2[0]].pos = (square2[0],square2[1])
    
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                prev = square
                square = (mouse_pos[0]//100,mouse_pos[1]//100)

    screen.fill("black")    
    grid()
    if square is None:
        pass
    else:
        if board.board[square[1]][square[0]] is None:
            draw(square[0],square[1],(100,100,100))
        else:
            draw(square[0],square[1],(100,200,100))
    for i in board.board:
        for j in i:
            if j is None:
                pass
            else:
                screen.blit(pieces[j.type], (j.pos[0] * 100, j.pos[1] * 100))


    if not(square is None):
        if not(prev is None):
            if square in board.legalMoves(prev):
                board.move(prev,square)
                square = None
                prev = None


    if square is None:
        pass
    else:
        spaces = board.legalMoves(square)
        for i in spaces:
            pygame.draw.circle(screen, (150,150,150),(i[0] * 100 + 50, i[1] * 100 + 50), 25)
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
