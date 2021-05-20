import pydot
import random
import shutil

#Input all variables below

#Which game to fetch the tree for
game = "prun"
#The item code for the item to be fetched
itemcode = "MINSHIP"
#whether the connecting lines should be coloured
coloured = True
#Whether a zip file of the output should be created
zip = True

#End of variables. Don't touch anything below this point unless you know how to code in python.

mdict = {}
mnat = open("mnats.txt")
mnats = mnat.readlines()


def random_color():
    if coloured == True:
        col = random.choice(['green', 'red', 'blue'])
    else:
        col = 'black'
    return (col)


def lmat(mtag, man):
    file = open(game.strip()+"mat/"+mtag.strip()+".txt")
    content = file.readlines()
    mats = int(content[1])
    graph.add_node(pydot.Node(mtag, shape='circle', fillcolor = 'lightblue', style = 'filled', fontname="helvetica"))
    colour = random_color()
    for i in range(mats):
        x = (i*2+2)
        y = content[x]
        co = float(content[x+1])
        new_edge = pydot.Edge(mtag, y, color= colour, label = round(co, 2), dir='back', minlen = 2, decorate = True)
        graph.add_edge(new_edge)
        num = co*man
        if y in mdict:
            mdict[y] += num
        else:
            mdict[y] = num
        lmat(y, num)


def graphing(tags):
    open('output/matlist.txt', 'w').close()
    open('output/matlistnat.txt', 'w').close()
    lmat (tags, 1)
    graph.set_size("80,80!")
    graph.write_png('output/output.png')
    for m, b in mdict.items():
        if m in mnats:
            mlist = str(m.strip() + " = " + str(round(b, 3)))
            f = open("output/matlistnat.txt", "a")
            f.write(mlist + "\n")
            f.close()
        mlist = str(m.strip() + " = " + str(round(b, 3)))
        f = open("output/matlist.txt", "a")
        f.write(mlist + "\n")
        f.close()
    if zip == True:
        shutil.make_archive("zips/"+tags.strip()+"zip", 'zip', "output")


graph = pydot.Dot('ctree_graph', graph_type='graph', bgcolor = 'white', \
suppress_disconnected = False, simplify = True, concentrate = True, splines = 'polyline')


graphing(itemcode)
