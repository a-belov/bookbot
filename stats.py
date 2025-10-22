def get_num_words(text):
    words = text.split()
    return len(words)


def get_characters_count(text):
    count_dict = dict()
    for c in text.lower():
        count_dict.setdefault(c, 0)
        count_dict[c] += 1 
    return count_dict


def dictionary_sort(count_dict):
    def sort_on(items):
        return items["num"]

    list_of_dicts = list()

    for k, v in count_dict.items():
        list_of_dicts.append({"name": k, "num": v})

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts