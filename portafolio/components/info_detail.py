import reflex as rx

from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.services.data import Section, Technology
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size

def info_detail(data: Section, show_icon: bool) -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.cond(
                show_icon,
                icon_badge(data.icon)
            ),
            rx.vstack(
                info_detail_text(data.title, data.subtitle, data.description),
                info_detail_techologies(data.technologies),
                info_detail_links(data.url, data.github)
            ),
            spacing=Size.DEFAULT.value
        ),
        info_detail_image(data.image),
        info_detail_auxiliar(data.date, data.certificate),
        spacing=Size.DEFAULT.value,
        flex_direction=["column-reverse", "row"]
    )

def info_detail_text(title: str, subtitle: str, description: str) -> rx.Component:
    return rx.vstack(
        rx.text.strong(title),
        rx.text(subtitle),
        rx.text(
            description,
            color_scheme="gray"
        )
    )

def info_detail_techologies(data: list[Technology]) -> rx.Component:
    return rx.cond(
        data,
        rx.flex(
            *[
                rx.badge(
                    item.name,
                    color_scheme="gray"
                )
                for item in data
            ],
            wrap="wrap"
        )
    )

def info_detail_links(url: str, github: str) -> rx.Component:
    return rx.cond(
        url != "" or github != "",
        rx.hstack(
            rx.cond(
                url != "",
                icon_button(
                    "link",
                    url,
                    variant="surface"
                )
            ),
            rx.cond(
                github != "",
                icon_button(
                    "github",
                    github,
                    variant="surface"
                )
            )
        )
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
        rx.box(
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
                align="end"
            ),
            flex_grow=0
        )
    )