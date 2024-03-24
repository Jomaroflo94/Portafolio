import reflex as rx

from portafolio.components.heading import heading
from portafolio.styles.styles import Size

def about(description: str, is_mobile: bool) -> rx.Component:
    return rx.vstack(
        heading(
            "Sobre mi", 
            size=Size.DEFAULT if is_mobile else Size.X_LARGE
        ),
        rx.text(
            description,
            size=Size.X_SMALL.value if is_mobile else Size.DEFAULT.value
        )
    )