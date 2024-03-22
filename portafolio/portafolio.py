import reflex as rx

from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.aptitudes import aptitudes
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.others import others
from portafolio.services.data import data

DATA = data

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(DATA),
            about(DATA.about),
            rx.divider(),
            aptitudes(DATA.technologies),
            rx.divider(),
            info("Experiencia", DATA.experience),
            info("Proyectos", DATA.projects),
            info("Formación", DATA.training),
            others(DATA.others),
            rx.divider(),
            footer(DATA),
            spacing=Size.MEDIUM.value,
            max_width=MAX_WIDTH,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            width="100%"
        )
    )

app = rx.App(
    style=BASE_STYLE,
    stylesheets=STYLESHEETS,
    theme=rx.theme(
        appearance="dark",
        accent_color="green",
        radius="large"
    )
)
app.add_page(index)