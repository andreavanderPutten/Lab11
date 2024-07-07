import copy

import networkx as nx

from database.DAO import DAO


class Model :
    def __init__(self):
        self.grafo = nx.Graph()
    def creaGrafo(self,colore,anno):
        self.grafo.clear()
        nodi = DAO.getVertci()
        nodi_veri = []
        for nodo in nodi :
            if nodo.Product_color == colore :
                nodi_veri.append(nodo)
        self.grafo.add_nodes_from(nodi_veri)

        for nodo1 in nodi_veri :
            for nodo2 in nodi_veri :
                if nodo1.Product_number == nodo2.Product_number :
                    continue
                else :
                    peso = DAO.getSameDaySales(nodo1,nodo2,anno)
                    if int(peso[0]) > 0 :
                        self.grafo.add_edge(nodo1, nodo2, weight=peso)
                        print(f"{nodo1}-{nodo2} : {peso}")

    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)
    def top3Archi(self):
        archi_ordinati = copy.deepcopy(self.grafo.edges)
        sorted(archi_ordinati,key= lambda nodo : nodo[2])
        top3 = archi_ordinati[:3]
        return top3




