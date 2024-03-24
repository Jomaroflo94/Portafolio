import reflex as rx

from portafolio.components.icon_button import icon_button
from portafolio.services.data import Media
from portafolio.styles.styles import Size

def media(data: list[Media], is_mobile=False) -> rx.Component:
    return rx.flex(
        *[
            icon_button(item.icon, 
                f"{item.url}{item.text}", 
                item.text,
                "solid" if item.is_primary else "surface",
                is_mobile
            )
            for item in data
        ],
        flex_direction="row",
        width="auto",
        flex_wrap="wrap",
        spacing=Size.X_SMALL.value
    )