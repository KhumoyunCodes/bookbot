def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def count_symbols(text):
    symbols = {}
    for symbol in text:
        symbol = symbol.lower()
        if symbol in symbols:
            symbols[symbol] +=1
        else:
            symbols[symbol] = 1
    return symbols
        

def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

