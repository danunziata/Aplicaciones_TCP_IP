"""A Reflex example of a analog clock in Radix."""

import asyncio
from datetime import datetime, timezone
from typing import Any

import reflex as rx
from reflex.components.radix.themes import theme

import pytz


# The supported time zones.
TIMEZONES = [
    "Asia/Tokyo",
    "Australia/Sydney",
    "Europe/London",
    "Europe/Paris",
    "Europe/Moscow",
    "US/Pacific",
    "US/Eastern",
]
DEFAULT_ZONE = TIMEZONES[-2]


def rotate(degrees: int) -> str:
    """CSS to rotate a clock hand.

    Args:
        degrees: The degrees to rotate the clock hand.

    Returns:
        The CSS to rotate the clock hand.
    """
    return f"rotate({degrees}deg)"
#La función rotate(degrees: int) -> str devuelve una cadena de texto que representa una transformación CSS
#para rotar una manecilla de reloj. Toma un argumento degrees, que es el número de grados para rotar la
#manecilla de reloj, y devuelve una cadena de texto que representa esta rotación en CSS.
#Por ejemplo, si pasas degrees = 90 a esta función, la cadena de salida sería "rotate(90deg)", que se puede
#usar como valor de la propiedad CSS transform para rotar una manecilla de reloj en 90 grados.

class State(rx.State):
    """The app state."""

    # Es una cadena que representa la zona horaria en la que se mostrará el reloj. Inicialmente se establece en DEFAULT_ZONE pero se puede actualizar mediante la interacción del usuario.
    zone: str = rx.Cookie(DEFAULT_ZONE)

    #  Es un booleano que indica si el reloj está en funcionamiento o no. Inicialmente se establece en False..
    running: bool = False

    # Es una variable que almacena la última marca de tiempo actualizada del reloj.
    _now: datetime = datetime.fromtimestamp(0)

    @rx.cached_var
    def valid_zone(self) -> str:
        """Get the current time zone.

        Returns:
            The current time zone.
        """
        try:
            pytz.timezone(self.zone)
        except Exception:
            return DEFAULT_ZONE
        return self.zone
    #Este método devuelve la zona horaria válida actual. Intenta obtener la zona horaria especificada por zone y, si hay un error, devuelve DEFAULT_ZONE.
    @rx.cached_var
    def time_info(self) -> dict[str, Any]:
        """Get the current time info.

        This can also be done as several computed vars, but this is more concise.

        Returns:
            A dictionary of the current time info.
        """
        now = self._now.astimezone(pytz.timezone(self.valid_zone))
        return {
            "hour": now.hour if now.hour <= 12 else now.hour % 12,
            "minute": now.minute,
            "second": now.second,
            "meridiem": "AM" if now.hour < 12 else "PM",
            "minute_display": f"{now.minute:02}",
            "second_display": f"{now.second:02}",
            "hour_rotation": rotate(now.hour * 30 - 90),
            "minute_rotation": rotate(now.minute * 0.0167 * 360 - 90),
            "second_rotation": rotate(now.second * 0.0167 * 360 - 90),
        }
    #Este método devuelve un diccionario con información sobre la hora actual. Obtiene la hora actual ajustada a la zona horaria válida y calcula los datos de la hora, minuto y segundo actual, así como la meridiana (AM/PM) y las rotaciones de las manecillas del reloj.
    def on_load(self):
        """Switch the clock off when the page refreshes."""
        self.running = False
        self.refresh()
    #Este método se llama cuando la página se carga. En este caso, apaga el reloj estableciendo running en False y actualiza la marca de tiempo del reloj.
    def refresh(self):
        """Refresh the clock."""
        self._now = datetime.now(timezone.utc)
    #Este método actualiza la marca de tiempo _now del reloj con la hora actual en UTC.
    @rx.background
    async def tick(self):
        """Update the clock every second."""
        while self.running:
            async with self:
                self.refresh()

            # Sleep for a second.
            await asyncio.sleep(1)
    #Este es un método asíncrono decorado con @rx.background que se ejecuta en segundo plano y actualiza el reloj cada segundo mientras running es True. Espera un segundo entre cada actualización.
    def flip_switch(self, running: bool):
        """Start or stop the clock.

        Args:
            running: Whether the clock should be running.
        """
        # Set the switch state.
        self.running = running

        # Start the clock if the switch is on.
        if self.running:
            return State.tick
    #Este método se llama para iniciar o detener el reloj. Toma un argumento running que indica si el reloj debería estar funcionando o no. Actualiza el estado running y devuelve el método tick si el reloj está en funcionamiento, lo que permite que el método tick comience a ejecutarse en segundo plano.

def clock_hand(rotation: str, color: str, length: str) -> rx.Component:
    """Create a clock hand.

    Args:
        rotation: The rotation of the clock hand.
        color: The color of the clock hand.
        length: The length of the clock hand.

    Returns:
        A clock hand component.
    """
    return rx.chakra.divider(
        transform=rotation,
        width=f"{length}em",
        position="absolute",
        border_style="solid",
        border_width="4px",
        border_image=f"linear-gradient(to right, rgb(250,250,250) 50%, {color} 100%) 0 0 100% 0",
        z_index=0,
    )


def analog_clock() -> rx.Component:
    """Create the analog clock."""
    return rx.chakra.circle(
        # The inner circle.
        rx.chakra.circle(
            width="1em",
            height="1em",
            border_width="thick",
            border_color="#43464B",
            z_index=1,
        ),
        # The clock hands.
        clock_hand(State.time_info["hour_rotation"], "black", "16"),
        clock_hand(State.time_info["minute_rotation"], "red", "18"),
        clock_hand(State.time_info["second_rotation"], "blue", "19"),
        border_width="thick",
        border_color="#43464B",
        width="25em",
        height="25em",
        bg="rgb(250,250,250)",
        box_shadow="dark-lg",
    )


def digital_clock() -> rx.Component:
    """Create the digital clock."""
    return rx.hstack(
        rx.heading(State.time_info["hour"], size="8"),
        rx.heading(":", size="8"),
        rx.heading(State.time_info["minute_display"], size="8"),
        rx.heading(":", size="8"),
        rx.heading(State.time_info["second_display"], size="8"),
        rx.heading(State.time_info["meridiem"], size="8"),
        border_width="medium",
        border_color="#43464B",
        border_radius="2em",
        padding_inline_start="2em",
        padding_inline_end="2em",
        background="white",
        color="#333",
    )


def timezone_select() -> rx.Component:
    """Create the timezone select."""
    return rx.select(
        TIMEZONES,
        placeholder="Select a time zone.",
        on_change=State.set_zone,
        value=State.valid_zone,
        width="100%",
        size="3",
    )


def index():
    """The main view."""
    return rx.center(
        rx.vstack(
            analog_clock(),
            rx.hstack(
                digital_clock(),
                rx.switch(is_checked=State.running, on_change=State.flip_switch),
                align="center",
                justify="center",
                width="100%",
            ),
            timezone_select(),
            padding="5em",
            border_width="medium",
            border_color="#43464B",
            border_radius="25px",
            background="#ededed",
            text_align="center",
        ),
        padding="5em",
    )


app = rx.App(
    theme=theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="amber",
        gray_color="sand",
    )
)
app.add_page(index, title="Clock", on_load=State.on_load)
