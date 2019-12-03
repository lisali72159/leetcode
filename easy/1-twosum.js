// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

//     Example:

// Given nums = [2, 7, 11, 15], target = 9,

//     Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

// var twoSum =
// function(nums, target){
//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[i] + nums[j] === target) {
//                 return [i, j];
//             }
//         }
//     }
// }

var twoSum = 
function(nums, target){
    let obj = {};
    for (let i = 0; i < nums.length; i++){
        obj[i] = nums[i];
        let diff = target - nums[i];
        for (var key in obj) {
            debugger
            if (obj[key] === diff && parseInt(key) !== i) {
                return [parseInt(key), i]
            }
        }
    }
}


console.log(twoSum([3,2,4], 6));
