// In a town, there are N people labelled from 1 to N.There is a rumor that one of these people is secretly the town judge.

// If the town judge exists, then:

// The town judge trusts nobody.
//     Everybody(except for the town judge) trusts the town judge.
// There is exactly one person that satisfies properties 1 and 2.
// You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

// If the town judge exists and can be identified, return the label of the town judge.Otherwise, return -1.

var findJudge = function(N, trust){
    let trustees = new Array(N).fill(0);
    let trusted = new Array(N).fill(0);

    trust.forEach(pair => {
        let person = pair[0];
        let possibleJudge = pair[1];

        trustees[person - 1] += 1;
        trusted[possibleJudge - 1] += 1;
    })

    for (let i = 0; i < trusted.length; i++) {
        if (trustees[i] === N - 1 && trusted[i] === 0) {
            return i + 1;
        }
    }
    return -1;
}