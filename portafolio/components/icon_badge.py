import reflex as rx

from portafolio.styles.styles import EmSize

def icon_badge(icon: str, size=32, variant="soft") -> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            size=size
        ),
        aspect_ratio="1",
        variant=variant
    )