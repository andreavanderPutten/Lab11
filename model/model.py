import copy

import networkx as nx

from database.DAO import DAO


class Model :
    def __init__(self):
        self.grafo = nx.Graph()
        self.idMap = {}
        self.solBest = []
    def creaGrafo(self,colore,anno):
        self.grafo.clear()
        nodi = DAO.getVertci()
        nodi_veri = []
        for nodo in nodi :
            if nodo.Product_color == colore :
                nodi_veri.append(nodo)
                self.idMap[nodo.Product_number] = nodo
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

    def get_sorted_edges(self):
        return sorted(self.grafo.edges(data=True), key=lambda x: x[2]['weight'], reverse=True)
    def trova_cammino(self,numero_prodotto):
        nodo_iniziale = self.idMap[numero_prodotto]

        parziale = []

        self.ricorsione(parziale,nodo_iniziale,0)

        print("final",len(self.solBest),[i[2]["weight"] for i in self.solBest])
    def ricorsione(self,parziale,nodo_ultimo,livello):
        archiViciniAmmissibili = self.getArchiViciniAmm(nodo_ultimo,parziale)

        if len(archiViciniAmmissibili) == 0:
            if len(parziale) > len(self.solBest) :
                self.solBest = list(parziale)
                print(len(self.solBest), [ii[2]["weight"] for ii in self.solBest])
        for a in archiViciniAmmissibili :
            parziale.append(a)
            self.ricorsione(parziale,a[1],livello+1)
            parziale.pop()

    def getArchiViciniAmm(self,nodo_ultimo,parziale):
        archiVicini = self.grafo.edges(nodo_ultimo, data=True)
        result = []
        for a  in archiVicini :
            if self.isAscendent(a,parziale) and self.isNovel(a,parziale) :
                result.append(a)
        return result
    def isAscendent(self,e,parziale):
        if len(parziale) == 0 :
            print("parziale id empty in ascendent")
            return True
        return e[2]["weight"] >= parziale[-1][2]["weight"]
    def isNovel(self, e, parziale):
        if len(parziale)==0:
            print("parziale is empty in isnovel")
            return True
        #faccio entrambi i casi
        e_inv = (e[1], e[0], e[2])
        return (e_inv not in parziale) and (e not in parziale)

    def get_nodes(self):
        return self.grafo.nodes()

    def get_edges(self):
        return list(self.grafo.edges(data=True))

    def get_num_of_nodes(self):
        return self.grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self.grafo.number_of_edges()



