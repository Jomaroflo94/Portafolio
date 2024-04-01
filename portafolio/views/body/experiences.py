import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.section_detail import section_detail
from portafolio.services.data import Experience
from portafolio.styles.styles import EmSize, Size
from portafolio.views.body.sections import sections

def experiences(experiences: list[Experience], is_mobile: bool, 
        title: str) -> rx.Component:
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
                    # rx.vstack(
                    #     rx.divider(
                    #         orientation="vertical", 
                    #         border_color="gray",
                    #         size="4"
                    #     ),
                    #     height="100vh",
                    #     margin_left="50%"
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
                            is_mobile,
                            show_icon=False
                        )
                    ),
                    padding_top=EmSize.SMALL.value,
                    spacing=Size.X_LARGE.value,
                    height="100%"
                ),
                height="100% !important",
                spacing=Size.DEFAULT.value
            )
            for item in experiences
        ],
        spacing=Size.X_LARGE.value
    )