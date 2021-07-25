"""
1 - Receive integer number
2 - Verify number is multiple 3 and 5:
    return bacon with egges
3 - Verify number not is multiple 3 and 5:
    return starves
4 - Verify number is multiple only 3:
    return  bacon
5 - Verify number is multiple only 5:
    return egges

"""


def bacon_with_egges(n):
    assert isinstance(n, int), 'n must be in'

    if n % 3 == 0 and n % 5 == 0:
        return 'bacon with egges'

    if n % 3 == 0:
        return 'bacon'

    if n % 5 == 0:
        return 'egges'

    return 'starves'
