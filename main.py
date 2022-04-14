import random
import math


def experiment():
    digit = 1
    for _ in range(8):
        digit += random.randint(0, 1)
    return digit


firstCol = []
answers = {}
for i in range(50):
    res = experiment()
    firstCol.append(round(res, 2))
    if res in answers.keys():
        answers[res] += 1
    else:
        answers[res] = 1


srArifm = 0
for k in answers.keys():
    srArifm += answers[k] * k
srArifm /= 50

secondCol = []
for row in firstCol:
    secondCol.append(round(row - srArifm, 2))

thirdCol = []
for row in secondCol:
    thirdCol.append(round(row ** 2, 2))
zeroCol = list(range(1, 51))
#print("Zero Col:", zeroCol)
#print("First Col:", firstCol)
#print("Second Col:", secondCol)
#print("Third Col:", thirdCol)
#print("srArifm:", srArifm)
#print("sumSecond:", sum(secondCol))
srSqrtOtkl = math.sqrt(1 / 49 * sum(thirdCol))
#print("srSqrtOtkl:", srSqrtOtkl)
#print("maxHighHistogram:", 1 / (srSqrtOtkl * math.sqrt(2 * math.pi)))
for i in range(50):
    print(f"{zeroCol[i]} & {firstCol[i]} & {secondCol[i]} & {thirdCol[i]} \ ".strip(), end='')
    print("\ \n\hline")

for i