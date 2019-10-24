import Foundation

/*
Use of arithmetic series formula to solve problem quickly for hackerrank
*/

func p1(_ n : Int) -> Int {    
    /* 
    Check up to n-1, to find all divisible numbers
    Express answer in terms of arithmetic sequences
    */
    // First find sum of threes
    let threeCap = (n - 1) / 3 
    let threeSum = 3 * (threeCap * (threeCap + 1)) / 2
    // Then sum of fives
    let fiveCap = (n - 1) / 5
    let fiveSum = 5 * (fiveCap * (fiveCap + 1)) / 2
    // Then fifteens
    let fifteenCap = (n - 1) / 15
    let fifteenSum = 15 * (fifteenCap * (fifteenCap + 1)) / 2
    // Add sums of numbers divisible by three or five below the cap
    // Subtract the sum of numbers divisible by fifteen, these are counted twice
    return threeSum + fiveSum - fifteenSum
}

// Hackerrank solution
let tests = Int(readLine()!)

for _ in 1...tests! {
    let limit = Int(readLine()!)
    print(p1(limit!))
}
