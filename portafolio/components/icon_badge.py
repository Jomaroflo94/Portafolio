import reflex as rx

from portafolio.styles.styles import EmSize

def icon_badge(icon: str, variant="soft", is_mobile=False) -> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            size=28 if is_mobile else 32
        ),
        aspect_ratio="1",
        variant=variant
    )