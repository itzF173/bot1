import pandas as pd
from pandas import pandas

pn = pandas
#
# data = {
#     "Имя": ["Iliya","Mark","Dmitriy"],
#     "Возраст": [14,13,12],
#     "Город": ["Moskow","Piter","Tula"]
# }
#
# db = pn.DataFrame(data)
#
# game = pn.read_excel("dvz_xls.xls")
#
#
# print(db)
# print(data)
#
# print(game.head(40))

tabl = pd.read_excel("Book 2 (1).xlsx")
print(tabl[tabl["День"] == "ПН"])
