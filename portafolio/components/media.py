import reflex as rx

from portafolio.components.icon_button import icon_button
from portafolio.services.data import Media
from portafolio.styles.styles import Size

def media(data: Media) -> rx.Component:
    return rx.flex(
        icon_button("mail", 
            f"mailto:{data.email}", 
            text=data.email
        ),
        rx.hstack(
            icon_button("file-text", 
                data.cv,
                variant="surface"
            ),
            icon_button("github", 
                data.github,
                variant="surface"
            ),
            icon_button("linkedin", 
                data.linkedin, 
                variant="surface"
            ),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )