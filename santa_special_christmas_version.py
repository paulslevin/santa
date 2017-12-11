from collections import OrderedDict
from itertools import product, izip

### DO NOT TRY AND RUN THIS ###
### IT MAY BE CHRISTMASSY, BUT TERRIBLE PYTHON ###


def 🍪(💰, 🎁):
    if not 💰 % 2 and not 🎁 % 2:
        return -🎁
    if not 💰 % 2 and 🎁 % 2:
        return - 2 * 💰 - 🎁
    if 💰 % 2 and not 🎁 % 2:
        return 3 - 4 * 💰 - 3 * 🎁
    if 💰 % 2 and 🎁 % 2:
        return 1 - 2 * 💰 - 3 * 🎁


def 👶(💰, 🎁):
    '''Return 👶 ID for the given 💰 and 🎁 IDs.'''
    if 💰 == 1:
        # The top row of the ☺️ matrix is given by the sum of the
        # arithmetic series (1 + 1 + ... + 1 ).
        return (🎁 * (🎁 + 1)) // 2
    return ((💰 + 🎁) ** 2 + 🍪(💰, 🎁)) // 2


def ✔️➕(🏭):
    return ➕(👶(💰, 🎁) for 💰, 🎁 in 🏭) % 100000000
