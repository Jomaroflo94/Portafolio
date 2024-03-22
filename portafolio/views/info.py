import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.services.data import Info
from portafolio.styles.styles import Size

def info(title: str, data: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[
                info_detail(item)
                for item in data
            ],
            spacing=Size.MEDIUM.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )