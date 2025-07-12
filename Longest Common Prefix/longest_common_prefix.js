/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let longestCommonPrefix = "";

    const maxLength = Math.min(...strs.map(str => str.length));

    if (strs.includes("")) return "";

    for (let i = 0; i < maxLength; i++) {
        // this is key, here we are getting the column of the matrix
        const column = strs.map(str => str[i]);

        const allEquals = column.every(element => element === column[0]);

        if (allEquals) {
            longestCommonPrefix += column[0];
        } else {
            break;
        }
    }

    return longestCommonPrefix;
};


const longest = longestCommonPrefix(["dog","racecar","car"]);

console.log(longest);