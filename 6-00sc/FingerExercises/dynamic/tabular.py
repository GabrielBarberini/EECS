def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1, change is a positive int.
       Return the minimum number of coins needed to have a set of coins the values of which sum to change. 
       Coins may be used more than once. For example, make_change([1, 5, 8], 11) should return 3. """

    #solve trivialities
    if change == 0 or change == 1 or len(coin_vals) == 1:
        return change #change in coin_vals or only 1 in coin_vals

    coin_vals.sort(reverse=True)

    for number in coin_vals:
        if number > change:
            coin_vals.remove(number)

    if change in coin_vals:
        return 1

    if change % coin_vals[0] == 0:
        return change/coin_vals[0]

    #begin
    #WIP
