import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.services.data import Data
from portafolio.styles.styles import Size

def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            radius="full",
            src=data.avatar,
            size=Size.MAXIMUN.value
        ),
        rx.vstack(
            heading(data.name, True),
            heading(data.title),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit"
            ),
            media(data.media),
            spacing=Size.SMALL.value
        ),
        spacing=Size.MEDIUM.value
    )