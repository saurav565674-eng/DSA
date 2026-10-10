from typing import Union

def calculate(a: int, b: int, op: str) -> Union[int, float, str]:
    if op in ["+","-","*","/","//","%","**"] and b==0:
        return "Division by zero"

    if op == "+":
        return a+b
    elif op =="-":
        return a-b
    elif op=="*":
        return a*b
    elif op == "/":
        return round(a/b,2)
    elif op== "//":
        return a//b
    elif op=="%":
        return a%b
    elif op=="**":
        return a**b
    else :
        return "invalid operation"