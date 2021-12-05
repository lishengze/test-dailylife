import math

income = 18333
subsidy = 1300
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

houseLimit ={
    "0.05":2464,
    "0.06":2956,
    "0.07":3448
}

sumInsurance = 0
for item in incomeRate:
    curMoney = income * item['value'];

    if item['name'] == '公积金':
        if str(item['value']) in houseLimit and curMoney > houseLimit[str(item['value'])] / 2:
            curMoney = houseLimit[str(item['value'])] / 2

    sumInsurance += curMoney
    print("%s %d" % (item['name'], math.ceil(curMoney)))

supportParents = 1000
houseLoan = 0
basicMoney = 5000

maxIncome = 10000000000
taxRateList = [[0, 3000, 0.03, 0], \
               [3000, 12000, 0.1, 210], \
               [12000, 25000, 0.20, 1410], \
               [25000, 35000, 0.25, 2660], \
               [35000, 55000, 0.30, 4410], \
               [55000, 80000, 0.35, 7160], \
               [80000, maxIncome, 0.45, 15160]]

moneyForTax = income - sumInsurance - supportParents - houseLoan - basicMoney
tax = 0

print("交税部分:       %d" % moneyForTax)

for item in taxRateList:
    if moneyForTax > item[0] and moneyForTax <= item[1]:
        tax = moneyForTax * item[2] - item[3]
        break

print ("税款:           %d" % tax)

incomeLeft = income - sumInsurance - tax + subsidy

print ("到手收入:       %d" % incomeLeft)
