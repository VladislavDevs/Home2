boysString = input("Введите список мужчин через запятую: ")
girlsString = input("Введите список женщин через запятую: ")
boysList = boysString.split()
girlsList = girlsString.split()

if((len(boysString) == 0 or len(girlsString) == 0) or (len(boysList) != len(girlsList))):
    print("Знакомство не возможно! В списках есть люди которые останутся без пары.")
else:
    for boy, girl in zip(sorted(boysList), sorted(girlsList)):
        print(f"{boy} и {girl}")