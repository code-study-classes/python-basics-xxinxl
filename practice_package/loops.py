def sum_even_digits(number):
    number = abs(number)
    
    match number:
        case 0:
            return 0
        
        case _:
            last_digit = number % 10
            rest_sum = sum_even_digits(number // 10)
            
            match last_digit % 2 == 0:
                case True:
                    return rest_sum + last_digit
                case False:
                    return rest_sum
        
def count_vowel_triplets(text):
    text = text.lower()
    
    vowels = "aeiouy"
    
    count = 0
    n = len(text)
    
    for i in range(n - 2):
        match (text[i] in vowels, text[i+1] in vowels, text[i+2] in vowels):
            case (True, True, True):
                count += 1
    
    return count

def find_fibonacci_index(number):
    if number < 1:
        return -1

    a, b = 1, 1
    index = 2 if number > 1 else 1

    match number:
        case 1:
            return 1

    while b < number:
        a, b = b, a + b
        index += 1
        if b == number:
            return index

    return -1


def remove_duplicates(string):
    match string:
        case "":
            return ""
        case _ if len(string) == 1:
            return string
        
    match string[0] == string[1]:
        case True: 
            return remove_duplicates(string[1:])
        case False:
            return string[0] + remove_duplicates(string[1:])