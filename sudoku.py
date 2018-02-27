import sys

class point:
    def __init__(self, xp, yp):
        self.x = xp
        self.y = yp
        self.available = []
        self.value = 0


def rowNum(p, sudoku):
    row = []
    rowlist = sudoku[p.y * 9: p.y * 9 + 9]
    row = set(rowlist)
    row.remove(0)
    return row  # set type


def colNum(p, sudoku):
    col = []
    length = len(sudoku)
    for i in range(p.x, length, 9):
        col.append(sudoku[i])
    col = set(col)
    col.remove(0)
    return col  # set type


def blockNum(p, sudoku):
    block_x = p.x // 3
    block_y = p.y // 3
    block = []
    start = block_y * 27 + block_x * 3
    for i in range(start, start + 3):
        block.append(sudoku[i])
    for i in range(start + 9, start + 12):
        block.append(sudoku[i])
    for i in range(start + 18 , start + 21):
        block.append(sudoku[i])
    block = set(block)
    block.remove(0)
    return block  # set type


def initPoint(sudoku):
    pointList = []
    length = len(sudoku)
    for i in range(length):
        if sudoku[i] == 0:
            p = point(i % 9, i // 9)
            for j in range(1, 10):
                if j not in rowNum(p, sudoku) and j not in colNum(p, sudoku) and j not in blockNum(p, sudoku):
                    p.available.append(j)
            pointList.append(p)
    return pointList


def tryInsert(p, sudoku):
    availNum = p.available
    for v in availNum:
        p.value = v
        if check(p, sudoku):
            sudoku[p.y * 9 + p.x] = p.value
            if len(pointList) <= 0:
                showSudoku(sudoku)
                fout.write(soduout(sudoku,'BTS'))
                exit()
            p2 = pointList.pop()
            tryInsert(p2, sudoku)
            sudoku[p2.y * 9 + p2.x] = 0
            sudoku[p.y * 9 + p.x] = 0
            p2.value = 0
            pointList.append(p2)
        else:
            pass

def AC3 (pointlist1,sudoku):
    tmp = None
    flag = 0
    pointlist = list(pointlist1)
    if len(pointlist)==0:
        showSudoku(sudoku)
        return sudoku,pointlist
    for pt in pointlist:
        if len(pt.available)==1:
            flag = 1
            pt.value = pt.available[0]
            sudoku[pt.y * 9 + pt.x] = pt.available[0]
            tmp = pt
            for pt1 in pointlist:
                if pt1.x == pt.x or pt1.y == pt.y or (pt.x//3 == pt1.x//3 and pt.y//3 == pt1.y//3):
                    if not (pt1.x == pt.x and pt1.y == pt.x) and sudoku[9*pt1.y+pt1.x]==0:
                        if pt.value in pt1.available:
                            print pt1.available
                            print pt.value
                            pt1.available.remove(pt.value)

    if flag == 1:
        pointlist.remove(tmp)
        print sudoku
        print len(pointlist)
        #return!!!!!!!!
        return  AC3 (pointlist,sudoku)
    else :
        return sudoku,pointlist



def solved (sudoku):
    print sudoku
    for j in range(0,9):
        for i in range(0,9):
            if sudoku[9*j+i] == 0:
                return False
    return True

def soduout(sudoku,method):
    sodu_out_list = []
    for j in range(0, 9):
        for i in range(0, 9):
            sodu_out_list.append(str(sudoku[j * 9 + i]))
    res=''.join(sodu_out_list) + " " + method
    print res
    return res

def check(p, sudoku):
    if p.value == 0:
        print('not assigned value to point p!!')
        return False
    if p.value not in rowNum(p, sudoku) and p.value not in colNum(p, sudoku) and p.value not in blockNum(p, sudoku):
        return True
    else:
        return False


def showSudoku(sudoku):
    for j in range(0,9):
        for i in range(0,9):
            print sudoku[j * 9 + i],
        print(' ')

if __name__ == '__main__':
    fout=open('output.txt','wt')
    lists = []
    finalsudo =[]
    lists = list(sys.argv[1])
    sudoku=[int(i) for i in lists]
    pointList = initPoint(sudoku)
    sudoku,pointList = AC3(pointList,sudoku)
    print 'ac3'
    showSudoku(sudoku)
    if solved(sudoku)==True:
        fout.write(soduout(sudoku,"AC3"))
        exit()
    p = pointList.pop()
    tryInsert(p, sudoku)
    showSudoku(sudoku)
