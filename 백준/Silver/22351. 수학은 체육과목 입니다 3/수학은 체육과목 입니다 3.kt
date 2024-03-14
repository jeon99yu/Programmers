import java.io.BufferedReader
import java.io.IOException
import java.io.InputStreamReader

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))

    val s = br.readLine()

    var n = 1
    if (s.length < 4) {
        val c = s[0]
        while (n < s.length) {
            if (s[n] != c) {
                break
            }
            n++
        }
    }

    val sb = StringBuilder()
    if (n == s.length) {
        sb.append("$s $s")
    } else {
        for (i in 1..999) {
            if (s.startsWith(i.toString())) {
                var str = s
                for (j in i..999) {
                    if (str.startsWith(j.toString())) {
                        str = str.substring(j.toString().length)
                    } else {
                        break
                    }
                    if (str.isEmpty()) {
                        sb.append("$i $j")
                        break
                    }
                }
                if (sb.isNotEmpty()) {
                    break
                }
            }
        }
    }
    print(sb)
}