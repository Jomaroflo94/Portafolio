import reflex as rx

from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.services.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size

def info_detail(data: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(data.icon),
            rx.vstack(
                rx.vstack(
                    rx.text.strong(data.title),
                    rx.text(data.subtitle),
                    rx.text(
                        data.description,
                        size=Size.SMALL.value,
                        color_scheme="gray"
                    )
                ),
                rx.cond(
                    data.technologies,
                    rx.flex(
                        *[
                            rx.badge(
                                item.name,
                                color_scheme="gray"
                            )
                            for item in data.technologies
                        ],
                        wrap="wrap",
                        spacing=Size.SMALL.value
                    )
                ),
                rx.cond(
                    data.url != "" or data.github != "",
                    rx.hstack(
                        rx.cond(
                            data.url != "",
                            icon_button(
                                "link",
                                data.url,
                                variant="surface"
                            )
                        ),
                        rx.cond(
                            data.github != "",
                            icon_button(
                                "github",
                                data.github,
                                variant="surface"
                            )
                        )
                    )
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        info_detail_image(data.image),
        info_detail_auxiliar(data.date, data.certificate),
        spacing=Size.DEFAULT.value,
        width="100%",
        flex_direction=["column-reverse", "row"]
    )

def info_detail_image(image: str) -> rx.Component:
    return rx.cond(
        image != "",
        rx.image(
            src=image,
            height=IMAGE_HEIGHT,
            width="auto",
            border_radius=EmSize.DEFAULT.value, 
            object_fit="cover"
        )
    )

def info_detail_auxiliar(date: str, certificate: str) -> rx.Component:
    return rx.cond(
        date != "" or certificate != "",
        rx.vstack(
            rx.cond(
                date != "",
                rx.badge(date),
            ),
            rx.cond(
                certificate != "",
                icon_button(
                    "shield-check",
                    certificate
                )
            ),
            spacing=Size.SMALL.value,
            align="end"
        )
    )