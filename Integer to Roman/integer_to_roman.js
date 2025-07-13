// start with the biggest values, covering all options. By doing this you dont have to check special cases
// in a separated function or condition, we simply check each option.

const romanValues = [
    1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
];

const romanNumbers = [
    "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
];

function convertIntegerToRoman (number) {
    let romanNumber = "";

    romanValues.forEach((value, index) => {
        while (number >= value) {
            number -= value;
            romanNumber += romanNumbers[index];
        }
    });

    return romanNumber;
}

console.log(convertIntegerToRoman(58));