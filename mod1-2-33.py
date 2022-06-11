while True:
	password=input("Введите пароль:")
	print()
	pASSWORD=password
	password1=password.lower()
	password2=password.upper()
	print(pASSWORD)
	print(password1)
	print(password2)

	print(len(password),"\n")

	if len(password)<=8:
		print("Пароль не подходит.")

	elif pASSWORD==password2:
		print("Пароль не подходит.")

	elif pASSWORD==password1:
		print("Пароль не подходит.")
	else:
		break

		

	
print("Пароль принят!")

input("\nВведите enter")