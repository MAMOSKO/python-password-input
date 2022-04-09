
# Python Password Input

### AÇIKLAMA/DESCRIPTION
**TR**
Python için hazırlanmış bir şifre girişi.
Kullanımı "input()" işleviyle aynıdır, ancak "input" ve "getpass"tan farkı, karakter yerine * yazdırmasıdır.

**EN**
A password input prepared for Python.
Its usage is the same as the "input()" function, but the difference from "input" and "getpass" is that it prints * instead of characters.

![GIF](https://i.hizliresim.com/crll8ua.gif)

### KULLANIM/USE
**TR**
Modül içer aktarılır ve modüle ait olan `passwordInput` komutu herhangi bir değişkene return edilir. Kullanıcı şifreyi girdiğinde değişken şifrenin değerine sahip olacaktır.
**EN**
The module is imported and the `passwordInput` command belonging to the module is returned to any variable. When the user enters the password, the variable will have the value of the password.

### ÖRNEKLER/EXAMPLES
```python
import passwordInput
password=passwordInput.passwordInput("Enter Your Password: ")
print("Password is "+password)
```
```python
from passwordInput import passwordInput
uname=input("User Name: ")
password=passwordInput("Password: ")
if uname=="python" and password=="best":
	print("Welcome Back!")
else:
	print("ERROR")
```

## GELİŞTİREN/AUTHOR
**Muhammed KARAMAN-MAMOSKO-**
Web Site: [www.mamosko.ml](https://mamosko.ml)<br>
Mail: [admin@mamosko.ml](mailto:admin@mamosko.ml)<br>
Instagram: [mhmdkrmn1](https://instagram.com/mhmdkrmn1)<br>
GitHub: [MAMSOKO](https://github.com/MAMOSKO)
