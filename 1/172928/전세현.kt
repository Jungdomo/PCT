class Solution {
    fun solution(park: Array<String>, routes: Array<String>): IntArray {
        var currentPosition: IntArray = intArrayOf(0, 0)
        val movements = HashMap<String, IntArray>()
        movements.put("N", intArrayOf(-1, 0))
        movements.put("S", intArrayOf(1, 0))
        movements.put("W", intArrayOf(0, -1))
        movements.put("E", intArrayOf(0, 1))

        for (i in 0 until park.size) {
            for (j in 0 until park[i].length) {
                if (park[i][j] == 'S') {
                    currentPosition = intArrayOf(i, j)
                }
            }
        }

        for (route in routes) {
            val direction = route.split(" ")[0]
            val steps = route.split(" ")[1].toInt()

            var newRow = currentPosition[0]
            var newCol = currentPosition[1]
            for (step in 1..steps) {
                val movement = movements[direction]!!
                newRow += movement[0]
                newCol += movement[1]

                if (newRow < 0 || newCol < 0 || newRow >= park.size || newCol >= park[0].length || park[newRow][newCol] == 'X') {
                    newRow = currentPosition[0]
                    newCol = currentPosition[1]
                    break
                }
            }

            currentPosition[0] = newRow
            currentPosition[1] = newCol
        }

        return currentPosition
    }
}
