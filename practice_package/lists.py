def square_odds(numbers):
    result = []
    for n in numbers:
        if n % 2 != 0:
            result.append(n ** 2)
    return result

def normalize_names(names):
    result = []
    for name in names:
        result.append(name.capitalize())
    return result

def remove_invalid_emails(emails):
    result = []
    for email in emails:
        if email.count('@') == 1 and len(email) >= 5 and not email.startswith('@') and not email.endswith('@'):
            result.append(email)
    return result

def filter_palindromes(words):
    result = []
    for word in words:
        if word.lower() == word.lower()[::-1]:
            result.append(word)
    return result

def calculate_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def find_common_prefix(strings):
    if not strings:
        return ""
    
    prefix = strings[0]
    
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix