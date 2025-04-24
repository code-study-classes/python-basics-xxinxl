extract_file_name = lambda path: path.replace('/').split('/')[-1].split('.')[0]

def encrypt_sentence(data):
    even_chars = [data[i] for i in range(len(data)) if i % 2 == 1]
    
    odd_chars = [data[i] for i in range(len(data)) if i % 2 == 0][::-1]
    
    return ''.join(even_chars + odd_chars)

def check_brackets(expression):
    arr = []
    for i, char in enumerate(expression):
        if char == '(':
            arr.append(i)
        elif char == ')':
            if arr: 
                arr.pop()
            else:
                return i + 1
            
    if arr:
        return -1
    else:
        return 0

def reverse_domain(str):
    parts = str.split('.')
    reversed_parts = parts[::-1]
    result = '.'.join(reversed_parts)
    return result

def count_vowel_groups(word):
    vowels = 'aeiouy'
    word = word.lower()
    count = 0
    in_group = False

    for letter in word:
        if letter in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False

    return count