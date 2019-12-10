// Longest Substring w/o Repeating Characters

function longest(s){
    let current = "";
    let [longest, start] = [0,0];
    for (let i = 0; i < s.length; i++) {
        start = current.indexOf(s[i]);
        if (start !== -1) {
            current = currentlslice(start + 1) + s[i]
        } else {
            current += s[i];
        }
        longest = Math.max(longest, current.length);
    }
    return longest;
}