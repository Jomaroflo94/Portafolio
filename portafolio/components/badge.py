import reflex as rx

from portafolio.styles.styles import EmSize, Size

def badge(text: str, icon: str, icon_size: EmSize, badge_size="2") -> rx.Component:
    return rx.badge(
        rx.cond(
            icon != "",
            rx.box(
                class_name=icon,
                font_size=icon_size.value
            )
        ),
        rx.text(text),
        size=badge_size
    )