import sys
sys.setrecursionlimit(10000)

def tree_make_change(coin_vals, change, sor=False):
    """coin_vals is a list of positive ints and coin_vals[0] = 1, change is a positive int.
       Return the minimum number of coins needed to have a set of coins the values of which sum to change. Coins may be used more than once. For example, make_change([1, 5, 8], 11) should return 3.
    """

    #solve trivialities 
    if change == 0 or change == 1 or len(coin_vals) == 1:
        return (1, )*change #change in coin_vals or only 1 in coin_vals

    if not sor:
        coin_vals.sort(reverse=True)

    if change in coin_vals:
        return (change, )

    if change % coin_vals[0] == 0:
        return (coin_vals[0], ) * (change//coin_vals[0])

    #begin
    changes = () 
    diff = change - coin_vals[0]
    if diff > 0:
        changes += (coin_vals[0],) + tree_make_change(coin_vals, diff, True)

    else:
        # current_great: [1,3,4,5] 7 -> (5,1,1)
        # next_great: [1,3,4] 7 -> (3,4)

        next_great = tree_make_change(coin_vals[1:], change+coin_vals[0], True)
        current_great = tree_make_change(coin_vals[1:], change, True)

        if len(next_great) < len(current_great)+1:
            changes += ('next_great',) + next_great 
        else:
            changes += current_great 

    if 'next_great' in changes and changes.index('next_great') != 0:
        i = changes.index('next_great')+1
        changes = changes[i:]

    #Theta(f(a,b)) = a*log(a)*log(b)
    return changes
