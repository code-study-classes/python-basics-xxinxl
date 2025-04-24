# T - функция не должна использовать ванильные условные конструкции, вместо этого: switch-case, match-case, тернарный оператор, словарь и т.д.
def is_weekend(day):
    match day:
        case 6 | 7:
            return True
        case _:
            return False

def get_discount(amount):
    match True:
        case _ if amount >= 5000:
            return round(amount * 0.1, 2)
        case _ if amount >= 1000:
            return round(amount * 0.05, 2)
        case _:
            return 0

def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    
    match len(str(n)):
        case 1:
            digit_word = "однозначное"
        case 2:
            digit_word = "двузначное"
        case 3:
            digit_word = "трехзначное"
        case _:
            digit_word = "неизвестность"
    
    return f"{parity} {digit_word} число"

def convert_to_meters(unitNumber, lengthInUnits):
    match unitNumber:
        case 1:
            factor = 0.1
        case 2:
            factor = 1000
        case 3:
            factor = 1
        case 4:
            factor = 0.001
        case 5:
            factor = 0.01
        case _:
            factor = 0 
    
    return lengthInUnits * factor

def describe_age(age):
    tens = age // 10
    ones = age % 10

    match tens:
        case 2: tens_word = "двадцать"
        case 3: tens_word = "тридцать"
        case 4: tens_word = "сорок"
        case 5: tens_word = "пятьдесят"
        case 6: tens_word = "шестьдесят"
        case 7: tens_word = "семьдесят"
        case 8: tens_word = "восемьдесят"
        case 9: tens_word = "девяносто"
        case 10: return "сто лет"
        case _: tens_word = ""

    match ones:
        case 1: ones_word = "один"
        case 2: ones_word = "два"
        case 3: ones_word = "три"
        case 4: ones_word = "четыре"
        case 5: ones_word = "пять"
        case 6: ones_word = "шесть"
        case 7: ones_word = "семь"
        case 8: ones_word = "восемь"
        case 9: ones_word = "девять"
        case 0: ones_word = ""
        case _: ones_word = ""

    num_word = f"{tens_word} {ones_word}".strip()

    # Определяем склонение
    if 11 <= age % 100 <= 14:
        suffix = "лет"
    else:
        match ones:
            case 1: suffix = "год"
            case 2 | 3 | 4: suffix = "года"
            case _: suffix = "лет"

    return f"{num_word} {suffix}"