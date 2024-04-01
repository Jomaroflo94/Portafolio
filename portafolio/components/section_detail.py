import reflex as rx
from portafolio.components.heading import heading

from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.services.data import Media, Section, Technology
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size

def section_detail(data: Section, is_mobile: bool) -> rx.Component:
    return rx.cond(
        is_mobile,
        section_detail_mobile(data),
        section_detail_desktop(data)
    )

def section_detail_desktop(data: Section) -> rx.Component:
    return rx.flex(
        rx.hstack(
            section_icon(data.icon),
            section_image_icon(data.image_icon),
            rx.vstack(
                heading(data.title, as_="h3", size=Size.DEFAULT),
                section_content(data.subtitle, data.description, 
                    data.media, data.technologies),
                spacing=Size.XX_SMALL.value
            ),
            spacing=Size.DEFAULT.value
        ),
        section_detail_image(data.image),
        section_detail_auxiliar(data.date),
        spacing=Size.DEFAULT.value,
        flex_direction="row"
    )

def section_detail_mobile(data: Section) -> rx.Component:
    return rx.flex(
        section_detail_image(data.image),
        section_detail_auxiliar(data.date),
        rx.vstack(
            rx.center(
                section_icon(data.icon, True),
                section_image_icon(data.image_icon, True),
                heading(data.title, as_="h3", size=Size.X_SMALL),
                spacing=Size.SMALL.value
            ),
            section_content(data.subtitle, data.description, 
                data.media, data.technologies, True),
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value,
        flex_direction="column",
        background="rgba(110,86,207,.2)",
        padding=EmSize.DEFAULT.value,
        border_radius=EmSize.DEFAULT.value
    )

def section_icon(icon: str, is_mobile=False) -> rx.Component:
    return rx.cond(
        icon != "",
        icon_badge(
            icon=icon if icon != "" else "tag", 
            is_mobile=is_mobile
        )
    ) 

def section_image_icon(icon_image: str, is_mobile=False) -> rx.Component:
    return rx.cond(
        icon_image != "",
        rx.image(
            src=icon_image,
            height=EmSize.X_LARGE.value if is_mobile else EmSize.XX_LARGE.value,
            width="auto",
            object_fit="cover",
            border_radius=EmSize.SMALL.value, 
        )
    )

def section_content(subtitle: str, description: list[str], media: list[Media],
        technologies: list[Technology], is_mobile=False) -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text(
                subtitle,
                size=Size.X_SMALL.value if is_mobile else Size.SMALL.value
            ),
            rx.vstack(
                *[
                    rx.text(
                        item,
                        size=Size.XX_SMALL.value if is_mobile else Size.SMALL.value,
                        color_scheme="gray"
                    )
                    for item in description
                ],
                spacing=Size.XX_SMALL.value if is_mobile else Size.X_SMALL.value
            ),
            spacing=Size.X_SMALL.value if is_mobile else Size.SMALL.value
        ),
        rx.vstack(
            section_detail_techologies(technologies),
            section_detail_links(media, is_mobile),
            spacing=Size.X_SMALL.value if is_mobile else Size.SMALL.value
        ),
        spacing=Size.SMALL.value
    ) 

def section_detail_techologies(data: list[Technology]) -> rx.Component:
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
            wrap="wrap",
            spacing=Size.XX_SMALL.value
        )
    )

def section_detail_links(media: list[Media], is_mobile=False) -> rx.Component:
    return rx.cond(
        media,
        rx.hstack(
            *[
                icon_button(item.icon,
                    item.url,
                    variant="solid" if item.is_primary else "surface",
                    is_mobile=is_mobile
                )
                for item in media
            ]
        )
    )

def section_detail_image(image: str) -> rx.Component:
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

def section_detail_auxiliar(date: str) -> rx.Component:
    return rx.cond(
        date != "",
        rx.box(
            rx.hstack(
                rx.cond(
                    date != "",
                    rx.badge(date),
                ),
                align="end"
            ),
            flex_grow=0
        )
    )