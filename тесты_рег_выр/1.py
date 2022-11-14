# Импортируем библиотеки
import getpass
import re
pattern_password =r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
# Используем getpass вместо стандартной функции ввода
# Это позволит скрыть запись как в реальной жизни
user_input = "abcABC@1234"
invalid_pass_text = \
"Ваш пароль должен содержать не менее 8 символов, \
по крайней мере одну заглавную букву, \
строчную букву, цифру и специальный символ, чтобы быть безопасным."
if (re.search(pattern_password, user_input)):
    print("Strong Password Set")
else:
    print(f"Данный пароль не подходит: {user_input}.", f"{invalid_pass_text}", sep='\n')

