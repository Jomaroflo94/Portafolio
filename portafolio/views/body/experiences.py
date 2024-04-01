import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.section_detail import section_detail
from portafolio.services.data import Experience, Section
from portafolio.styles.styles import EmSize, Size
from portafolio.views.body.sections import sections

def experiences(experiences: list[Experience], is_mobile: bool, 
        title: str) -> rx.Component:
    return rx.cond(
        is_mobile,
        experiences_mobile(experiences, title),
        experiences_desktop(experiences, title)
    )

def experiences_desktop(experiences: list[Experience], title: str) -> rx.Component:
    return rx.vstack(
        rx.divider(),
        heading(title, size=Size.X_LARGE),
        *[
            rx.hstack(
                rx.vstack(
                    company_image(item.image),
                    vertical_divider(len(item.sections)),
                    spacing=Size.LARGE.value,
                    width="auto"
                ),
                rx.vstack(
                    company_name(item.name),
                    content(item.sections),
                    padding_top=EmSize.SMALL.value,
                    spacing=Size.X_LARGE.value
                ),
                spacing=Size.DEFAULT.value
            )
            for item in experiences
        ],
        spacing=Size.X_LARGE.value
    ) 

def experiences_mobile(experiences: list[Experience], title: str) -> rx.Component:
    return rx.vstack(
        rx.divider(),
        heading(title, size=Size.DEFAULT),
        *[
            rx.vstack(
                rx.center(
                    company_image(item.image, True),
                    company_name(item.name, True),
                    spacing=Size.SMALL.value,
                    width="auto"
                ),
                content(item.sections, True),
                spacing=Size.DEFAULT.value
            )
            for item in experiences
        ],
        spacing=Size.LARGE.value
    ) 

def company_image(image: str, is_mobile=False) -> rx.Component:
    return rx.image(
        src=image,
        height=EmSize.X_LARGE.value if is_mobile else EmSize.XX_LARGE.value,
        width="auto",
        object_fit="cover",
        border_radius=EmSize.SMALL.value, 
    )

def company_name(name: str, is_mobile=False) -> rx.Component:
    return rx.heading(
        name,
        size=Size.DEFAULT.value if is_mobile else Size.X_LARGE.value
    )

def vertical_divider(sections_lenght: int) -> rx.Component:
    return rx.vstack(
        rx.divider(
            orientation="vertical",
            border="1px solid rgba(220, 220, 220, .2)",
            size=Size.DEFAULT.value,
            height= str(6*sections_lenght +
                6*(sections_lenght - 1)) + "em"
        ),
        margin_left="50%"
    )

def content(section_list: list[Section], is_mobile=False) -> rx.Component:
    return rx.vstack(
        sections(
            section_list,
            is_mobile=is_mobile,
            no_divider=True
        )
    )