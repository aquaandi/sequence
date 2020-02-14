from process import sequence


num_runs = 10000


def assignment():
    """
    Calculates the number of steps required to reach 1 in the sequence, for all m in defined range.
    See ..results/InterviewTask.pdf
    """
    for m in range(1, num_runs):
        counter = sequence.get_to_one(m)
        sequence.log_progress(counter, m)


if __name__ == "__main__":
    assignment()
