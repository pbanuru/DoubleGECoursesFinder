from color_handling import apply_color
from course_handling import pair_ge_categories


def main():
    year = 2022
    quarter = "SUMMER1"
    online_filter = True

    ge_pairs = [
        # (("GE-7", "GE-4"), ("GE-8", "GE-2")),
        # (("GE-7", "GE-2"), ("GE-8", "GE-4")),
        # (("GE-7", "GE-4"), ("GE-8", "GE-3")),
        (("GE-7", "GE-3"), ("GE-8", "GE-4"))
    ]
    chosen = ["GE-2", "GE-3"]

    for option_index, option in enumerate(ge_pairs):
        option_num = option_index // 2 + 1
        variation_num = option_index % 2 + 1
        print(apply_color("white", f"OP{option_num} Variation {variation_num} - {chosen[option_num-1]}"))

        pair_ge_categories(year, option[0], option[1], quarter, online_filter)
        

if __name__ == "__main__":
    main()



