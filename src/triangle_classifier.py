# src/triangle_classifier.py

import sys


def classify_triangle(sides):
    try:
        words = sides.strip().split()

        if not words:
            return "Error: No input provided"

        if words[0].lower() in ["exit", "quit"]:
            sys.exit("Application exited by user.")

        if len(words) != 3:
            missing = 3 - len(words)
            if missing == 1:
                return "Error: One side missing"
            elif missing == 2:
                return "Error: Two sides missing"
            else:
                return "Error: Invalid number of sides"

        try:
            a, b, c = map(float, words)
        except ValueError:
            return "Error: Invalid input"

        if a <= 0 or b <= 0 or c <= 0:
            return "Error: Invalid sides"

        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        elif a + b > c and a + c > b and b + c > a:
            return "Scalene"
        else:
            return "NoTriangle"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    for line in sys.stdin:
        result = classify_triangle(line)
        if result in ["Equilateral", "Isosceles", "Scalene", "NoTriangle"]:
            print(result)
        elif "Application exited" in result:
            print(result)
            break
        else:
            print(result, file=sys.stderr)


if __name__ == "__main__":
    main()
