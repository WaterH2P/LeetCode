// 面试题 08.03. 魔术索引
// 魔术索引。 
// 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。
// 给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMagicIndex = function(nums) {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === i) { return i; }
    if (nums[i] > i) { i = nums[i] - 1; }
  }
  return -1;
};

let nums = [-294354269, -168926144, -62738268, 3]
console.log(findMagicIndex(nums))