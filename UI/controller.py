import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        provider = self._view.ddprovider.value
        soglia = self._view.txtDistanza.value
        if provider == None or soglia == None:
            self._view.create_alert("Non hai inserito un provider o una soglia")
            return
        try :
            S = float(soglia)
        except ValueError :
            self._view.create_alert("Hai inserito un valore di soglia non accetabile")

        self._model.creaGrafo(provider,S)
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi : {self._model.grafoDetails()[0]},Numero di archi : {self._model.grafoDetails()[1]}"))
        self._view.update_page()
    def fillDD(self):
        provider = DAO.getProvider()
        self._view.ddprovider.options = list(map(lambda x: ft.dropdown.Option(x), provider))

    def handle_analisi(self,e):
        pass
    def handle_path(self,e):
        pass