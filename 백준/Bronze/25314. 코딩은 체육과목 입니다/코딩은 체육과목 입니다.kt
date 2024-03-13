import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    solution()
}

fun solution() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val sb = StringBuilder()
    for (i in 0 until n / 4) {
        sb.append("long ")
    }
    sb.append("int")
    println(sb)
}
