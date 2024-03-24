import reflex as rx

from portafolio.styles.styles import Size

def text_icon(text: str, icon: str, is_mobile=False) -> rx.Component:
    return rx.hstack(
        rx.icon(
            icon,
            size=16 if is_mobile else 24
        ),
        rx.text(
            text,
            size=Size.X_SMALL.value if is_mobile else Size.DEFAULT.value
        ),
        spacing=Size.X_SMALL.value
    )