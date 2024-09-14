import networkx as nx
from geopy import distance
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.nodi = []
        self.idMap = {}
    def creaGrafo(self,provider,soglia):
        self.nodi = DAO.getNodi(provider)
        self.grafo.add_nodes_from(self.nodi)
        for loc1 in self.nodi :
            for loc2 in self.nodi :
                valore = DAO.getPeso(loc2, provider)

                self.idMap[loc2] = valore
                if loc1 != loc2 :
                    distanze = self.calcola_distanza(self.idMap[loc1][0][0],self.idMap[loc1][0][1],self.idMap[loc2][0][0],self.idMap[loc2][0][1])
                    if distanze <= soglia :
                        self.grafo.add_edge(loc1,loc2,weight=distanze)


    def calcola_distanza(self,lat1,lon1,lat2,lon2):
        coordinate1 = (lat1,lon1)
        coordinate2 = (lat2,lon2)
        return distance.distance(coordinate1,coordinate2)

    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)