import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.services.data import Section
from portafolio.styles.styles import Size

def sections(data: list[Section], title="", show_icon=True) -> rx.Component:
    return rx.vstack(
        rx.cond(
            title != "",
            heading(title)
        ),
        rx.vstack(
            *[
                info_detail(item, show_icon)
                for item in data
            ],
            spacing=Size.X_LARGE.value
        ),
        spacing=Size.DEFAULT.value
    )