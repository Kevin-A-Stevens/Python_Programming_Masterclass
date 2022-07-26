"""
Working with binary files

bytes and bytearray

"""
# equation = bytes((207, 128, 114, 194, 178))
equation = b'\xcf\x80r\xc2\xb2'
print(equation)  # b'\xcf\x80r\xc2\xb2'
print(type(equation))  # <class 'bytes'>
print(len(equation))  # 5

for b in equation:
    print(b, end=', ')
print()

print(equation.decode('utf-8'))  # πr²

