from lib.ChineseDate.dates import ChineseDate, GregDate

class CommonTrigramm:
    trigramm_names = ['Цянь (небо)', 'Дуй (Водоем)', 'Ли (Огонь)', 'Чжэнь (Гром)', 'Сюнь (Ветер)', 'Кань (Вода)', 'Гэнь (Гора)', 'Кунь (Земля)']
    
    def predict(self, num, sex):
        if sex == 0:
            if num == 0 or num == 6:
                return 7
            elif num == 1:
                return 5
            elif num == 2:
                return 2
            elif num == 3:
                return 6
            elif num == 4:
                return 1
            elif num == 5:
                return 0
            elif num == 7:
                return 4
            else:
                return 3
        elif sex == 1:
            if num == 0 :
                return 4
            elif num == 1 or num == 4:
                return 6
            elif num == 2:
                return 0
            elif num == 3:
                return 1
            elif num == 5:
                return 2
            elif num == 6:
                return 5
            elif num == 7:
                return 7
            else:
                return 3

    def __init__(self, year, sex):
        self.number = self.predict(year % 9, sex)

    def get_trigramm(self, number):
        bin_str = bin(number)[2:]
        i = len(bin_str)
        while i < 3:
            bin_str = "0" + bin_str
            i += 1
        return bin_str
        

    def draw_trigramm(self):
        bin_str = self.get_trigramm(self.number)
        for i in reversed(range(3)):
            if bin_str[i] == '0':
                print("_____")
            else:
                print("__ __")

  


class Trigramm:

    l = [7, 5, 6, 3, 2, 1, 0, 4]
    trigramm_names = ['Цянь (небо)', 'Дуй (Водоем)', 'Ли (Огонь)', 'Чжэнь (Гром)', 'Сюнь (Ветер)', 'Кань (Вода)', 'Гэнь (Гора)', 'Кунь (Земля)']
    numbers =  [[1, 43, 14, 34, 9, 5, 26, 11],
                [10, 58, 38, 54, 61, 60, 41, 19],
                [13, 49, 30, 55, 37, 63, 22, 36], 
                [25, 17, 21, 51, 42, 3, 27, 24],
                [44, 28, 50, 32, 57, 48, 18, 46], 
                [6, 47, 64, 40, 59, 29, 4, 7],
                [33, 31, 56, 62, 53, 39, 52, 15],
                [12, 45, 35, 16, 20, 8, 29, 2]]

    def __init__(self, date_str, time):
        chinese_date = ChineseDate(GregDate(date_str))
        guards_number = int(((time + 1) / 2) % 12 + 1)
        self.first_number = (chinese_date.year_branch + chinese_date.month + chinese_date.day + guards_number) % 8
        self.second_number = (chinese_date.year_branch + chinese_date.month + chinese_date.day) % 8
        

    def print_info(self):
        print("Нижнее число:", self.first_number)
        print("Нижняя триграмма:", self.trigramm_names[self.l[self.first_number - 1]])
        print("Верхнее число:", self.second_number)
        print("Верхняя триграмма:",  self.trigramm_names[self.l[self.second_number - 1]])
        print("Гексаграмма:", self.numbers[self.l[self.first_number - 1]][self.l[self.second_number - 1]])

    def get_trigramm(self, number):
        num = self.l[number - 1]
        bin_str = bin(num)[2:]
        i = len(bin_str)
        while i < 3:
            bin_str = "0" + bin_str
            i += 1
        return bin_str
        

    def draw_trigramm(self, bin_str):
        for i in reversed(range(3)):
            if bin_str[i] == '0':
                print("_____")
            else:
                print("__ __")

    def draw_geksogramm(self):
        self.draw_trigramm(self.get_trigramm(self.second_number))
        self.draw_trigramm(self.get_trigramm(self.first_number))

