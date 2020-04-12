f = open("data.csv", "r")

def parsing_tables(f):
	'''Представим нашу таблицу в виде словаря списков.'''
	#Шапку таблицы представим в виде ключей словаря:
	mydict = {}
	line = f.readline()
	k = 0
	word = ""
	while k < (len(line)-1):
		if line[k] != ",":
			word += line[k]
		else:
			mydict[word] = []
			word = ""
		k += 1
	mydict[word] = []
	
	#Столбцы таблицы представим в виде списков - значений для каждого ключа нашего словаря:
	word = ""
	key_number = 1
	for char in f.read():
		if (char == ",") or (char == "\n"):
			if key_number == 1:
				mydict["timestamp"].append(word)
			elif key_number == 2:
				mydict["msisdn_origin"].append(word)
			elif key_number == 3:
				mydict["msisdn_dest"].append(word)
			elif key_number == 4:
				mydict["call_duration"].append(word)
			else:
				mydict["sms_number"].append(word)
			word = ""
			if key_number < 5:
				key_number += 1
			else:
				key_number = 1
		else:
			word += char
	return mydict

def tariffication_t(mydict, phone_number, k_ti, k_tv):
	'''Тарификация услуг Тлефония'''
	cost_t = 0
	for number in mydict["msisdn_origin"]:
		if number  == phone_number:
			cost_t += float(mydict["call_duration"][mydict["msisdn_origin"].index(number)]) * k_ti

	for number in mydict["msisdn_dest"]:
		if number  == "915642913":
			cost_t += float(mydict["call_duration"][mydict["msisdn_dest"].index(number)]) * k_tv

	return cost_t

def tariffication_s(mydict, phone_number, k_s, free_cost):
	'''Тарификация услуг СМС'''
	cost_s = 0
	for number in mydict["msisdn_origin"]:
		if number == phone_number:
			cost_s += float(mydict["sms_number"][mydict["msisdn_origin"].index(number)]) * k_s

	return cost_s - free_cost

#Коэффициент для исходящих звонков
k_ti = 1
#Коэффициент для входящих звонков
k_tv = 1
#Коэффициент для смс
k_s = 1
#Количество бесплатных смс
free_cost = 5
#Номер телефона
phone_number = "915642913"
mydict = parsing_tables(f)
cost_t = tariffication_t(mydict, phone_number, k_ti, k_tv)
cost_s = tariffication_s(mydict, phone_number, k_s, free_cost)
print("\n\tИтоговая стоимость всех звонков абонента: ", cost_t, " рублей.")
print("\tИтоговая стоимость всех смс абонента: ", cost_s, " рублей.\n")

f.close()