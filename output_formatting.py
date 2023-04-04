import shutil
import textwrap
from typing import List, Dict

from color_handling import apply_color

def format_output(common_courses: List[Dict], ge_first: str, ge_second: str, quarter: str) -> str:
    output = []
    output.append(apply_color("bright_green", f"\tCommon courses of {ge_first} and {ge_second} for {quarter} quarter:"))

    for course in common_courses:
        course_id = course['id']
        course_title = course['title']
        course_ge = course['ge_text']
        course_description = course['description']

        output.append(apply_color("bright_blue", f"\t\t{course_id}: {course_title}"))
        output.append(apply_color("bright_black", f"\t\t\tGE: {course_ge}"))

        wrapped_description = indent_wrap_text(f"\t\t\tDescription: {course_description}\n")
        colored_wrapped_description = apply_color("bright_cyan", wrapped_description)
        output.append(colored_wrapped_description)

    return "\n".join(output)

def indent_wrap_text(text: str) -> str:
    indent = ""
    for char in text:
        if char == " " or char == "\t":
            indent += char
        else:
            break

    terminal_width = shutil.get_terminal_size().columns

    lines = textwrap.wrap(text, width=terminal_width, subsequent_indent=indent)

    return "\n".join(lines)
