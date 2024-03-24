import reflex as rx

from portafolio.styles.styles import Size

def icon_button(icon: str, url: str, text="", 
        variant="solid", is_mobile=False) -> rx.Component:
    return rx.button(
        rx.icon(
            icon,
            size=16 if is_mobile else 24
        ),
        text,
        size=Size.XX_SMALL.value if is_mobile else Size.X_SMALL.value,
        variant=variant,
        on_click=rx.redirect(url, True)
    )