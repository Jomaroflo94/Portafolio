import reflex as rx

from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.body.about import about
from portafolio.views.body.aptitudes import aptitudes
from portafolio.views.body.experiences import experiences
from portafolio.views.footer.footer import footer
from portafolio.views.header.header import header
from portafolio.views.body.sections import sections
from portafolio.views.body.others import others
from portafolio.services.data import data

DATA = data

def index() -> rx.Component:
    return rx.center(
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
        rx.divider(),
        about(DATA.about, is_mobile),
        rx.divider(),
        aptitudes(DATA.technologies, is_mobile),
        rx.divider(),
        experiences(DATA.experiences, "Experiencia"),
        rx.divider(),
        sections(DATA.projects, "Proyectos"),
        rx.divider(),
        sections(DATA.training, "Formación"),
        rx.divider(),
        others(DATA.others, is_mobile),
        rx.divider(),
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
app.add_page(index)