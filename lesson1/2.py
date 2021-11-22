a = int(input("Введите кол-во секунд = "))

hour = int(a / 3600)
min = int((a - hour * 3600) / 60)

sec = int(a - (hour * 3600 + (min * 60)))
print('{2}:{1}:{0}'.format(sec, min, hour))
