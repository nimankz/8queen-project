# this is nima nikrouz's midterm project
#=============================================library=====================================================
from tabulate import tabulate
#=============================================library=====================================================
#=============================================roots=====================================================
realBord=(("a1","b1","c1","d1","e1","f1","g1","h1"),
      ("a2","b2","c2","d2","e2","f2","g2","h2"),
      ("a3","b3","c3","d3","e3","f3","g3","h3"),
      ("a4","b4","c4","d4","e4","f4","g4","h4"),
      ("a5","b5","c5","d5","e5","f5","g5","h5"),
      ("a6","b6","c6","d6","e6","f6","g6","h6"),
      ("a7","b7","c7","d7","e7","f7","g7","h7"),
      ("a8","b8","c8","d8","e8","f8","g8","h8"))

primeryBord=[["a1","b1","c1","d1","e1","f1","g1","h1"],
      ["a2","b2","c2","d2","e2","f2","g2","h2"],
      ["a3","b3","c3","d3","e3","f3","g3","h3"],
      ["a4","b4","c4","d4","e4","f4","g4","h4"],
      ["a5","b5","c5","d5","e5","f5","g5","h5"],
      ["a6","b6","c6","d6","e6","f6","g6","h6"],
      ["a7","b7","c7","d7","e7","f7","g7","h7"],
      ["a8","b8","c8","d8","e8","f8","g8","h8"]]
queen="Q"
full="F"
#=============================================roots=====================================================
#=============================================defs=====================================================
def column(n):
#this def is for having a list of the column we want.
    column=[]
    for item in range(8):
        column.append(primeryBord[item][n])
    return column

def orib1(mylist):
#this def is for orib list from top left to bottom right.
    i=int(mylist[0])
    j=int(mylist[1])
    orib1=[]
    while 0<=j<len(realBord) and 0<=i<len(realBord):
        orib1.append(realBord[i][j])
        i+=1
        j+=1
    i=mylist[0]-1
    j=mylist[1]-1
    while 0<=j<len(realBord) and 0<=i<len(realBord):
        orib1.append(realBord[i][j])
        i+=-1
        j+=-1

    return orib1

def orib2(mylist):
# this def is for orib list from top right to bottom left.
    i=mylist[0]
    j=mylist[1]
    orib=[]
    while 0<=j < len(realBord) and i < len(realBord):
        orib.append(realBord[i][j])
        i += 1
        j -= 1
    i = mylist[0] - 1
    j = mylist[1] +1
    while 0 <= j < len(realBord) and 0 <= i < len(realBord):
        orib.append(realBord[i][j])
        i -= 1
        j += 1
    return orib

def index(k):
#this def is for finding the index of an elemnt.
    for item in range(len(realBord)):
        for j in range(len(realBord)):
            if realBord[item][j]==k:
                return [item,j]

def check(n):
#this def is for checking if there is any queen in those areas.
    i=index(n)[0]
    j=index(n)[1]
    sets=list(set(realBord[i]).union(set(column(j))).union(set(orib1(index(n)))).union(set(orib2(index(n)))))
    for item in range(len(sets)):
        if sets[item]=="Q":
            return False
def emptyplace(mylist):
#this def finds empty places for placing queens.
    emptyPlace1 = []
    for j in range(len(mylist)):
        if mylist[j] == "Q" or mylist[j] == "F":
            pass
        else:
            if check(mylist[j]) != False:
                emptyPlace1.append(mylist[j])
    return emptyPlace1
def queenfinder():
#this def is a primary memory for remembering where the queen was.
    queenlist=[]
    for item in range(8):
        for j in range(8):
            if primeryBord[item][j]=="Q":
                queenlist.append([item,j])
    return queenlist

def queenPlacer(x):
#this def is for placing queen and which areas are not empty for other queens.
    i=index(x)[0]
    j=index(x)[1]
    y=orib1(index(x))
    z=orib2(index(x))
    oribs=list(set(y)^set(z))
    for item in range(8):
            primeryBord[i][item]=full
    for item in range(8):
            primeryBord[item][j]=full
    for item in range(len(oribs)):
            if oribs[item]=="F" or oribs[item]=="Q":
                pass
            else:
                inorb=index(oribs[item])
                primeryBord[int(inorb[0])][int(inorb[1])]=full
    primeryBord[i][j]=queen
    return primeryBord

def maindef():
#this def is the main def for finding different situations.
    num=1
