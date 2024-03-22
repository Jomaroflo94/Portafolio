import reflex as rx

from portafolio.components.media import media
from portafolio.services.data import Data
from portafolio.styles.styles import Size

def footer(data: Data) -> rx.Component:
    return rx.vstack(
        rx.text(data.name),
        media(data.media),
        spacing=Size.SMALL.value
    )