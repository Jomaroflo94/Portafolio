import reflex as rx
from portafolio.components.heading import heading

from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.services.data import Media, Section, Technology
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size

def section_detail(data: Section, is_mobile: bool, show_icon: bool) -> rx.Component:
    return rx.cond(
        is_mobile,
        section_detail_mobile(data, show_icon),
        section_detail_desktop(data, show_icon)
    )

def section_detail_desktop(data: Section, show_icon: bool) -> rx.Component:
    return rx.flex(
        rx.hstack(
            section_icon(data.icon, show_icon),
            rx.vstack(
                heading(data.title, as_="h3", size=Size.DEFAULT),
                section_content(data.subtitle, data.description, 
                    data.media, data.technologies)
            ),
            spacing=Size.DEFAULT.value
        ),
        section_detail_image(data.image),
        section_detail_auxiliar(data.date),
        spacing=Size.DEFAULT.value,
        flex_direction="row"
    )

def section_detail_mobile(data: Section, show_icon: bool) -> rx.Component:
    return rx.flex(
        section_detail_image(data.image),
        section_detail_auxiliar(data.date),
        rx.vstack(
            rx.hstack(
                section_icon(data.icon, show_icon, True),
                heading(data.title, as_="h3", size=Size.SMALL),
                spacing=Size.DEFAULT.value
            ),
            section_content(data.subtitle, data.description, 
                data.media, data.technologies, True),
            spacing=Size.DEFAULT.value
        ),
        spacing=Size.DEFAULT.value,
        flex_direction="column"
    )

def section_icon(icon: str, show_icon: bool, 
        is_mobile=False) -> rx.Component:
    return rx.cond(
        show_icon,
        icon_badge(icon, 
            is_mobile=is_mobile
        )
    )

def section_content(subtitle: str, description: str, media: list[Media],
        technologies: list[Technology], is_mobile=False) -> rx.Component:
    return rx.vstack(
        rx.text(
            subtitle,
            size=Size.X_SMALL.value if is_mobile else Size.SMALL.value
        ),
        rx.text(
            description,
            size=Size.X_SMALL.value if is_mobile else Size.SMALL.value,
            color_scheme="gray"
        ),
        section_detail_techologies(technologies),
        section_detail_links(media, is_mobile),
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