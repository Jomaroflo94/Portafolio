import reflex as rx

from portafolio.styles.styles import Size

def avatar(src: str, size: Size) -> rx.Component:
    return rx.avatar(
        radius="full",
        src=src,
        size=size.value
    )