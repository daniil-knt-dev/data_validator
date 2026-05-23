def validate_string(value, min_len=3, max_len=20, contains=None):
    if type(value) != str:
        return False
    if not min_len <= len(value) <= max_len:
        return False
    if contains != None and len(set(value).intersection(contains)) != len(contains):
        return False
    return True


def validate_int(value, min_val=1):
    if type(value) != int:
        return False
    if value < min_val:
        return False
    return True


def validate_data(data, rules):
    res = {}
    for el in data:
        if rules[el]["type"] == "string":
            res[el] = validate_string(data[el], min_len=rules[el]["min_len"],
                                      max_len=rules[el]["max_len"], contains=rules[el]["contains"])
        elif rules[el]["type"] == "int":
            res[el] = validate_int(data[el], rules[el]["min_val"])
    return res


def set_filters():
    print("Фильтры для имени пользователя")
    username_min_len = int(
        input("Введите минимальную длину имени пользователя: ").strip())
    username_max_len = int(
        input("Введите максимальную длину имени пользователя: ").strip())
    username_contains = [x for x in input(
        "Введите через пробел символы, которые должны содержаться в имени пользователя: ").strip().split()]
    print("Фильтры для email")
    email_min_len = int(input("Введите минимальную длину email: ").strip())
    email_max_len = int(input("Введите максимальную длину email: ").strip())
    email_contains = [x for x in input(
        "Введите через пробел символы, которые должны содержаться в email: ").strip().split()]
    print("Фильтры для пароля")
    password_min_len = int(input("Введите минимальную длину пароля: ").strip())
    password_max_len = int(
        input("Введите максимальную длину пароля: ").strip())
    password_contains = [x for x in input(
        "Введите через пробел символы, которые должны содержаться в пароле: ").strip().split()]

    rules = {
        "username":
        {
            "type": "string",
            "min_len": username_min_len,
            "max_len": username_max_len,
            "contains": username_contains
        },
        "email":
        {
            "type": "string",
            "min_len": email_min_len,
            "max_len": email_max_len,
            "contains": email_contains
        },
        "password":
        {
            "type": "string",
            "min_len": password_min_len,
            "max_len": password_max_len,
            "contains": password_contains
        }
    }
    return rules


rules = set_filters()

username = input("👤Введите имя пользователя: ").strip()
email = input("📫Введите email: ").strip()
password = input("🔒Введите пароль: ").strip()

data = {
    "username": username,
    "email": email,
    "password": password
}

res = validate_data(data, rules)
print(res)

input("Enter для выхода")