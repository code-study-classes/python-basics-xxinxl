def find_common_elements(set1, set2):
    result = set()
    for item in set1:
        if item in set2:
            result.add(item)
    return result

def is_superset(set_a, set_b):
    for item in set_b:
        if item not in set_a:
            return False
    return True

def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

def count_unique_words(text):
    words = text.lower().split()
    unique = set(words)
    return len(unique)

def find_shared_items(*sets):
    if not sets:
        return set()
    
    shared_items = sets[0]
    
    for s in sets[1:]:
        shared_items = {item for item in shared_items if item in s}
    
    return shared_items