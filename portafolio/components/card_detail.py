import reflex as rx

from portafolio.components.heading import heading
from portafolio.services.data import Other
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size

def card_detail(data : Other, is_mobile: bool) -> rx.Component:
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=data.image,
                    height=IMAGE_HEIGHT,
                    object_fit="cover"
                ),
                pb=Size.DEFAULT.value
            ),
            rx.vstack(
                heading(
                    data.title,
                    size=Size.X_SMALL if is_mobile else Size.DEFAULT
                ),
                rx.text(
                    data.subtitle,
                    color_scheme="gray",
                    size=Size.X_SMALL.value if is_mobile else Size.SMALL.value,
                ),
                spacing=Size.XX_SMALL.value,
                margin_top=EmSize.SMALL.value
            ),
            href=data.url,
            is_external=True
        )
    )