import Foundation

func p1(_ n : Int) -> Int {
    // Initialise total counter
    var total = 0
    /* Now loop through all values from 1 to n-1
    And add to total if they are divisible by three or 5
    */
    for i in 1...n-1 {
        if i % 3 == 0 || i % 5 == 0 {
            total += i 
        }
    }
    return total
}

print(p1(1000))
