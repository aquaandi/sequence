from datetime import datetime
from multiprocessing import Pool

from process import sequence, sequence_fast

processor_name = "Ryzen 3700x 8-core"

def parallel_run(test_runs, sequence_module):
    """
    (Rereading the assignment, parallel implementation wasn't asked for. Leaving it in for reference)

    Parallel implementation mapping sequence objects to m parameter.
    """

    # threadpool for parallel processing
    pool = Pool(16)

    # parameters to map to parallel function calls
    m_list = list(range(1, test_runs))

    # Parallel processing on Ryzen 3700x 8-core/16T took: 0:00:03.658328
    for counter in pool.map(sequence_module.get_to_one, m_list):
        # print(counter.num_steps)
        pass


def single_thread_run(test_runs, sequence_module):
    for m in range(1, test_runs):
        counter = sequence_module.get_to_one(m)
        # print(counter.num_steps)


def evaluate_runtimes(method: str, sequence_module):
    test_runs = 500000

    start_parallel = datetime.now()
    parallel_run(test_runs, sequence_module)
    parallel_elapsed = datetime.now()-start_parallel

    # Single Thread processing on Ryzen 3700x 8-core took: 0:00:09.598735
    start_no_threading = datetime.now()
    single_thread_run(test_runs, sequence_module)
    single_thread_elapsed = datetime.now()-start_no_threading

    print("")
    print(method)
    print("Single Thread processing on "+processor_name+" took:", single_thread_elapsed)
    print("Parallel processing on "+processor_name+" took:", parallel_elapsed)
    print("Parallel speedup factor", str(round(single_thread_elapsed/parallel_elapsed, 3)))


def assignment():
    """
    Making the step calculation as fast as possible by removing object use and employing c compilation through numba.
    (Rereading the assignment, parallel implementation wasn't asked for. Leaving it in for reference)

    See InterviewTask.pdf

    Todo: Use Interface for sequence modules
    Todo: Implement CUDA Parallel Kernel Processing
    Todo: Improve algorithm using profiler
    Todo: Test parallel results vs single thread
    Todo: Store parallel computation results
    """

    print("Commencing assignment c)")

    evaluate_runtimes("Python compiled code using objects:", sequence)
    evaluate_runtimes("C compiled code using simple types:", sequence_fast)


if __name__ == "__main__":
    assignment()
