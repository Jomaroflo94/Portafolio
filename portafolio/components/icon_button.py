import reflex as rx

def icon_button(icon: str, url: str, text="", variant="solid") -> rx.Component:
    return rx.button(
        rx.icon(icon),
        text,
        variant=variant,
        on_click=rx.redirect(url, True)
    )