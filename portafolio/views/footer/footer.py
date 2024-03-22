import reflex as rx

from portafolio.components.media import media
from portafolio.services.data import Data
from portafolio.styles.styles import Size

def footer(data: Data) -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.hstack(
                rx.vstack(
                    rx.text.strong(data.name),
                    media(data.media),
                    spacing=Size.SMALL.value,
                    width="100%"
                ),
                spacing=Size.DEFAULT.value,
                width="100%"
            ),
            rx.mobile_only(
                footer_last_update(data.last_update, True)
            ),
            rx.tablet_and_desktop(
                footer_last_update(data.last_update),
                width="100%"
            ),
            spacing=Size.MEDIUM.value,
            width="100%",
            flex_direction=["column", "row"]
        ),
        spacing=Size.SMALL.value,
        width="100%"
    )

def footer_last_update(last_update: str, mobile=False)-> rx.Component:
    return rx.vstack(
        rx.text.strong("Última actualización:"),
        rx.text(last_update),
        width="100%",
        align="end" if not mobile else "start"
    )