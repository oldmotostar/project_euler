from helpers import find_number_for_target_proportion


def main():
    target = 0.99
    result = find_number_for_target_proportion(target)
    print(f"The least number with {target * 100:.0f}% bouncy numbers is {result}")


if __name__ == "__main__":
    main()
