import random


def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    if (y == 0):
        return 1;
    temp = y // 2;
    z = mod_exp(x, temp, N);
    if ((y % 2) == 0):
        return (z^2) % N;
    else:
        return (x * z**2) % N;
	

def fprobability(k):
    # You will need to implement this function and change the return value.   
    return 0.0


def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 0.0


def fermat(N,k):
    # random.randint(0, N);

    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
	return 'prime'


def miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
	return 'composite'
