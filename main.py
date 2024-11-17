def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    list_dict = dict_to_list(chars_dict)
    create_report(list_dict, num_words, book_path)
    # print(list_dict)
    

def create_report(list_dict, word_count, path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    for i in range(len(list_dict) - 1):
        if list_dict[i]["key"].isalpha():
            print(f"The {list_dict[i]["key"]} character was found {list_dict[i]["value"]} times")


def dict_to_list(dict):
    list_dict = []
    for key in dict:
        list_dict.append({'key': key, 'value': dict[key]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict


def sort_on(dict):
    return dict["value"]


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
