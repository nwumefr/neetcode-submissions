func hasDuplicate(nums []int) bool {
    _map := map[int]int{}
    for i := 0; i < len(nums); i++{
        _map[nums[i]] += 1
        if _map[nums[i]] > 1{
            fmt.Println(_map[nums[i]])
            return true
        }
    }
    return false
}
