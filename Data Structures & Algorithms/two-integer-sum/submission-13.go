import (
    "slices"
)
func twoSum(nums []int, target int) []int {
    _map := map[int]int{}
    _dup := map[int]int{}

    _ret := []int{}
    for i := 0; i < len(nums);i++{
        result := target - nums[i]
        _map[nums[i]] = result
        _dup[nums[i]] += 1 
    }
    // fmt.Println(_map)
    // fmt.Println(_dup)
    for k := 0; k < len(nums);k++{
        // fmt.Println(k)
        if slices.Contains(nums,_map[nums[k]]){
            // fmt.Println()
            if _dup[nums[k]] > 1 || (nums[k] != _map[nums[k]]){
                _ret = append(_ret,k)
            }
        }
    }
    return _ret
}
