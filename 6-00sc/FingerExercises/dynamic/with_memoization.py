def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1, change is a positive int.
       Return the minimum number of coins needed to have a set of coins the values of which sum to change. 
       Coins may be used more than once. For example, make_change([1, 5, 8], 11) should return 3.
                                                                                                 """
    if change == 0 or change == 1:
        return change #change in coin_vals

    step = 1 
    possibilities = []

    try:
        return cached_changes(tuple(coin_vals), change)

    except KeyError:
        while step <= change:
            for i in range(change):
                if (change - i)/step in coin_vals:
                    possibilities.append(make_change(coin_vals, i) + step) #remainder changes + (change-i)
            step += 1

        result = min(possibilities)
        cached_changes(tuple(coin_vals), change, result)
        return result

        # Theta( f(a,b) ) = b^2 * a * log(a)

cache = dict()
def cached_changes(coins, change, result=None):
    if result:
        cache[(coins,change)] = result
    else:
        return cache[(coins,change)]
