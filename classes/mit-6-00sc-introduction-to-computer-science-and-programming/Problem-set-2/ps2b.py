'''Implement the compute_deriv function. This function computes the derivative of a polynomial function. It takes in a tuple of numbers poly and returns the derivative, which is also a polynomial represented by a tuple.'''

def reverse_tuple(in_tuple):
    l = list()
    for i in in_tuple:
        l.append(i)
    l.reverse()
    return tuple(l)

def compute_deriv(poly):
    poly_dev = list()
    poly = reverse_tuple(poly)

    for power in range(len(poly)):
        if power == 0:
            poly_dev.append(0)
        else:
            poly_dev.insert(power-1, (power+1) * poly[power])
    poly_dev.reverse()
    return poly_dev 

print(compute_deriv( (-13.39, 0.0, 17.5, 3.0, 1.0) ) )

# Problem Set 2b
# Name: Gabriel Barberini
# Collaborators: None
# Time Spent (min): 20:00
