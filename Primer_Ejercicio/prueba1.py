import random
import string as s

elements = s.ascii_letters+s.digits+s.punctuation

size = int(input("¿Qué tan grande deseas que sea la contraseña? "))
password = ""

for i in range(size):
    password += random.choice
print(password)