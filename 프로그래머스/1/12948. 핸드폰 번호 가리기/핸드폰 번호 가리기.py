import re

def solution(phone_number):
    return re.sub(r'.(?=.{4})', '*', phone_number)