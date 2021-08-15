import random
password_length = int(input("Enter your preferred length of password: "))
T="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(T,password_length))
print(password)
