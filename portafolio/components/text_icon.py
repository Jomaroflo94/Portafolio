import reflex as rx

from portafolio.styles.styles import Size

def text_icon(text: str, icon: str) -> rx.Component:
    return rx.flex(
        rx.icon(icon),
        rx.text(text),
        direction="row",
        spacing=Size.SMALL.value,
        width="100%"
    )