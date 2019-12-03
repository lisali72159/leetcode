// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

//     Example 1:

// Input: ["flower", "flow", "flight"]
// Output: "fl"
// Example 2:

// Input: ["dog", "racecar", "car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

var longestCommonPrefix = function(strings) {
    
    let temp = strings[0];
    for (let i = 1; i < strings.length; i++) {
        let word = strings[i];
        for (let j = 0; j < temp.length; j++) {
            if (temp[j] !== word[j] || temp[j] === undefined || word[j] === undefined){
                temp = temp.slice(0,j)
            }
        }
    }
    return temp;
}