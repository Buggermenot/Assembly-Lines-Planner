class colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def PINK(s: str) -> str:
    return colors.PINK + s + colors.DEFAULT

def BLUE(s: str) -> str:
    return colors.BLUE + s + colors.DEFAULT

def CYAN(s: str) -> str:
    return colors.CYAN + s + colors.DEFAULT

def GREEN(s: str) -> str:
    return colors.GREEN + s + colors.DEFAULT

def RED(s: str) -> str:
    return colors.RED + s + colors.DEFAULT

def YELLOW(s: str) -> str:
    return colors.YELLOW + s + colors.DEFAULT

def DEFAULT() -> str:
    return colors.DEFAULT

def BOLD(s: str) -> str:
    return colors.BOLD + s + colors.DEFAULT

def UNDERLINE(s: str) -> str:
    return colors.UNDERLINE + s + colors.DEFAULT