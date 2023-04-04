from query_handling import run_query, extract_courses_from_result, QUERY_TEMPLATE
from output_formatting import format_output
from color_handling import apply_color

NO_COMMON_COURSES_FOUND_MESSAGE = "No common courses found."

def get_common_courses(ge_category1_courses, ge_category2_courses, online_only):
    common_courses = set(ge_category1_courses.keys()).intersection(set(ge_category2_courses.keys()))

    common_courses_found = []
    for course_id in common_courses:
        course = ge_category1_courses[course_id]
        meetings = course.get("meetings", [])
        if not online_only or any(meeting.get("building") == "ON LINE" for meeting in meetings):
            common_courses_found.append({
                "id": course_id,
                "title": course["course"]["title"],
                "description": course["course"]["description"],
                "ge_text": course["course"]["ge_text"]
            })

    return common_courses_found

def fetch_courses(year, ge_category, quarter):
    query_variables = {"year": year, "ge": ge_category, "quarter": quarter}
    result = run_query(QUERY_TEMPLATE, query_variables)
    courses = extract_courses_from_result(result)
    return courses

def find_common_courses(year, ge_category1, ge_category2, quarter, online_only=False):
    ge_category1_courses = fetch_courses(year, ge_category1, quarter)
    ge_category2_courses = fetch_courses(year, ge_category2, quarter)

    common_courses = get_common_courses(ge_category1_courses, ge_category2_courses, online_only)

    if common_courses == []:
        return None

    output = format_output(common_courses, ge_category1, ge_category2, quarter)

    return output


def pair_ge_categories(year, ge_pair1, ge_pair2, quarter, online_only=False):
    output1 = find_common_courses(year, ge_pair1[0], ge_pair1[1], quarter, online_only)
    output2 = find_common_courses(year, ge_pair2[0], ge_pair2[1], quarter, online_only)

    if output1 and output2:
        print(output1)
        print(output2)
    else:
        print(apply_color("red", f"\t\t{NO_COMMON_COURSES_FOUND_MESSAGE}"))
