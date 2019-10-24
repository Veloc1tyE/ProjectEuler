import Foundation

// Hackerrank implementation
let tests = Int(readLine()!)

for i in 1...tests! {
    let limit = Int(readLine()!)

    var prev = 0
    var next = 1
    var num = 0
    var sum = 0

    while next < limit! {
        /*
        Sequentially compute the fibonacci sequence
        up to a certain limit, then add on to running
        total if even
        */
        num = prev
        prev = next
        next += num
        if (prev % 2 == 0) {
            sum += prev
        }
    }
    // And this will be the sum of all even fibonacci's
    // Below this point
    print(sum)
}
