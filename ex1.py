import matplotlib.pyplot as plt

input_file = open("выгрузка.csv", "r")

param = []
X = []
Y = []
FT = []
for line in input_file:
    param.append(line)

names = []
l = []

for name in param[0].split(","):
    names.append(name)

for i in range(0, 31):
    l.append(i)

d = dict(zip(names, l))  # заполняет по имени столбца список значений

nx = input('Enter param 1 ').upper()
ny = input("Enter param 2 ").upper()
first = d[nx]
second = d[ny]

for line in param[1:]:
    line = line.split(",")
    X.append(line[first])
    Y.append(line[second])
    FT.append(line[30])
Colors = {'G\n': 'green', 'F\n': 'red', 'U\n': 'grey'}

xlist = []
ylist = []
Xaxis = sorted(set(X))
Yaxis = sorted(set(Y))
for index, xx in enumerate(Xaxis):
    xlist.append((xx, index))
for index, yy in enumerate(Yaxis):
    ylist.append((yy, index))
Xaxis.clear()
Yaxis.clear()
Xaxis = dict(xlist)
Yaxis = dict(ylist)


def picture(x, y, z):
    plt.figure()
    plt.xlabel(nx)
    plt.ylabel(ny)
    plt.scatter(x, y, color=z)
    plt.show()
    return


xlist.clear()
ylist.clear()

zlist = []
for (x, y, z) in zip(X, Y, FT):
    xlist.append(Xaxis[x])
    ylist.append(Yaxis[y])
    zlist.append(Colors[z])
picture(xlist, ylist, zlist)
