from process import sequence


def assignment(m: int):
    """
    Calculates the number of steps required to reach 1 in the sequence, for any given m.
    See ..results/InterviewTask.pdf
    """
    counter = sequence.get_to_one(m)
    sequence.log_progress(counter, m)


if __name__ == "__main__":
    assignment(42)

