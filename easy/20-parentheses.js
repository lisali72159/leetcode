// Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Note that an empty string is also considered valid.

// Example 1:

// Input: "()"
// Output: true
// Example 2:

// Input: "()[]{}"
// Output: true

// Example 4:

// Input: "([)]"
// Output: false
// Example 5:

// Input: "{[]}"
// Output: true

var isValid = function (s) {
    let obj = { ")": "(", "}": "{", "]": "[" }
    let arr = [];
    for (let i = 0; i < s.length; i++) {
        // console.log(s[i]); 
        // console.log(s[i + 1]);
        // console.log(obj[s[i]]);
        if (arr.length === 0) {
            arr.push(s[i]);
        } else if (obj[s[i]] === arr[arr.length - 1]) {
            arr.pop();
        } else {
            arr.push(s[i]);
        }
    }
    console.log(arr);
    return (arr.length === 0)  
};

console.log(isValid("()"));
console.log(isValid("{)"))