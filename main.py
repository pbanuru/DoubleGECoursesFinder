from color_handling import apply_color
from course_handling import pair_ge_categories, find_common_courses


def main():
    year = 2022
    quarter = "SUMMER1"
    online_filter = True

    # Say you need 4 more GE credits to graduate, including 1 GE-7, 1 GE-8 credit, 1 GE-2, and 1 GE-3 credit
    # You want to see if you can satisfy all 4 of these requirements in just two courses.
    # Input all possible combinations you want to search for, and the program will tell you if it can find any.
    # Ex. The first entry to ge_pairs is (("GE-7", "GE-4"), ("GE-8", "GE-2")), which means you want to find a course that satisfies both GE-7 and GE-4, and another course that satisfies both GE-8 and GE-2.
    # ge_pairs = [
    #     (("GE-7", "GE-4"), ("GE-8", "GE-2")),
    #     (("GE-7", "GE-2"), ("GE-8", "GE-4")),
    #     (("GE-7", "GE-4"), ("GE-8", "GE-3")),
    #     (("GE-7", "GE-3"), ("GE-8", "GE-4"))
    # ]

    # for option_index, option in enumerate(ge_pairs):
    #     option_num = option_index // 2 + 1
    #     variation_num = option_index % 2 + 1
    #     print(apply_color("white", f"OP{option_num} Variation {variation_num}"))
    #     pair_ge_categories(year, option[0], option[1], quarter, online_filter)

    # Alternatively, if you just want to search for single courses that satisfy two specified GE requirements, 
    # you can just use find_common_courses(), and print the result, selecting the two GEs you want to satisfy as parameters.
    print(find_common_courses(year, "GE-7", "GE-3", quarter, online_filter))

if __name__ == "__main__":
    main()



