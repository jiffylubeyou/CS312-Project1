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
        return (z**2) % N;
    else:
        return (x * z**2) % N;
	

def fprobability(k):
    # You will need to implement this function and change the return value.   
    return (1 - (1/2)**k);


def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 0.0


def fermat(N,k):

    for i in range(0, k):
        a = random.randint(1, (N - 1));
        if (mod_exp(a, (N - 1), N) == 1):
            continue;
        else:
            return 'composite';
    return 'prime';


    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.


def miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
	return 'composite'
