def count_words(text: str):
    return len(text.split())

def parse_text_file(file_path: str):
    with open(file_path) as f:
        return f.read()

def count_characters(text: str):
    character_count = {}

    for char in text:
        lower_case_char = char.lower()
        if(not lower_case_char.isalpha()):
            continue

        if(lower_case_char in character_count):
            character_count[lower_case_char] += 1
        else:
            character_count[lower_case_char] = 1
    return character_count

def get_report(file_path: str):
    file_contents = parse_text_file(file_path)

    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(file_contents)} words found in the document\n")

    character_count = count_characters(file_contents)
    sorted_character_count = {k:v for k,v in sorted(character_count.items(), key=lambda item:item[1], reverse=True)}

    for char, count in sorted_character_count.items():
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

def main():
    get_report("books/frankenstein.txt")


main()