def word_count(book_text):
    count = book_text.split()
    return len(count)

def converter(book_text):
    dict = {}
    convert = book_text.lower()
    for letter in convert:
        if letter in dict:
            dict[letter] = dict[letter] + 1
        else:
            dict[letter] = 1
    return dict


def sort_on(d):
    return d["num"]

def sorted_dict(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


