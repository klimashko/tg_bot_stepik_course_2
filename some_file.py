def greet(name: str) -> str:
    return "Hello, " + name
print(greet.__annotations__)
#
#
# result: int = 5
#
# result = 'summer'
#
# print(greet('Yulya'))
#
# print(result)

from typing import Literal
user: dict[Literal['name'] | Literal['second_name'] | Literal['username'], str] = {}

user = {'second_name': 'Anya'}


# class User:
#     def __init__(self, user_id, name, age, email):
#         self.user_id = user_id
#         self.name = name
#         self.age = age
#         self.email = email

from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str
import requests


api_url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
else:
    print(response.status_code)    # При другом коде ответа выводим этот код

api_url_numbers =  'http://numbersapi.com/43/'

response = requests.get(api_url_numbers)

print(response.text if response.status_code == 200 else response.status_code)