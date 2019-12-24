var maxNumberOfBalloons = function(text) {
    let letters = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0};
    
   
    for (let i = 0; i < text.length; i++){
        if (letters[text[i]] >= 0) {
            letters[text[i]] += 1;
        }
    }
    
    letters['l'] = Math.floor(letters['l'] / 2);
    letters['o'] = Math.floor(letters['o'] / 2);
    counts = Object.values(letters)
    
    return Math.min(...counts);
};

console.log(maxNumberOfBalloons('nlaebolko'));