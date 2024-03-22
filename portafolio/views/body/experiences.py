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
                        height=EmSize.MAXIMUN.value,
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
                    spacing=Size.MEDIUM.value,
                    width="auto"
                ),
                rx.vstack(
                    rx.heading(
                        item.name,
                        size=Size.MEDIUM.value
                    ),
                    rx.vstack(
                        sections(
                            item.sections, 
                            show_icon=False
                        ),
                        spacing=Size.SMALL.value,
                        width="100%"
                    ),
                    padding_top=EmSize.SMALL.value,
                    spacing=Size.MEDIUM.value,
                    width="100%"
                ),
                spacing=Size.DEFAULT.value,
                width="100%"
            )
            for item in experiences
        ],
        spacing=Size.MEDIUM.value,
        width="100%"
    )




    # return rx.vstack(
    #     heading(title),
    #     *[
    #         rx.vstack(
    #             rx.hstack(
    #                 rx.image(
    #                     src="/favicon.ico",
    #                     height=EmSize.MAXIMUN.value,
    #                     width="auto",
    #                     object_fit="cover",
    #                     border_radius=EmSize.SMALL.value, 
    #                 ),
    #                 rx.heading(
    #                     item.name,
    #                     size=Size.MEDIUM.value
    #                 ),
    #                 spacing=Size.DEFAULT.value,
    #                 width="100%"
    #             ),
    #             rx.hstack(
    #                 rx.center(
    #                     rx.divider(
    #                         orientation="vertical", 
    #                         border_color="gray"
    #                     ),
    #                     height="4em"
    #                 ),
    #                 rx.vstack(
    #                     sections(item.sections),
    #                     spacing=Size.MEDIUM.value,
    #                     width="100%"
    #                 ),
    #                 spacing=Size.MEDIUM.value,
    #                 width="100%"
    #             ),
    #             spacing=Size.MEDIUM.value,
    #             width="100%"
    #         )
    #         for item in experiences
    #     ],
    #     spacing=Size.MEDIUM.value,
    #     width="100%"
    # )