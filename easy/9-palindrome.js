// Determine whether an integer is a palindrome.An integer is a palindrome when it reads the same backward as forward.

//     Example 1:

// Input: 121
// Output: true
// Example 2:

// Input: -121
// Output: false
// Explanation: From left to right, it reads - 121. From right to left, it becomes 121 -.Therefore it is not a palindrome.

var isPalindrome = function(x){
    let num = x.toString();
    for (let i = 0; i < num.length; i++) {
        if (num[i] !== num[num.length - 1 - i]){
            return false;
        }
    }
    return true;
}

console.log(isPalindrome(12));