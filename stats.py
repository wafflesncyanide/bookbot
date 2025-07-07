def get_word_count(file):
    with open(file) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
    return word_count

def get_character_counts(file):
    character = {}
    with open(file) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        for letter in file_contents:
            if letter in character:
                character[letter] += 1
            else:
                character[letter] = 1
    return character

def sort_on(items):
    return items["num"]
 

def listify(dict):
    dict_list = []
    new_dict = {}
    for name in dict:
            new_dict["name"] = name
            new_dict["num"] = dict[name]
            dict_list.append(new_dict)
            new_dict = {}
    return dict_list
