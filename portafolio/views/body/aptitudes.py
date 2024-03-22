import reflex as rx

from portafolio.components.heading import heading
from portafolio.services.data import Technology
from portafolio.styles.styles import EmSize, Size

def aptitudes(data : list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Tecnologías"),
        rx.flex(
            
            *[
                rx.badge(
                    rx.box(
                        class_name=aptitude.icon,
                        font_size=EmSize.MEDIUM.value
                    ),
                    rx.text(aptitude.name),
                    size="2"
                )
                for aptitude in sorted(data, key = lambda x : x.name)
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )