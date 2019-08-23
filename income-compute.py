import math

income = 30000
rateNumb = 5
incomeRate=[]


incomeRate.append({
    'name': '养老金:        ',
    'value':0.08
})

incomeRate.append({
    'name': '医疗金:        ',
    'value':0.02
})

incomeRate.append({
    'name': '失业金:        ',
    'value':0.005
})

incomeRate.append({
    'name': '公积金:        ',
    'value':0.12
})

# incomeRate.append({
#     'name': '所得税:        ',
#     'value': 0.16
# })

antiTax = 0

for item in incomeRate:
    curMoney = income * item['value'];
    antiTax += curMoney
    print("%s %d" % (item['name'], math.ceil(curMoney)))

supportParents = 1000
houseLoan = 1000

antiTax += supportParents
antiTax += houseLoan

maxIncome = 10000000000
taxRateList = [[0, 3000, 0.03, 0], \
             [3000, 12000, 0.1, 210], \
             [12000, 25000, 0.20, 1410], \
             [25000, 35000, 0.25, 2660], \
             [35000, 55000, 0.30, 4410], \
             [55000, 80000, 0.35, 7160], \
             [80000, maxIncome, 0.45, 15160]]

afterInsurance = income - antiTax
tax = 0

print("交税部分:     %d" % afterInsurance)

for item in taxRateList:
    if afterInsurance > item[0] and afterInsurance <= item[1]:
        tax = afterInsurance * item[2] - item[3]
        break

print ("税款:       %d" % tax)

incomeLeft = afterInsurance - tax + supportParents + houseLoan
print ("到手收入:   %d" % incomeLeft)
