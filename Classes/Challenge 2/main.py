from password import Password

password1 = Password("low")
password2 = Password("mid")
password3 = Password("high")

print(password1.random_password())
print(password2.random_password())
print(password3.random_password())