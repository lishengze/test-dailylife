var income = 12000;
var rateNumb = 5;
var incomeRate = new Array(rateNumb);

for (var i = 0; i < rateNumb; ++i) {
    incomeRate[i] = {
        'name': 'origin name',
        'value':0
    };
}

incomeRate[0].name = '养老金:        '
incomeRate[0].value = 0.08;

incomeRate[1].name = '医疗金:        '
incomeRate[1].value = 0.02;

incomeRate[2].name = '失业金:        '
incomeRate[2].value = 0.005;

incomeRate[3].name = '公积金:        '
incomeRate[3].value = 0.12;

incomeRate[4].name = '所得税:        '
incomeRate[4].value = 0.16;

var antiTax = 0;

console.log ('总收入:        ' + income);

for (var i = 0; i < rateNumb-1; ++i) {
    console.log (incomeRate[i].name + Math.ceil(income * incomeRate[i].value) +'  比率: ' + incomeRate[i].value);
    antiTax += income * incomeRate[i].value;
}

var incomeWithOutFiveTax = income - antiTax;
var subsidy              = 1000;
var incomeForTax         = incomeWithOutFiveTax + subsidy;


var officialAntiTax = 3500;
var incomeWithOutOfficalTax = incomeForTax - officialAntiTax;
var personalTax = Math.ceil(incomeWithOutOfficalTax * 0.2 - 555);

var incomeLeft = incomeForTax - personalTax;


var sumTax = antiTax + personalTax;

console.log ('扣除五险一金:   ' + incomeWithOutFiveTax);
console.log ('补贴:          ' + subsidy);
console.log ('交税基数:      ' + incomeForTax);
console.log ('个人纯收入:     ' + incomeLeft);
console.log ('个人所得税:     ' + personalTax);
console.log ('五金+税:       ' + sumTax);



