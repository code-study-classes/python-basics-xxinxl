def count_char_occurrences(text):
    filtered_text = [char.lower() for char in text if char.isalpha()]
    
    char_count = {}
    
    for char in filtered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count

def merge_dicts(dict1, dict2, conflict_resolver):
    merged = dict1.copy()
    
    for key, value in dict2.items():
        if key in merged:
            merged[key] = conflict_resolver(key, merged[key], value)
        else:
            merged[key] = value
            
    return merged

def invert_dictionary(original_dict):
    inverted_dict = {}
    
    for key, value in original_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    
    return inverted_dict

def dict_to_table(data_dict, columns):
    pass

def deep_update(base_dict, update_dict):
    pass