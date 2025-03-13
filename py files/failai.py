


# 1. Susikurkite vieną keletą failų, pamėginkite juos nuskaityti taikant įvairas
# metodikas (viską vienu metu, po atskirą eilutę, sudedant į dictionary, ir
# pan.)

# open('failas.txt')
# with open('C:/Users/vytau/Desktop/VCS/Python/tekstas.txt', encoding = 'utf-8') as failas:
# nt = failas.read()
# nt = failasreadline.()
# nt = failas.readlines()
# nt = failas.read()
# print('NORIMAS:', nt)
# kt = failas.read()
# print('KITAS', kt)
# print('NUSKAITYTAS', nt)
# failas.seek(30)
# per_nauja_teksas = failas.read()
# print('PER NAUJA nuo 30tos vietos:', per_nauja_teksas)
# print('nuskaitytas teksas:', failas.read())
# print(nt)
# with open('C:/Users/vytau/Desktop/VCS/Python/tekstas.txt') as failas:
#     tekstas = failas.read()
#     print(tekstas)
# with open('C:/Users/vytau/Desktop/VCS/Python/tekstas.txt', encoding = 'utf-8-sig') as failas:
#     VT = failas.readlines()
#     print('VT:', VT)
#     sutvarkytas_tekstas = [eilute.rstrip('\n') for eilute in VT]
#     print('SUTVARKYTAS TEKSTAS:', sutvarkytas_tekstas)

eilutes = []

with open('C:/Users/vytau/Desktop/VCS/Python/uz2.txt', encoding = 'utf-8-sig') as failas:
    # cars = failas.read()
    # print('cars:', cars)
    for eilute in failas:
        eilute = eilute.rstrip('\n')
        print('eilute:', eilute)
        eilutes.append(eilute)
print(eilute)

cars = []
with open('C:/Users/vytau/Desktop/VCS/Python/uz2.txt', encoding = 'utf-8-sig') as failas:
    for eilute in failas:
        eilute = eilute.rstrip('\n')
        isskaidyta = eilute.split(';')
        car = dict(
            make=isskaidyta[0],
            model=isskaidyta[1],
            year=isskaidyta[2],
            engine=isskaidyta[3],
        )
        cars.append(car)
print(cars)

