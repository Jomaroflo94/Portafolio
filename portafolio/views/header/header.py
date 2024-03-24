import reflex as rx

from portafolio.components.avatar import avatar
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.components.text_icon import text_icon
from portafolio.services.data import Data, Media, Profile
from portafolio.styles.styles import EmSize, Size

def header(profile: Profile, media_list: list[Media], is_mobile: bool) -> rx.Component:
    return rx.cond(
        is_mobile,
        header_mobile(profile, media_list),
        header_desktop(profile, media_list)
    )

def header_desktop(profile: Profile, media_list: list[Media]) -> rx.Component:
    return rx.center(
        rx.hstack(
            avatar(profile.avatar, Size.MAXIMUN),
            rx.vstack(
                rx.vstack(
                    heading(profile.name, size=Size.XXX_LARGE),
                    heading(profile.position, as_="h3")
                ),
                text_icon(profile.location, "map-pin"),
                media(media_list),
                spacing=Size.DEFAULT.value
            ),
            spacing=Size.X_LARGE.value
        )
    )

def header_mobile(profile: Profile, media_list: list[Media]) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            avatar(profile.avatar, Size.XX_LARGE),
            rx.vstack(
                heading(profile.name),
                heading(profile.position, as_="h3", size=Size.X_SMALL),
                margin_top=EmSize.X_SMALL.value
            ),
            spacing=Size.DEFAULT.value
        ),
        text_icon(profile.location, "map-pin", True),
        media(media_list, True),
        spacing=Size.X_SMALL.value
    )



