import reflex as rx

from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.body.about import about
from portafolio.views.body.aptitudes import aptitudes
from portafolio.views.body.experiences import experiences
from portafolio.views.footer.footer import footer
from portafolio.views.header.header import header_mobile, header_desktop
from portafolio.views.body.sections import sections
from portafolio.views.body.others import others
from portafolio.services.data import data

DATA = data

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.mobile_only(
                header_mobile(DATA)
            ),
            rx.tablet_and_desktop(
                header_desktop(DATA)
            ),
            about(DATA.about),
            rx.divider(),
            aptitudes(DATA.technologies),
            rx.divider(),
            experiences(DATA.experiences, "Experiencia"),
            rx.divider(),
            sections(DATA.projects, "Proyectos"),
            sections(DATA.training, "Formación"),
            others(DATA.others),
            rx.divider(),
            footer(DATA),
            spacing=Size.MEDIUM.value,
            max_width=MAX_WIDTH,
            padding_x=EmSize.BIG.value,
            padding_y=EmSize.MAXIMUN.value,
            width="100%"
        )
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