class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let res = 0;
        let cpt = 0

        for (let i=0; i<nums.length; i++){
            if (nums[i] == 0) {
               res = Math.max(res, cpt);
               cpt = 0;
            } else {
                cpt += 1;
            }
        }
        return Math.max(res, cpt);
    }
}
