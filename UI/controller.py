import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        anni = DAO.getAllAnni()
        colori = DAO.getAllColors()

        self._view._ddyear.options = list(map(lambda x : ft.dropdown.Option(x),anni))
        self._view._ddcolor.options = list(map(lambda x: ft.dropdown.Option(x), colori))


    def handle_graph(self, e):
        anno = self._view._ddyear.value
        colore = self._view._ddcolor.value



        if  anno == None or anno == None:
            self._view.create_alert("Non hai scelto un valore di colore o di anno!!")
            return
        else :
            self._model.creaGrafo(colore,anno)
            self._view.txtOut.controls.append(ft.Text(f"Nodi: {self._model.grafoDetails()[0]},Archi: {self._model.grafoDetails()[1]}"))
            self.fillDDProduct()
            self._view.update_page()
        top3 = self._model.get_sorted_edges()[:3]
        lista_nodi = {}
        for arco in top3 :
            self._view.txtOut.controls.append(ft.Text(f"{arco[0].Product_number}<->{arco[1].Product_number} peso :{arco[2]["weight"]}"))
            if arco[0].Product_number not in lista_nodi :
                lista_nodi[arco[0].Product_number] = 1
            else:
                lista_nodi[arco[0].Product_number] += 1

            if arco[1].Product_number not in lista_nodi :
                lista_nodi[arco[1].Product_number] = 1
            else:
                lista_nodi[arco[1].Product_number] += 1
            n_repeated = [k for (k,v) in lista_nodi.items() if v > 1]
        self._view.txtOut.controls.append(ft.Text(f"i nodi ripetuti sono : {n_repeated}"))
        self._view.update_page()

    def fillDDProduct(self):
        for n in self._model.get_nodes():
            self._view._ddnode.options.append(ft.dropdown.Option(n.Product_number))
        self._view.update_page()
    def handle_search(self,e):
        self._model.trova_cammino(int(self._view._ddnode.value))
        self._view.txtOut2.controls.append(ft.Text(f"Numero di archi del cammino massimo : {len(self._model.solBest)}"))
        self._view.update_page()





