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
            self._view.update_page()
        top3 = self._model.top3Archi()
        lista_nodi = {}
        for arco in top3 :
            self._view.txtOut.controls.append(ft.Text(f"{arco[0]}<->{arco[1]}"))
            if arco[0].Prdouct_number not in lista_nodi :
                lista_nodi[arco[0].Product_number] = 1
            else:
                lista_nodi[arco[0].Product_number] += 1

            if arco[1].Prdouct_number not in lista_nodi :
                lista_nodi[arco[1].Product_number] = 1
            else:
                lista_nodi[arco[1].Product_number] += 1


    def handle_search(self):
        pass