#these loops are for placing queens.
    for item1 in range(8):
        queenPlacer(column(0)[item1])
        for item2 in range(len(emptyplace(column(1)))):
            queenPlacer(emptyplace(column(1))[item2])
            for item3 in range(len(emptyplace(column(2)))):
                queenPlacer(emptyplace(column(2))[item3])
                for item4 in range(len(emptyplace(column(3)))):
                    queenPlacer(emptyplace(column(3))[item4])
                    for item5 in range(len(emptyplace(column(4)))):
                        queenPlacer(emptyplace(column(4))[item5])
                        for item6 in range(len(emptyplace(column(5)))):
                            queenPlacer(emptyplace(column(5))[item6])
                            for item7 in range(len(emptyplace(column(6)))):
                                queenPlacer(emptyplace(column(6))[item7])
                                for item8 in range(len(emptyplace(column(7)))):
                                    queenPlacer(emptyplace(column(7))[item8])
                                    print("NO.",num,":")
                                    print(tabulate(primeryBord,headers=["a","b","c","d","e","f","g","h"],
                                                   showindex=["1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 "]))
                                    print("-----------------------------------------------","\n")
                                    num+=1
                                    #these loops are for change primary bord to previous level.
                                    for item9 in range(len(column(7))):
                                            primeryBord[item9][7]=realBord[item9][7]
                                    for j1 in range(len(queenfinder())):
                                        ix=int(queenfinder()[j1][0])
                                        jx=int(queenfinder()[j1][1])
                                        x=realBord[ix][jx]
                                        queenPlacer(x)
                                for item10 in range(len(column(6))):
                                        primeryBord[item10][6] = realBord[item10][6]
                                        primeryBord[item10][7]=realBord[item10][7]
                                for j1 in range(len(queenfinder())):
                                    ix = int(queenfinder()[j1][0])
                                    jx = int(queenfinder()[j1][1])
                                    x = realBord[ix][jx]
                                    queenPlacer(x)
                            for item11 in range(len(column(5))):
                                    primeryBord[item11][5]=realBord[item11][5]
                                    primeryBord[item11][6]=realBord[item11][6]
                                    primeryBord[item11][7]=realBord[item11][7]
                            for j1 in range(len(queenfinder())):
                                ix = int(queenfinder()[j1][0])
                                jx = int(queenfinder()[j1][1])
                                x = realBord[ix][jx]
                                queenPlacer(x)
                        for item12 in range(len(column(4))):
                                primeryBord[item12][4]=realBord[item12][4]
                                primeryBord[item12][5]=realBord[item12][5]
                                primeryBord[item12][6]=realBord[item12][6]
                                primeryBord[item12][7]=realBord[item12][7]
                        for j1 in range(len(queenfinder())):
                            ix = int(queenfinder()[j1][0])
                            jx = int(queenfinder()[j1][1])
                            x = realBord[ix][jx]
                            queenPlacer(x)
                    for item13 in range(len(column(3))):
                            primeryBord[item13][3]=realBord[item13][3]
                            primeryBord[item13][4]=realBord[item13][4]
                            primeryBord[item13][5]=realBord[item13][5]
                            primeryBord[item13][6]=realBord[item13][6]
                            primeryBord[item13][7]=realBord[item13][7]
                    for j1 in range(len(queenfinder())):
                        ix = int(queenfinder()[j1][0])
                        jx = int(queenfinder()[j1][1])
                        x = realBord[ix][jx]
                        queenPlacer(x)
                for item14 in range(len(column(2))):
                        primeryBord[item14][2]=realBord[item14][2]
                        primeryBord[item14][3]=realBord[item14][3]
                        primeryBord[item14][4]=realBord[item14][4]
                        primeryBord[item14][5]=realBord[item14][5]
                        primeryBord[item14][6]=realBord[item14][6]
                        primeryBord[item14][7]=realBord[item14][7]
                for j1 in range(len(queenfinder())):
                    ix = int(queenfinder()[j1][0])
                    jx = int(queenfinder()[j1][1])
                    x = realBord[ix][jx]
                    queenPlacer(x)
            for item15 in range(len(column(1))):
                    primeryBord[item15][1]=realBord[item15][1]
                    primeryBord[item15][2]=realBord[item15][2]
                    primeryBord[item15][3]=realBord[item15][3]
                    primeryBord[item15][4]=realBord[item15][4]
                    primeryBord[item15][5]=realBord[item15][5]
                    primeryBord[item15][6]=realBord[item15][6]
                    primeryBord[item15][7]=realBord[item15][7]
            for j1 in range(len(queenfinder())):
                ix = int(queenfinder()[j1][0])
                jx = int(queenfinder()[j1][1])
                x = realBord[ix][jx]
                queenPlacer(x)
        for item16 in range(len(column(0))):
                primeryBord[item16][0]=realBord[item16][0]
                primeryBord[item16][1]=realBord[item16][1]
                primeryBord[item16][2]=realBord[item16][2]
                primeryBord[item16][3]=realBord[item16][3]
                primeryBord[item16][4]=realBord[item16][4]
                primeryBord[item16][5]=realBord[item16][5]
                primeryBord[item16][6]=realBord[item16][6]
                primeryBord[item16][7]=realBord[item16][7]
#=============================================defs=====================================================
#=============================================action=====================================================
maindef()
#=============================================action=====================================================
# this is nima nikrouz's midterm project
