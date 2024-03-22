import reflex as rx

from portafolio.components.heading import heading

def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("Sobre mi"),
        rx.text(description)
    )