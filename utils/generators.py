import random
import string

def generate_email():
    first_name = "Yaroslav"
    last_name = "Melnikov"
    cohort = "22"
    digits = "".join(random.choices(string.digits, k=3))
    domain = "yandex.ru"
    return f"{first_name}_{last_name}_{cohort}_{digits}@{domain}"

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
