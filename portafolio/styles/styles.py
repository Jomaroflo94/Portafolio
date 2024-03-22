import reflex as rx

from enum import Enum

MAX_WIDTH = "900px"
IMAGE_HEIGHT="200px"

# Tamaños soportados por CSS
class EmSize(Enum):
    SMALL = '0.5em'     # 8px
    DEFAULT = '1em'     # 16px
    MEDIUM = '1.5em' # 24px
    BIG = '2em'         # 32px
    MAXIMUN = '3em'        # 48px

# Tamaños soportados por Radix UI
class Size(Enum):
    ZERO = None
    SMALL = '2'         # 8px
    DEFAULT = '4'       # 16px por defecto (1em)
    MEDIUM = '6'        # 32px
    MEDIUM_BIG = '7'    # 40px
    BIG = '8'           # 48px
    MAXIMUN = '9'       # 54px

STYLESHEETS= [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

BASE_STYLE = {
    rx.hstack: {
        "width": "100%"
    },
    rx.vstack: {
        "width": "100%"
    },
    rx.button: {
        "--cursor-button": "pointer"
    },
    rx.link: {
        "text-decoration": "none"
    }
}