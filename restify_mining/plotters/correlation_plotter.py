"""
Correlation plotter prints sample points in a 2D plane, to allow a visual detection of
concentrated clusters. Internally uses the pyplot scatter module. Useful e.g. for time to
error-rate ratio. Skill to error rate ratio, etc.
Author: Maximilian Schiedermeier
"""
import matplotlib.pyplot as plt

from restify_mining.plotters.correlation import Correlation
from restify_mining.plotters.group_samples import GroupSamples


# TODO: add axis override option to sync related graphs.

def plot_correlation(correlation: Correlation, file_name_marker: str) -> None:
    """
    Meta plotter method to just print my data with labels, but without any contrived parameters
    that nobody actually every needs.

    :param correlation: as the correlation data to visualize
    :return: None
    """

    # Compute plot axis dimensions including a buffer margin.
    x_max_with_buffer: float = correlation.x_axis_max * 1.05
    y_max_with_buffer: float = correlation.y_axis_max * 1.05
    # 10000
    plt.axis([0, y_max_with_buffer, 0, x_max_with_buffer])

    # Add the axis labels
    plt.xlabel(correlation.y_axis_label)
    plt.ylabel(correlation.x_axis_label)

    # For all groups in the bundle, add the sample points in the correct colour
    red_bundle: GroupSamples = correlation.red_bundle
    plt.scatter(red_bundle.y_axis_values, red_bundle.x_axis_values, color=red_bundle.group_tint)
    green_bundle: GroupSamples = correlation.green_bundle
    plt.scatter(green_bundle.y_axis_values, green_bundle.x_axis_values,
                color=green_bundle.group_tint)
    blue_bundle: GroupSamples = correlation.blue_bundle
    plt.scatter(blue_bundle.y_axis_values, blue_bundle.x_axis_values, color=blue_bundle.group_tint)
    yellow_bundle: GroupSamples = correlation.yellow_bundle
    plt.scatter(yellow_bundle.y_axis_values, yellow_bundle.x_axis_values,
                color=yellow_bundle.group_tint)

    plt.savefig("generated-plots/" + file_name_marker + correlation.filename)
    plt.show()
