''' So I fixed it to be compliant with a proper implementation of Sel sort, swaping only for every iteration in the outter loop'''

def optm_sel_sort(L):
    suffix_start = 0
    counter = 0

    while suffix_start != len(L):
        for i in range(counter+1, len(L)):
            if L[i] < L[suffix_start]:
                suffix_start = i
        #swaps
        L[suffix_start], L[counter] = L[counter], L[suffix_start]
        counter += 1
        suffix_start = counter 
