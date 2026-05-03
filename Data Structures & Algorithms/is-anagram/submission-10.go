func isAnagram(s string, t string) bool {
    smap := map[byte]int{}
    // tmap := map[byte]int{}
    
    if len(s) != len(t) {
        return false
    }

    for i := 0; i < len(s); i++{
        smap[s[i]] += 1
        fmt.Println(s[i],smap[s[i]])

    }

    for i := 0; i < len(t); i++{
        smap[t[i]] -= 1
        // fmt.Println(t[i],tmap[t[i]])
    }

    for i := 0; i < len(t); i++{
        if smap[t[i]]!=0{
            return false
        }
    }

    return true
}
