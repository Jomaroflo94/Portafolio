import reflex as rx

from portafolio.components.heading import heading
from portafolio.styles.styles import Size

def about(description: list[str], is_mobile: bool) -> rx.Component:
    return rx.vstack(
        rx.divider(),
        heading(
            "Sobre mi", 
            size=Size.DEFAULT if is_mobile else Size.X_LARGE
        ),
        rx.vstack(
            *[
                rx.text(
                    item,
                    size=Size.XX_SMALL.value if is_mobile else Size.DEFAULT.value
                )
                for item in description
            ],
            spacing=Size.XX_SMALL.value
        ),
        spacing=Size.SMALL.value if is_mobile else Size.DEFAULT.value
    )