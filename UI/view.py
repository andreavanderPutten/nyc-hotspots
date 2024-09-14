import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_analisi_grafo = None
        self.txt_result = None
        self.txt_container = None
        self.ddprovider = None
        self.txtDistanza = None
        self.txtStringa = None
        self.ddTarget = None
        self.btn_grafo = None
        self.btn_calcola_percorso = None
        self.txt_result2= None
        self.txt_result3 = None


    def load_interface(self):
        # title
        self._title = ft.Text("Hello World", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_name = ft.TextField(
            label="name",
            width=200,
            hint_text="Insert a your name"
        )

        # button for the "hello" reply
        self.ddprovider = ft.Dropdown(label="Provider")
        self.btn_grafo = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handle_graph)
        row1 = ft.Row([self.ddprovider, self.btn_grafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result)



        self.txtDistanza = ft.TextField(label="Distanza")
        self.btn_analisi_grafo = ft.ElevatedButton(text="Analisi grafo",on_click=self._controller.handle_analisi)

        row2 = ft.Row([self.txtDistanza, self.btn_analisi_grafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self.txt_result2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result2)

        self.txtStringa = ft.TextField(label="Stringa")
        self.btn_calcola_percorso = ft.ElevatedButton(text="Calcola percorso",on_click=self._controller.handle_path)
        self.ddTarget = ft.Dropdown(label="Target")
        row3 = ft.Row([self.txtStringa, self.btn_calcola_percorso,self.ddTarget],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        self.txt_result3 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result3)

        # List View where the reply is printed

        self._controller.fillDD()
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
