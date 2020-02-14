import random
import sys

from process import task_a, task_b, task_c, task_d


def test_assignments():
    """
    Run all assignments. Simple test for exceptions.
    """
    task_a.assignment(random.randint(1,sys.maxsize))
    task_b.assignment()
    task_c.assignment()
    task_d.assignment()


if __name__ == "__main__":
    test_assignments()
