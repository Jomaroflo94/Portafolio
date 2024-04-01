import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.section_detail import section_detail
from portafolio.services.data import Section
from portafolio.styles.styles import Size

def sections(data: list[Section], is_mobile: bool, 
        title="", no_divider=False) -> rx.Component:
    return rx.vstack(
        rx.cond(
            not no_divider,
            rx.divider()
        ),
        sections_title(title, is_mobile),
        sections_details(data, is_mobile),
        spacing=Size.DEFAULT.value if is_mobile else Size.LARGE.value
    )

def sections_title(title: str, is_mobile: bool) -> rx.Component:
    return rx.cond(
        title != "",
        heading(
            title,
            size=Size.DEFAULT if is_mobile else Size.X_LARGE
        )
    )

def sections_details(data: list[Section], is_mobile: bool) -> rx.Component:
    return rx.vstack(
        *[
            section_detail(item, is_mobile)
            for item in data
        ],
        spacing=Size.DEFAULT.value if is_mobile else Size.X_LARGE.value
    )