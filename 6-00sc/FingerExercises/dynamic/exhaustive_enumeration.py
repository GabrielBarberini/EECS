def tabuall_make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1, change is a positive int.
       Return the minimum number of coins needed to have a set of coins the values of which sum to change. 
       Coins may be used more than once. For example, make_change([1, 5, 8], 11) should return 3. """

    #solve trivialities
    if change == 0 or change == 1 or len(coin_vals) == 1:
        return change #change in coin_vals or only 1 in coin_vals

    coin_vals.sort(reverse=True)

    if change in coin_vals:
        return 1

    if change % coin_vals[0] == 0:
        return change/coin_vals[0]

    #begin
    combinations = list() 
    possibilities = {change} 

    for n in coin_vals:
        i = 1
        while change % (n*i) != change:
            combinations.append((n,)*i)
            i+= 1

    i = 0
    while len(combinations[i])+1 < min(possibilities): 
        for number in coin_vals:
            attempt = (combinations[i] + (number,))
            size = len(attempt)
            total = sum(attempt)

            if total > change or attempt in combinations:
                next
            else:
                combinations.append(attempt)

            if change - total == 0:
                possibilities.add(size)
        i += 1

    return min(possibilities)
    # Theta(f(a,b)) = a^2 * b ?
