// Given a non - empty string s and a dictionary wordDict containing a list of non - empty words, determine if s can be segmented into a space - separated sequence of one or more dictionary words.

//     Note:

// The same word in the dictionary may be reused multiple times in the segmentation.
// You may assume the dictionary does not contain duplicate words.
//     Example 1:

// Input: s = "leetcode", wordDict = ["leet", "code"]
// Output: true
// Explanation: Return true because "leetcode" can be segmented as "leet code".

// Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
// Output: false


function wordBreak(string, wordDict) {
    let table = new Array(string.length + 1).fill(false);
    table[0] = true;

    for (let i = 0; i < table.length; i++) {
        if (table[i] === false) {
            continue;
        }
        for (let j = i + 1; j < table.length; j++) {
            let word = string.slice(i,j);
            if (wordDict.includes(word)){
                table[j] = true;
            }
        }
    }
    return table[table.length - 1]; 
}