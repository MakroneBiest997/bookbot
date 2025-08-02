

def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count



def count_each_character(text):

    lower_case_text = text.lower()
    character_list = list(lower_case_text)
    character_dic = {}
    
    for character in character_list:
        if character not in character_dic:
            character_dic[character] = 1
        elif character in character_dic:
             character_dic[character] += 1
    return character_dic

def unsorted_dictionary_list(dictonary):
    dic_list = []
    for key, value in dictonary.items():
        list_value = {"char" : key , "num" : value}
        dic_list.append(list_value)
    return dic_list

def get_sort_key(dictionary):
    return dictionary["num"]