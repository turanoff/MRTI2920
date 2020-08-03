import datetime

hours_declension = {
                    'первого': (1, 13), "второго": (2, 14), "третьего": (3, 15),
                    "четвертого": (4, 16), "пятого": (5, 17), "шестого": (6, 18),
                    "седьмого": (7, 19), "восьмого": (8, 20), "девятого": (9, 21),
                    "десятого": (10, 22), "одиннадцатого": (11, 23), "двенадцатого": (12, 24),
                    }

single_hours = {
                'час': (1, 13), "два": (2, 14), "три": (3, 15),
                "четыре": (4, 16), "пять": (5, 17), "шесть": (6, 18),
                "семь": (7, 19), "восемь": (8, 20), "девять": (9, 21),
                "десять": (10, 22), "одиннадцать": (11, 23), "двенадцать": (12, 24),
                }

abc_minutes = {
               1: 'одна', 2: 'две', 3: 'три', 4: 'четере', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
               11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шеснадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать',
               21: 'двадцать одна', 22:'двадцать две', 23: 'двадцать три', 24: 'двадцать четыре', 25: 'двадцать пять', 26: 'двадцать шесть', 27: 'двадцать семь', 28: 'двадцать восемь', 29: 'двадцать девять', 30:'тридцать',
               31: 'тридцать одна', 32: 'тридцать две', 33: 'тридцать три', 34: 'тридцать четыре', 35: 'тридцать пять', 36: 'тридцать шесть', 37: 'тридцать семь', 38: 'тридцать восемь', 39: 'тридцать девять', 40: 'сорок',
               41: 'сорок одна', 42: 'сорок две', 43: 'сорок три', 44: 'сорок четыре', 45: 'сорок пять', 46: 'сорок шесть', 47: 'сорок семь', 48: 'сорок восемь', 49: 'сорок девять', 50: 'пятьдесят',
               51: 'пятьдесят одна', 52: 'пятьдесят две', 53: 'пятьдесят три', 54: 'пятьдесят четыре', 55: 'пятьдесят пять', 56: 'пятьдесят шесть', 57: 'пятьдесят семь', 58: 'пятьдесят восемь', 59: 'пятьдесят девять',
               }

abc_minutes_declension = {
                          1: 'минуты', 2: 'двух', 3: 'трех', 4: 'четырех', 5: 'пяти', 6: 'шести', 7: 'семи', 8: 'восьми', 9: 'девяти', 10: 'десяти',
                          11: 'одиннадцати', 12: 'двенадцати', 13: 'тренадцати', 14: 'четырнадцати', 15: 'четверти', 16: 'шестнадцати', 17: 'семнадцати', 18: 'восемнадцати', 19: 'девятнадцати', 20: 'двадцати',
                          21: 'двадцати одной', 22: 'двадцати двух', 23: 'двадцати трех', 24: 'двадцати четырех', 25: 'двадцати пяти', 26: 'двадцати шести', 27: 'двадцати семи', 28: 'двадцати восьми', 29: 'двадцати девяти',
                         }

tmp = (
        (1, 21),
        (2, 3, 4, 22, 23, 24),
        (2, 3, 4, 22, 23, 24),
        (25, 26, 27, 28, 29),
        (21, 31),
      )

q = int(input('enter "1" if you want to know the current time; "2" to set your own: \n'))
if q == 1:
    now = datetime.datetime.now()
    hour = now.hour
    minutes = now.minute
elif q == 2:
    now = input('enter enter the time as "hh:mm": \n').split(":")
    hour = int(now[0])
    minutes = int(now[1])

real_hour = [k for k, v in hours_declension.items() if hour + 1 in v]
real_hour = "".join(real_hour)

ident_hour = [k for k, v in single_hours.items() if hour + 1 in v]
ident_hour = "".join(ident_hour)

real_minutes = [v for k, v in abc_minutes.items() if minutes == k]
real_minutes = "".join(real_minutes)

if minutes <= 30:
    if minutes == 0:
        if hour in tmp[0]:
            print(f"{hour} час ровно")
        elif hour in tmp[1]:
            print(f"{hour} часа ровно")
        else:
            print(f"{hour} часов ровно")
    elif minutes in tmp[2]:
        print(f'{real_minutes} минуты {real_hour}')
    elif minutes <= 20 or minutes in tmp[3]:
        print(f"{real_minutes} минут {real_hour}")
    elif minutes in tmp[4]:
        print(f"{real_minutes} минута {real_hour}")
    elif minutes == 30:
        print(f'половина {real_hour}')
else:
    print(f"без {abc_minutes_declension[60 - minutes]} минут {ident_hour}")
#