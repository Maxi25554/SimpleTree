import pydot
import random

def random_color():
    col = random.choice(['green', 'red', 'blue'])
    return (col)
#    return ('black')
mdict = {}

mnat = open("mnats.txt")
mnats = mnat.readlines()

def lmat(mtag, man):
    file = open("mat/"+mtag.strip()+".txt")
    content = file.readlines()
    mats = int(content[1])
    graph.add_node(pydot.Node(mtag, shape='circle', fillcolor = 'lightblue', style = 'filled', fontname="helvetica"))
    colour = random_color()
    for i in range(mats):
        x = (i*2+2)
        y = content[x]
        co = float(content[x+1])
#        lam = round(float(content[x+1]), 2)
        new_edge = pydot.Edge(mtag, y, color= colour, label = round(co, 2), dir='back', minlen = 2, decorate = True)
        graph.add_edge(new_edge)
        num = co*man
        if y in mdict:
            mdict[y] += num
        else:
            mdict[y] = num
        lmat(y, num)


def graphing(tags):
    open('matlist.txt', 'w').close()
    open('matlistnat.txt', 'w').close()
    lmat (tags, 1)
    graph.set_size("80,80!")
    graph.write_png('output.png')
    for m, b in mdict.items():
        if m in mnats:
            mlist = str(m.strip() + " = " + str(round(b, 3)))
            f = open("matlistnat.txt", "a")
            f.write(mlist + "\n")
            f.close()
        mlist = str(m.strip() + " = " + str(round(b, 3)))
        f = open("matlist.txt", "a")
        f.write(mlist + "\n")
        f.close()


graph = pydot.Dot('ctree_graph', graph_type='graph', bgcolor = 'white', \
suppress_disconnected = False, simplify = True, concentrate = True, splines = 'polyline')

##Edit the variable below

graphing("KOM")
