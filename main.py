def main():
    print("Enter name of the file you want to read from")
    filename = input()
    print("Enter keyword you want to search for")
    keyword = input()
    filter_file_by_keyword(filename, keyword)


def filter_file_by_keyword(input_file, keyword):
    print("Filtering file by keyword: " + keyword + " from file: " + input_file)


if __name__ == "__main__":
    main()