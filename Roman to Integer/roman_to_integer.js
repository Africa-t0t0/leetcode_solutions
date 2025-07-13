const mappingRomanValues = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}

const specialCases = [
    "CM", "CD", "XC", "XL", "IX", "IV"
];

const normalCases = [
    "M", "D", "C", "L", "X", "V", "I"
];

function romanToInt (romanNumber) {
    let totalSum = 0;
    let cleanedRomanNumber = String(romanNumber);
    specialCases.forEach((value) => {
        while (cleanedRomanNumber.includes(value)) {
            totalSum += mappingRomanValues[value];
            // I thought this replaced every value in the array, but it just replaces the first element that
            // matches the criteria. In Python, replace kills every match.
            cleanedRomanNumber = cleanedRomanNumber.replace(value, "");
        }
    });
    normalCases.forEach(value => {
        while (cleanedRomanNumber.includes(value)) {
            totalSum += mappingRomanValues[value];
            cleanedRomanNumber = cleanedRomanNumber.replace(value, "");
        }
    });
    return totalSum;
};