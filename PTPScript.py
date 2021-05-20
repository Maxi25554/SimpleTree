import pydot
import random
#import networkx as nx
#import matplotlib.pyplot as plt
#import matplotlib
#import graphviz
#function to extrapolate full downwards crafting tree from a single material
def random_color():
    col = random.choice(['green', 'red', 'blue'])
    return (col)
#    return ('black')
mdict = {}

def lmat(mtag, man):
    file = open("mat/"+mtag.strip()+".txt")
    content = file.readlines()
    mats = int(content[1])
    graph.add_node(pydot.Node(mtag, shape='circle', fillcolor = 'lightblue', style = 'filled', fontname="helvetica"))
    colour = random_color()
    for i in range(mats):
        x = (i*2+2)
        y = content[x]
        new_edge = pydot.Edge(mtag, y, color= colour, label = content[x+1], dir='back', minlen = 2, )
        graph.add_edge(new_edge)
        nam = (float(content[x+1])*man)
        num = round(nam, 6)
        if y in mdict:
            mdict[y] += num
        else:
            mdict[y] = num
        lmat(y, num)


def graphing(tags):
    open('matlist.txt', 'w').close()
    lmat (tags, 1)
    graph.set_size("80,80!")
    graph.write_png('output.png')
    print (mdict)
    for m, b in mdict.items():
        mlist = str(m.strip() + " = " + str(b))
        f = open("matlist.txt", "a")
        f.write(mlist + "\n")
        f.close()



graph = pydot.Dot('ctree_graph', graph_type='graph', bgcolor = 'white', \
suppress_disconnected = False, simplify = True, concentrate = True, splines = 'polyline')

##Edit the variable below

graphing("LIS")
