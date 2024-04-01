import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.services.data import Data, Media, Profile
from portafolio.styles.styles import EmSize, Size

def footer(profile: Profile, media_list: list[Media], is_mobile: bool) -> rx.Component:
    return rx.vstack(
        rx.divider(),
        rx.flex(
            footer_media(profile.name, media_list, is_mobile),
            footer_last_update(profile.last_update, is_mobile),
            spacing=Size.DEFAULT.value,
            margin_top=EmSize.SMALL.value if is_mobile else EmSize.DEFAULT.value,
            flex_direction=["column", "row"]
        )
    )

def footer_media(name: str, media_list: list[Media], is_mobile: bool)-> rx.Component:
    return rx.hstack(
        rx.vstack(
            heading(
                name,
                as_="h3",
                size=Size.X_SMALL if is_mobile else Size.SMALL
            ),
            media(media_list, is_mobile),
            spacing=Size.X_SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )

def footer_last_update(last_update: str, is_mobile: bool)-> rx.Component:
    return rx.vstack(
        heading(
            "Última actualización:",
            as_="h3",
            size=Size.X_SMALL if is_mobile else Size.SMALL
        ),
        rx.text(
            last_update,
            size=Size.X_SMALL.value if is_mobile else Size.SMALL.value
        ),
        align="end" if not is_mobile else "start",
        spacing=Size.XX_SMALL.value if is_mobile else Size.X_SMALL.value
    )