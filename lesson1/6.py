a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
c = int(a)
result_day = 1
result_km = a
while a < b:
        a = a + 0.1 * a
        result_day = result_day + 1
        result_km = result_km + a
print("Вы достигнете требуемых показателей на %.d день" % result_day)