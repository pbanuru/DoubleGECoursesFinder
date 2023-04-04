# Custom exception class for invalid color errors
class InvalidColorError(Exception):
    pass

# Dictionary containing ANSI Escape color codes for the terminal
# If you aren't familiar with ANSI Escape codes, watch this: https://youtu.be/W0mlGkew6K4
COLOR_CODES = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m"
}

# ANSI Escape Reset code to clear color formatting
RESET_CODE = "\033[0m"

# Apply the specified color to a given text
def apply_color(color : str, text : str) -> str:
    if color in COLOR_CODES:
        # Apply the color code to the text and reset the formatting
        colored_output = f"{COLOR_CODES[color]}{text}{RESET_CODE}"
    else:
        raise InvalidColorError(f"{COLOR_CODES['red']}Invalid color specified: {RESET_CODE}{color}")
    
    return colored_output
