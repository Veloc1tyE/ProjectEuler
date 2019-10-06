# Efficient method to find last digits of 28433*2**(7830457))+1
number = 28433

for i in range(7830457):
    number = number*2
    number = number % 10**10
    
number += 1

# This question deals with probabilities with non-replacement

def prob2(blue, red):
    base = 1
    for i in range(2):
        base *= blue / (blue + red)
        blue -= 1
    return base

def binaryOp(blue, red, upper_right, lower_right,
             upper_left, lower_left, num):
    
    # binary search workhorse function
    # evaluate prob and proceed on this basis

    blue = (lower_right + upper_right) // 2
    red = (lower_left + upper_left) // 2
    # Now checker for bounds
    if prob2(blue, red) > 0.5:
        upper_right = blue
        lower_left = red
    else:
        lower_right = blue
        upper_left = red
        
    blue += num - (blue + red)
    
    return (blue, red, upper_right, 
            lower_right, upper_left,
            lower_left)

def find50(num):
    # Performs binary search
    # Ensures num is valid
    # First steps
    blue = num // 2
    red = num // 2
    blue += num - (blue + red)
    # Establish bounds
    # And binary search between them
    upper_right = num
    lower_right = blue
    upper_left = red
    lower_left = 0
    # Now we perform the search
    while True:
        """
        Now next, we'll try 0.75, 0.25. This will overshoot
        Next we know that blue lies between 0.5 and 0.75
        and red lies between 0.25 and 0.5.
        
        Therefore, we try the midpoints, 0.625 and 0.375,
        keep iteratively establishing new bounds like so
        """
        prevBlue, prevRed = blue, red # to compare later
        
        (blue, red, upper_right,
         lower_right, 
         upper_left,lower_left) =  binaryOp(blue,red,upper_right,lower_right,
                                             upper_left, lower_left, num)
        
        # print(blue, red)
        # Stopping conditions
        if prob2(blue,red) == 0.5:
            break
        # Break if we reach a point where we aren't going anywhere
        if prevBlue == blue or prevRed == red:
            break
    
    prob = prob2(blue,red)
    return blue, red, prob
    
def main(num):
    # Go for it
    blue, red, prob = find50(num)
    while prob != 0.5:
        # keep increasing
        num += 1
        blue, red, prob = find50(num)
    return blue, red


