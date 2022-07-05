''' Selection sort presented in John Guttag book swaps for every iteration '''

def sel_sort(L):
    suffix_start = 0
    while suffix_start != len(L):
        for i in range(suffix_start, len(L)):
            if L[i] < L[suffix_start]:
                #swaps
                L[suffix_start], L[i] = L[i], L[suffix_start]
        suffix_start += 1



