from collections import OrderedDict
from itertools import product, izip

# Row i column j gives the child ID for sack ID i and present ID j.
# This is just an excerpt as the full happiness matrix has entries numbering
# in the billions!
HAPPINESS_MATRIX = [
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78],
    [2, 7, 9, 16, 20, 29, 35, 46, 54, 67, 77,],
    [4, 5, 11, 14, 22, 27, 37, 44, 56, 65,],
    [8, 17, 19, 30, 34, 47, 53, 68, 76,],
    [12, 13, 23, 26, 38, 43, 57, 64,],
    [18, 31, 33, 48, 52, 69, 78,],
    [24, 25, 39, 42, 58, 63,],
    [32, 49, 51, 70, 74,],
    [40, 41, 59, 62,],
    [50, 71, 73,],
    [60, 61,],
    [72,],
 ]

DIFFERENCE_MATRIX = [
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,],
    [5, 2, 7, 4, 9, 6, 11, 8, 13, 10,],
    [1, 6, 3, 8, 5, 10, 7, 12, 9,],
    [9, 2, 11, 4, 13, 6, 5, 18,],
    [1, 10, 3, 11, 5, 14, 7],
    [13, 2, 15, 4, 17, 6],
    [1, 14, 3, 16, 5],
    [17, 2, 19, 4],
    [1, 18, 3],
    [21, 22],
    [1,],
]


def santas_little_helper(sack, present):
    '''Helper function which changes depending whether the sack and present have
    odd or even IDs. Unfortunately, Santa was a little exhausted by caculating
    all the prime factors of 6300000000 so he doesn't have a precise
    mathematical proof that this works. I think we can cut him a little slack 
    given the joy he brings to children across the world!
    '''
    if not sack % 2 and not present % 2:
        return -present
    if not sack % 2 and present % 2:
        return - 2 * sack - present
    if sack % 2 and not present % 2:
        return 3 - 4 * sack - 3 * present
    if sack % 2 and present % 2:
        return 1 - 2 * sack - 3 * present


def child(sack, present):
    '''Return child ID for the given sack and present IDs.'''
    if sack == 1:
        # The top row of the happiness matrix is given by the sum of the
        # arithmetic series (1 + 1 + ... + 1 ).
        return (present * (present + 1)) // 2
    return ((sack + present) ** 2 + santas_little_helper(sack, present)) // 2


def factor_pairs(prime_factorisation):
    '''Given prime factorisation of a number n represented as an OrderedDict,
    return set of pairs of factors of n.

    Example
    -------
    27 = 2*2*3*3 so the input would be OrderedDict([(2, 2), (3, 2)]) 
    returning {(1, 36), (2, 18), (3, 12), (4, 9), (6, 6),
               (36, 1), (18, 2), (12, 3), (9, 4)}
    '''
    # Pairs of factors consist of products of primes appearing in the prime
    # factorisation. Iterating over all combinations of multiplicities of primes
    # will thus yield all pairs.
    primes = prime_factorisation.keys()
    multiplicities = prime_factorisation.values()
    factor_pair_multiplicity_possibilities = [ 
        xrange(multiplicity + 1) for multiplicity in multiplicities
    ]

    pairs = set()
    seen = set()
    factor_combos = product( *factor_pair_multiplicity_possibilities )
    for combo in factor_combos:
        if combo in seen:
            continue
        # For each combination representing the multiplicities of primes in the
        # first factor, get the multiplicities of primes in the other factor.
        inverse_combo = tuple( 
            prime_factor - x for x, prime_factor in izip(combo, multiplicities)
        )
        factor1 = reduce( lambda x, y: x * y, [
            prime ** factor for prime, factor in izip(primes, combo)
        ])
        factor2 = reduce( lambda x, y: x * y, [
            prime ** factor for prime, factor in izip(primes, inverse_combo) 
        ])
        pairs.add((factor1, factor2))
        if factor1 != factor2:
            pairs.add((factor2, factor1))
        seen |= {combo, inverse_combo}

    return pairs


def checksum(factors):
    return sum(child(sack, present) for sack, present in factors) % 100000000
