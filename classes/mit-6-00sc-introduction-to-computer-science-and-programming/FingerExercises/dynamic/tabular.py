def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1, change is a positive int.
       Return the minimum number of coins needed to have a set of coins the values of which sum to change. Coins may be used more than once. For example, make_change([1, 5, 8], 11) should return 3.

    """
    #solve trivialities
    if change == 0 or change == 1 or len(coin_vals) == 1:
        return [1, ]*change #change in coin_vals or only 1 in coin_vals

    coin_vals.sort(reverse=True)

    if change in coin_vals:
        return [change]

    if change % coin_vals[0] == 0:
        return [coin_vals[0], ] * (change//coin_vals[0])

    #begin
    result = [1,]*change
    results = [change]
    coin_vals.sort()

    left_over = 0
    coin = 1
    while coin < len(coin_vals):
        current_coin = coin_vals[coin]
        previous_coin = coin_vals[coin-1]

        previous_coin_fit_current = (change // current_coin) * current_coin 
        removed = 0
        added = 0

        while previous_coin <= (previous_coin_fit_current - removed):
            result.remove(previous_coin)
            removed += previous_coin

        while added < previous_coin_fit_current: 
            result.append(current_coin)
            added += current_coin

        left_over += (previous_coin_fit_current - removed)

        if left_over > 0:
            left_over -= result.pop(0)
        if coin == len(coin_vals)-1 and\
        left_over < 0 and\
        -left_over in coin_vals:
            result.insert(0, -left_over)
        elif coin == len(coin_vals)-1 and\
        left_over < 0 and\
        -left_over not in coin_vals:
            '''-2 -5 = -7; -7 + 4 = -3; -3 + 3 = 0'''
            left_over -= result.pop()
            remainings = coin_vals[:len(coin_vals)-1]
            remainings.sort(reverse=True)
            for option in remainings:
                if left_over < 0:
                    left_over += option
                    result.append(option)
                else:
                    break

        results.append(result)
        coin+=1
        if len(result) == 2:
            break

    return results[-1]
    #Theta(f(a,b)) = a*log(b)
