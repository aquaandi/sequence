import os

import plotly
import plotly.graph_objects as go

from process import sequence

num_runs = 10000

# plot will be saved here
output_filename = "../results/sequence_plot.html"


def gen_plots(m_values, num_steps):
    """
    Generates, displays and disk-saves plotly interactive .html plots.

    Args:
        m_values (list(int)): Start values of the sequence.
        num_steps (list(int)): Number of steps required to reach one for corresponding m.
    """

    # generate plot
    fig = go.Figure([go.Scatter(x=m_values, y=num_steps)])
    fig.update_layout(xaxis_rangeslider_visible=True)
    plotly.offline.plot(fig, filename=output_filename, auto_open=False)

    # write plot to disk
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("Plot saved to", dir_path, output_filename)

    # display plot
    fig.show()


def assignment():
    """
    Repeats assignment b, but stores num_steps to plot using the plotly library.
    May plot through matplotlib alternatively.

    See ..results/InterviewTask.pdf
    """
    print("Commencing assignment d)")

    m_values = []
    num_steps = []
    for m in range(1, num_runs):
        counter = sequence.get_to_one(m)
        sequence.log_progress(counter, m)

        m_values.append(m)
        num_steps.append(counter.num_steps)

    gen_plots(m_values, num_steps)


if __name__ == "__main__":
    assignment()
