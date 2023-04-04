import shutil
import textwrap

from color_handling import apply_color

def format_output(common_courses, ge1, ge2, quarter):
    output = []
    output.append(apply_color("bright_green", f"\tCommon courses of {ge1} and {ge2} for {quarter} quarter:"))

    for course in common_courses:
        output.append(apply_color("bright_blue", f"\t\t{course['id']}: {course['title']}"))  # Course ID and title
        output.append(apply_color("bright_black", f"\t\t\tGE: {course['ge_text']}"))  # GE text

        wrapped_description = indent_matcher_overflow(f"\t\t\tDescription: {course['description']}\n")
        colored_wrapped_description = apply_color("bright_cyan", wrapped_description)
        output.append(colored_wrapped_description)

    return "\n".join(output)

def indent_matcher_overflow(text):
    # Detect the indent at the beginning of the text
    indent = ""
    for char in text:
        if char == " " or char == "\t":
            indent += char
        else:
            break

    # Get terminal width
    terminal_width = shutil.get_terminal_size().columns

    # Use textwrap to break the text into lines based on the terminal width
    lines = textwrap.wrap(text, width=terminal_width, subsequent_indent=indent)

    # Join the lines with newlines and return the result
    return "\n".join(lines)