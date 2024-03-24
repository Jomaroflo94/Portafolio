import reflex as rx

from enum import Enum

MAX_WIDTH = "900px"
IMAGE_HEIGHT="200px"

# Tamaños soportados por CSS
class EmSize(Enum):
    X_SMALL = "0.25em"  # 4px
    SMALL = '0.5em'     # 8px
    DEFAULT = '1em'     # 16px
    LARGE = '1.5em'     # 24px
    X_LARGE = '2em'     # 32px
    XX_LARGE = '3em'    # 48px

# Tamaños soportados por Radix UI
class Size(Enum):
    ZERO = None
    XX_SMALL = '1'      # 4px
    X_SMALL = '2'       # 8px
    SMALL = '3'         # 12px
    DEFAULT = '4'       # 16px por defecto (1em)
    LARGE = '5'         # 24px
    X_LARGE = '6'       # 32px
    XX_LARGE = '7'      # 40px
    XXX_LARGE = '8'     # 48px
    MAXIMUN = '9'       # 54px

STYLESHEETS= [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

BASE_STYLE = {
    rx.grid: {
        "width": "100%"
    },
    rx.card: {
        "width": "100%"
    },
    rx.image: {
        "width": "100%"
    },
    rx.flex: {
        "width": "100%"
    },
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