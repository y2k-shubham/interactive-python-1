from commons.separator_utils import show_text_with_separator

show_text_with_separator("print numbers")
# Arithmetic expressions - numbers, operators, expressions
print(3, -1, 3.142, -2.81)

show_text_with_separator("number types")
# numbers - two types, an integer or a decimal number
# two corresponding data types int() and float()
print(type(3), type(-1), type(3.142), type(-2.81))
print(type(3.), type(-.3), type(.3))

show_text_with_separator("number type-cast")
# we can convert between data types using int() and float()
# note that int() takes the "whole" part of a decimal number and doesn't round
# float() applied to integers is boring
print(int(3.142), int(-2.81))
print(float(34), float(-79))

show_text_with_separator("floating-point approximation")
# floating point number have around 15 decimal digits of accuracy
# pi is 3.1415926535897932384626433832795028841971...
# square root of two is 1.4142135623730950488016887242096980785696...
# approximation of pi, Python displays 12 decimal digits
print(3.1415926535897932384626433832795028841971)
# appoximation of square root of two, Python displays 12 decimal digits
print(1.4142135623730950488016887242096980785696)

show_text_with_separator("arithmetic operators")
# arithmetic operators
# +		plus		addition
# -		minus		subtraction
# *		times		multiplication
# /		divided by 	division
# **    power		exponentiation
print(1 + 2, 3 - 4, 5 * 6, 2 ** 5)

show_text_with_separator("division in python3")
# Division in Python 3
# If one operand is a decimal (float), the answer is decimal
print(1.0 / 3, 5.0 / 2.0, -7 / 3.0)
# If both operands are ints, the answer is still float
print(1 / 3, 5 / 2, -7 / 3)
# To get integer answer (rounded down), use //
print(1 // 3, 5 // 2, -7 // 3)

show_text_with_separator("expressions")
# expressions - number or a binary operator applied to two expressions
# minus is also a unary operator and can be applied to a single expression
print(1 + 2 * 3, 4.0 - 5.0 / 6.0, 7 * 8 + 9 * 10)

show_text_with_separator("implicit precedence")
# expressions are entered as sequence of numbers and operations
# how are the number and operators grouped to form expressions?
# operator precedence - "please excuse my dear aunt sallie" = (), **, *, /, +,-
print(1 * 2 + 3 * 4)
print(2 + 12)

show_text_with_separator("explicit precedence")
# always manually group using parentheses when in doubt
print(1 * (2 + 3) * 4)
print(1 * 5 * 4)
