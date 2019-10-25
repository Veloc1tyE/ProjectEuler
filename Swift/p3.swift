// Hackerrank solution to p3
import Foundation

func primeFactor(_ n : Int) -> Int {
    /*
    Finds the largest prime factor of n
    by repeatedly dividing by prime factors and
    expressing the residue
    */
    var res = n
    var i = 2
    while (i * i <= res) {
        while (res % i == 0 && i != res) {
            res = res / i
        }
        i += 1
    }
    return res
}

let tests = Int(readLine()!)

for it in 1...tests! {
    let limit = Int(readLine()!)
    print(primeFactor(limit!))
}
