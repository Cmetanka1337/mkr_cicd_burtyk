import os


def main():
    print("Enter name of the file you want to read from (only with .txt extension)\nExample: unfiltered\nDo not add extension in the end")
    filename = input().strip() + ".txt"
    print("Enter keyword you want to search for\n")
    keyword = input()
    filter_file_by_keyword(filename, keyword)


def filter_file_by_keyword(input_file, keyword, output_dir=os.path.dirname(__file__)):
    try:
        filtered_lines = []
        with open(input_file, "r") as file:
            for line in file:
                if keyword in line:
                    filtered_lines.append(line)

        output_file_path = os.path.join(output_dir, 'filtered.txt')
        with open(output_file_path, "w") as output_file:
            output_file.writelines(filtered_lines)

        if len(filtered_lines) == 0:
            print("No matching lines found")
        else:
            print(f"Lines containing keyword {filtered_lines}:")
            print(f"Filtered lines written to 'filtered.txt' in {output_dir}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()