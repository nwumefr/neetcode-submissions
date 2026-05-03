func isAnagram(s string, t string) bool {
    smap := map[byte]int{}
    // tmap := map[byte]int{}
    
    if len(s) != len(t) {
        return false
    }

    for i := 0; i < len(s); i++{
        smap[s[i]] += 1
        smap[t[i]] -= 1
    }

    for i := 0; i < len(t); i++{
        if smap[t[i]]!=0{
            return false
        }
    }

    return true
}
