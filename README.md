# Trigram
Два различных класса с разными методами для построения триграмм .

## Класс CommonTrigramm
Создает триграмму по дате рождения и полу.

##Пример использования:
```python
from trigramms import CommonTrigramm

common_trigramm = CommonTrigramm(1985, 1)
common_trigramm.draw_trigramm()
```
## Класс Trigramm
Создает личную гексограмму по дате и времени рождения. Гексограмма соостоит из 2-х триграмм - верхней и нижней.

## Пример использования
```python
from trigramms import Trigramm
date = "10.08.1985" #Дата рождения в строковом формате dd.mm.yyyy
time = 5.3 #Время рождения, число, в данном примере время рождения между 5 и 6 утра
my_trigramm = Trigramm(date, time)
my_trigramm.print_info() #Выводим информацию о триграммах и гексограмме
my_trigramm.draw_geksogramm() #Рисует личную гексограмму
```
