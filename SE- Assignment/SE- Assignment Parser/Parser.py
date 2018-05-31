import networkx as nx

class Analyzer():
    def __init__(self,fileName):
        self.fileName=fileName
        self.file = open(self.fileName, 'r')
        self.graph=nx.Graph()
    def buildGraph(self):
        for line in self.file.readlines():
            if(line.find("if")>0 or line.find("while")>0):
                print("Hello there");

analyzer=Analyzer("..\Xml_parser.py")
analyzer.buildGraph();




