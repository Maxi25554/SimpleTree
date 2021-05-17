import pydot
#import networkx as nx
#import matplotlib.pyplot as plt
#import matplotlib
#import graphviz
#function to extrapolate full downwards crafting tree from a single material



def lmat(mtag):
    abc = mtag
    file = open("mat/"+mtag.strip()+".txt")
    content = file.readlines()
    mats = int(content[1])
    graph.add_node(pydot.Node(mtag, shape='circle', fillcolor = 'lightblue', style = 'filled', fontname="helvetica", fontsize = 20))
    if mats > 0:
        for i in range(mats):
            x = (i*2+2)
            y = content[x]
            new_edge = pydot.Edge(mtag, y, color='black', label = content[x+1], dir="back", fontsize = 20)
            graph.add_edge(new_edge)
            lmat(y)

#graph = pydot.Dot('ctree_graph', graph_type='graph', bgcolor='white', suppress_disconnected = False, simplify = True)

def graphing(tags):
    lmat (tags)
    graph.write_raw('ctreedot.dot')
    graph.set_size("80,80!")
    graph.write_png('output.png')

graph = pydot.Dot('ctree_graph', graph_type='graph', bgcolor='white', suppress_disconnected = False, simplify = True)

##Edit the variable below

graphing("RCT")
