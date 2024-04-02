import reflex as rx

from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.body.about import about
from portafolio.views.body.technologies import technologies
from portafolio.views.body.experiences import experiences
from portafolio.views.footer.footer import footer
from portafolio.views.header.header import header
from portafolio.views.body.sections import sections
from portafolio.views.body.others import others
from portafolio.services.data import data

DATA = data
title = "Portafolio - Jose Manuel Romero Flores"
description = "Jose Manuel Romero Flores"
image = "/avatar.jpg"

def index() -> rx.Component:
    return rx.center(
        rx.script("document.documentElement.lang='es'"),
        # rx.theme_panel(),
        rx.mobile_only(
            content(True),
            width="inherit"
        ),
        rx.tablet_and_desktop(
            content(),
            width="inherit"
        )
    )

def content(is_mobile=False) -> rx.Component:
    return rx.vstack(
        header(DATA.profile, DATA.media, is_mobile),
        about(DATA.about, is_mobile),
        technologies(DATA.technologies, is_mobile),
        experiences(DATA.experiences, is_mobile, "Experiencia"),
        sections(DATA.projects, is_mobile, "Proyectos"),
        sections(DATA.training, is_mobile, "Formación"),
        others(DATA.others, is_mobile),
        footer(DATA.profile, DATA.media, is_mobile),
        spacing=Size.DEFAULT.value if is_mobile else Size.LARGE.value,
        max_width=MAX_WIDTH,
        padding_x=EmSize.X_LARGE.value,
        padding_y=EmSize.XX_LARGE.value
    )

app = rx.App(
    style=BASE_STYLE,
    stylesheets=STYLESHEETS,
    theme=rx.theme(
        appearance="dark",
        accent_color="violet",
        radius="large"
    )
)

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {
            "name": "og:title", 
            "content": title
        },
        {
            "name": "og:description", 
            "content": description
        },
        {
            "name": "og:image", 
            "content": image
        }
    ]
)