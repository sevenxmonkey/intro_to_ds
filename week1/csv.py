import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

ave = sum(float(d['hwy']) for d in mpg) / len(mpg)
print(ave)

sylinders= set(d['cyl'] for d in mpg)
print(sylinders)

CtyMpgByCyl = []

for c in sylinders:
    summpg = 0
    cyltypecount = 0
    for d in mpg:
        if d['cyl'] == c:
            summpg += float(d['cty'])
            cyltypecount += 1
    CtyMpgByCyl.append((c, summpg / cyltypecount))

CtyMpgByCyl.sort(key=lambda x: x[0])
print(CtyMpgByCyl)

vehicleclass = set(d['class'] for d in mpg)
print(vehicleclass)

HwyMpgByClass = []
for t in vehicleclass:
    summpg = 0
    vclasscount = 0
    for d in mpg:
        if d['class'] == t:
            summpg += float(d['hwy'])
            vclasscount += 1
    HwyMpgByClass.append((t, summpg / vclasscount))
HwyMpgByClass.sort(key=lambda x: x[1])
print(HwyMpgByClass)