from numba import jit


@jit(cache=True)
def progress_sequence(c: int):
    """
    Modifies input value c by a given formula.

    Uses numba cached c compilation.
    """

    # c is even
    if c % 2 == 0:
        return c/2
    # c is uneven
    elif c % 2 == 1:
        return c * 3 + 1
    # c is not an int
    else:
        return c


@jit(cache=True)
def get_to_one(m: int):
    """
    Calls progress_sequence until c value of counter reaches 1.

    Uses no objects and numba cached c compilation.

    Args:
        m (int): Start value of the sequence.
    Return:
        num_steps (int): Number of steps required to reach 1.
    """
    num_steps = 0
    c = m
    while c != 1.:
        c = progress_sequence(c=c)
        num_steps += 1
    return num_steps
