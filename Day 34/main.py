#Type hint

age: int
name: str
height: float
is_human: bool

def generic_function(variable: int) -> bool:
    pass

generic_function(20)
generic_function("oi")

age = 12
print(age)
age = "twelve"
print(age)


