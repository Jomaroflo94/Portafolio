import reflex as rx

from portafolio.services.data import Other
from portafolio.styles.styles import IMAGE_HEIGHT, Size

def card_detail(data : Other) -> rx.Component:
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=data.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover"
                ),
                pb=Size.DEFAULT.value
            ),
            rx.text.strong(
                data.title,
                size=Size.DEFAULT.value,
            ),
            rx.text(
                data.subtitle,
                size=Size.SMALL.value,
                color_scheme="gray"
            ),
            href=data.url,
            is_external=True
        ),
        width="100%"
    )