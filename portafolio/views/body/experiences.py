import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.services.data import Experience
from portafolio.styles.styles import EmSize, Size
from portafolio.views.body.sections import sections

def experiences(experiences: list[Experience], title: str) -> rx.Component:
    return rx.vstack(
        heading(title),
        *[
            rx.hstack(
                rx.vstack(
                    rx.image(
                        src=item.image,
                        height=EmSize.XX_LARGE.value,
                        width="auto",
                        object_fit="cover",
                        border_radius=EmSize.SMALL.value, 
                    ),
                    # rx.center(
                    #     rx.divider(
                    #         orientation="vertical", 
                    #         border_color="gray",
                    #         size="4"
                    #     ),
                    #     height="4em",
                    # ),
                    spacing=Size.X_LARGE.value,
                    width="auto"
                ),
                rx.vstack(
                    rx.heading(
                        item.name,
                        size=Size.X_LARGE.value
                    ),
                    rx.vstack(
                        sections(
                            item.sections, 
                            show_icon=False
                        )
                    ),
                    padding_top=EmSize.SMALL.value,
                    spacing=Size.X_LARGE.value
                ),
                spacing=Size.DEFAULT.value
            )
            for item in experiences
        ],
        spacing=Size.X_LARGE.value
    )