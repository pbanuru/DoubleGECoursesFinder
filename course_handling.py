from query_handling import run_query, extract_courses_from_result, QUERY_TEMPLATE
from output_formatting import format_output
from color_handling import apply_color

NO_COMMON_COURSES_FOUND = False
NO_OUTPUT = ""
NO_COMMON_COURSES_FOUND_MESSAGE = "No common courses found."

def get_common_courses(courses1, courses2, online_only):
    common_courses_found = []
    common_courses = set(courses1.keys()).intersection(set(courses2.keys()))

    if not common_courses:
        return common_courses_found

    for course_id in common_courses:
        course = courses1[course_id]
        meetings = course.get("meetings", [])
        if not online_only or any(meeting.get("building") == "ON LINE" for meeting in meetings):
            course_title = course["course"]["title"]
            course_description = course["course"]["description"]
            ge_text = course["course"]["ge_text"]
            common_courses_found.append((course_id, course_title, course_description, ge_text))

    return common_courses_found

def fetch_courses(ge, quarter):
    query_variables = {"ge": ge, "quarter": quarter}
    result = run_query(QUERY_TEMPLATE, query_variables)
    courses = extract_courses_from_result(result)
    return courses

def find_common_courses(ge_category1, ge_category2, quarter, online_only=False):
    courses1 = fetch_courses(ge_category1, quarter)
    courses2 = fetch_courses(ge_category2, quarter)

    common_courses_found = get_common_courses(courses1, courses2, online_only)

    if not common_courses_found:
        return NO_COMMON_COURSES_FOUND, NO_OUTPUT

    output = format_output(common_courses_found, ge_category1, ge_category2, quarter)

    return True, output


def pair_ge_categories(ge_pair1, ge_pair2, quarter, online_only=False):
    found_common_courses1, output1 = find_common_courses(ge_pair1[0], ge_pair1[1], quarter, online_only)
    found_common_courses2, output2 = find_common_courses(ge_pair2[0], ge_pair2[1], quarter, online_only)

    if found_common_courses1 and found_common_courses2:
        print(output1)
        print(output2)
    else:
        print(apply_color("red", f"\t\t{NO_COMMON_COURSES_FOUND_MESSAGE}"))

