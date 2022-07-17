class Solution {
    fun dfs(info: IntArray, cnt: Int, n: Int) {
        if (cnt == n + 1) {
            var apeach_point = 0
            var lion_point = 0
            for (i in 0..10) {
                if (info[i] != 0 || lion[i] != 0) {
                    if (info[i] < lion[i]) lion_point += 10 - i else apeach_point += 10 - i
                }
            }
            
            if (lion_point - apeach_point >= max) {
                res = lion.clone()
                max = lion_point - apeach_point
            }
            return
        }
        var j = 0
        while (j <= 10 && lion[j] <= info[j]) {
            lion[j]++
            dfs(info, cnt + 1, n)
            lion[j]--
            j++
        }
    }

    fun solution(n: Int, info: IntArray): IntArray {
        lion = IntArray(11)
        dfs(info, 1, n)
        return res
    }

    companion object {
        var res = intArrayOf(-1)
        lateinit var lion: IntArray
        var max = 0
    }
}
