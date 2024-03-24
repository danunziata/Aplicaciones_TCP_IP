import reflex as rx


class State(rx.State): #clase que manejan variables que tienen eventos
    count: int = 0
    #crean dos funciones para incrementar y decrementar
    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index(): #es la pagina en si, es la grafica estatica.
    return rx.hstack(
        rx.button(
            "Decrement",
            color_scheme="blue",
            on_click=State.decrement,
        ),
        rx.heading(State.count, font_size="2em"),
        rx.button(
            "Increment",
            color_scheme="yellow",
            on_click=State.increment,
        ),
        spacing="4",
    )



app = rx.App()
app.add_page(index)
