import reflex as rx

from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.services.data import Other
from portafolio.styles.styles import Size

def others(data: list[Other]) -> rx.Component:
    return rx.vstack(
        heading("Otras referencias"),
        rx.mobile_only(
            rx.vstack(
                *[
                    card_detail(item)
                    for item in data
                ],
                spacing=Size.DEFAULT.value,
                width="100%"
            ),
            width="100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *[
                    card_detail(item)
                    for item in data
                ],
                spacing=Size.DEFAULT.value,
                columns="3"
            ),
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )