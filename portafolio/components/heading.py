import reflex as rx

from portafolio.styles.styles import Size

def heading(text: str, as_="h1", size=Size.X_LARGE) -> rx.Component:
    return rx.heading(
        text, 
        as_=as_,
        size=size.value
    )