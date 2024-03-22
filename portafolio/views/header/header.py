import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.components.text_icon import text_icon
from portafolio.services.data import Data
from portafolio.styles.styles import EmSize, Size

def header_desktop(data: Data) -> rx.Component:
    return rx.center(
        rx.hstack(
            header_avatar(data.avatar, Size.MAXIMUN),
            rx.vstack(
                rx.vstack(
                    heading(data.name, size=Size.BIG),
                    heading(data.title),
                    spacing=Size.SMALL.value,
                    width="100%"
                ),
                text_icon(data.location, "map-pin"),
                media(data.media),
                spacing=Size.DEFAULT.value,
                width="100%"
            ),
            spacing=Size.MEDIUM.value,
            width="100%"
        ),
        width="100%"
    )

def header_mobile(data: Data) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            header_avatar(data.avatar, Size.MEDIUM_BIG),
            rx.vstack(
                heading(data.name, size=Size.MEDIUM),
                heading(data.name, as_="h3", size=Size.SMALL),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        text_icon(data.location, "map-pin"),
        media(data.media),
        spacing=Size.DEFAULT.value,
        width="100%"
    )

def header_avatar(src: str, size: Size) -> rx.Component:
    return rx.avatar(
        radius="full",
        src=src,
        size=size.value
    )



