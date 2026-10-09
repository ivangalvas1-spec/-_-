import random
import string
print('Привет! Я генератор паролей. Давай сгенерируем тебе надежный пароль.')
l = input("Введите длину пароля: ")
alf= string.ascii_letters + string.digits

def p(l):
    return ''.join(random.choices(alf,k=l))

while not l.isdigit() or int(l)<=0:
    if not l.isdigit():
        print('Длина не может содержать буквы и другие символы')
        l=input("Введите длину пароля: ")
    elif int(l)<=0:
        print("Введенное Вами число должно быть натуральным")
        l=input("Введите длину пароля: ")
        
l=int(l)
print(p(l))
