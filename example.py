from trigramms import Trigramm, CommonTrigramm
date = "10.08.1985"
time = 5.3
my_trigramm = Trigramm(date, time)
my_trigramm.print_info()
my_trigramm.draw_geksogramm()

print("#############")
common_trigramm = CommonTrigramm(1985, 1)
common_trigramm.draw_trigramm()