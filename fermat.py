import random


def prime_test(N, k):
	return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    # The time complexity here is constant and so is space complexity
    if (y == 0):
        return 1;
    # if we reach this portion, it recurses so the time compexity max is n^2, n being N, and N will be log(N) time
    # complexity because multiplication complexity is dependant number of bits that N takes up in binary, which is log(N)

    temp = y // 2;
    z = mod_exp(x, temp, N);
    if ((y % 2) == 0):
        return (z**2) % N;
    else:
        return (x * z**2) % N;
    # since multiplication is n^2 time complexity, that within a recurser (runs it N times) function becomes N^3, which is the time
    # complexity of all of the md_exp function
    # space complexityin terms of N will just be log(N) in base 2 log because N has arithmatic done on it and N is stored
    # in log(N) number of bits to be computed by the computer
	

def fprobability(k):
    # time complexity here is just k^3 because division is n^3 time complexity and it runs the division times so k(n^3) is like k^3
    #space complexity is constant here because it doesn't grow even as k grows
    return (1 - (1/2)**k);


def mprobability(k):
    # same here as the f probability with both space and time complexity
    return (1 - (1/4)**k);


def fermat(N,k):

    #the mod_exp function has N^3 time complexity, and this runs mod_exp k number of times (in the worst case scenario that is,
    # which is whenever we have a prime number).
    for i in range(0, k):
        a = random.randint(1, (N - 1));
        if (mod_exp(a, (N - 1), N) == 1):
            continue;
        else:
            return 'composite';
    return 'prime';
    # This means that in terms of k and N, k(N^3) is the time complexity for the whole fermat function
    # the space complexity is constant in terms of k because running a loop multiple times won't increase the memory
    # that you consume, and N is represented in N bits and uses mod_exp function so space complexity for fermats theorem is log(N)


def miller_rabin(N,k):

    # this right here is k(N^3) time complexity as we saw earlier, and log(N) space complexity
    if (fermat(N,k) == 'composite'):
        return 'composite';

    # this is similar to fermats in complexity but it will run more times if the square root can be found from the
    # N - 1 exponent, and in worst case scenario, that runs log(N) times (I think) so the time complexity will become
    # k((N^3) * log(N)) because in worst case scenario, number is prime and mod_exp with N^3 has to be run log(N) times,
    # and all that has to be run k times
    # the space complexity should remaint the same as fermats with log(N) space complexity because loops don't accumulate
    # space taken
    for i in range(0, k):
        a = random.randint(1, N - 1);
        exp = N - 1;
        while (exp % 2 == 0):
            if (mod_exp(a, (exp), N) == 1):
                exp = exp / 2;
                continue;
            else:
                return 'composite';

    return 'prime';
