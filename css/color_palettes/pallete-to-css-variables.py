# TAILWIND 4 defines colors in css instead of using tailwind.config.js, all the palletes I generated from coolors, 
# were in the format expected by tailwind 3 and earlier. This script will convert them
import re
import json

def normalize_input(s):
    # Convert single quotes to double quotes
    s = re.sub(r"'", r'"', s)

    # Quote all unquoted keys (including numeric keys like 100:)
    key_pattern = r'(?<=\{|,|\n)\s*([a-zA-Z_][a-zA-Z0-9_-]*|\d+)\s*:'
    s = re.sub(key_pattern, r'"\1":', s)

    return s

def main():
    #print("Enter your color object (end input with an empty line):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    raw_input = "\n".join(lines)
    processed_input = normalize_input(raw_input)

    try:
        color_data = json.loads(processed_input)
    except json.JSONDecodeError as e:
        print(f"Invalid input after processing: {e}")
        return

    css_lines = []

    for color_name, values in color_data.items():
        for key, hex_value in values.items():
            key_str = f"-{key}" if key != "DEFAULT" else ""
            css_lines.append(f"--{color_name}{key_str}: {hex_value};")

    print("\n\n/* Tailwind 4.x*: add to themes.css inside a @theme {}*/")
    for line in css_lines:
        print(line)

if __name__ == "__main__":
    main()
