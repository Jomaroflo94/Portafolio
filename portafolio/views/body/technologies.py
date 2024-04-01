import reflex as rx

from portafolio.components.badge import badge
from portafolio.components.heading import heading
from portafolio.services.data import Technology
from portafolio.styles.styles import EmSize, Size

def technologies(data : list[Technology], is_mobile: bool) -> rx.Component:
    return rx.vstack(
        rx.divider(),
        heading(
            "Tecnologías",
            size=Size.DEFAULT if is_mobile else Size.X_LARGE
        ),
        rx.flex(
            
            *[
                badge(
                    aptitude.name, 
                    aptitude.icon,
                    EmSize.DEFAULT if is_mobile else EmSize.LARGE,
                    Size.XX_SMALL.value if is_mobile else Size.X_SMALL.value
                )
                for aptitude in sorted(data, key = lambda x : x.name)
            ],
            spacing=Size.X_SMALL.value,
            wrap="wrap"
        ),
        spacing=Size.DEFAULT.value
    )