import reflex as rx

from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.services.data import Other
from portafolio.styles.styles import Size

def others(data: list[Other], is_mobile: bool) -> rx.Component:
    return rx.cond(
        len(data) > 0,
        rx.vstack(
            rx.divider(),
            heading(
                "Otras referencias",
                size=Size.DEFAULT if is_mobile else Size.X_LARGE
            ),
            rx.cond(
                is_mobile,
                others_mobile(data),
                others_desktop(data)
            ),
            spacing=Size.DEFAULT.value
        )
    )


def others_mobile(data: list[Other]) -> rx.Component:
    return rx.vstack(
        *[
            card_detail(item, True)
            for item in data
        ],
        spacing=Size.DEFAULT.value
    )

def others_desktop(data: list[Other]) -> rx.Component:
    return rx.grid(
        *[
            card_detail(item, False)
            for item in data
        ],
        spacing=Size.DEFAULT.value,
        columns="3"
    )