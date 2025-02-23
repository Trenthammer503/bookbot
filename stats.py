def count_words(text):
    word_count = 0
    for i in text.split():
        word_count += 1
    return word_count

def character_count(text):
    character_dict = {}
    lowercase_text = text.lower()

    for i in lowercase_text:
        if i == " ":
            pass
        elif i not in character_dict:
            character_dict[i] = 1
        else:
            character_dict[i] += 1
    return character_dict

def sort_on(dict):
    for i in dict:
        return dict[i]

def book_report(char_dict):
    list_of_dicts = []

    for i in char_dict:
        list_of_dicts.append({i: char_dict[i]})

    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts
