class Counter:
    """
    Stores state information of the current sequence.
    """
    c = 1
    num_steps: int = 0


def log_progress(counter: Counter, m: int):
    print("Number of steps required to reach 1 for c_m(1) := ", m, " steps =", counter.num_steps)


def progress_sequence(c: int):
    """
    Modifies input value c by a given formula.
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


def get_to_one(m: int):
    """
    Calls progress_sequence until c value of counter reaches 1.

    Args:
        m (int): Start value of the sequence.
    Return:
        counter (Counter): State of the sequence.
    """
    counter = Counter()
    counter.c = m
    while counter.c != 1.:
        counter.c = progress_sequence(c=counter.c)
        counter.num_steps += 1
    return counter
