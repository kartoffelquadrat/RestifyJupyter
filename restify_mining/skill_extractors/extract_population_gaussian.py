"""
This module reads participant skills from the participant/skills.csv file, computes the gaussian
distributions per skill and creates a plot. The output file is stored in:
"generated-plots/gaussian.png"
Author: Maximilian Schiedermeier
"""

from restify_mining.skill_extractors import participant_stat_tools
from restify_mining.markers import skills_markers
from restify_mining.data_objects.participant import Participant
from restify_mining.scatter_plotters.skill_plotter import plot_gaussian


def extract_population_gaussian(population: list[Participant]) -> None:
    """
    Helper method to compute a gaussian distribution (defined by mean and standard dev) for every
    skill and produce plot
    :param population: as the subset of the study participants to analyze.
    :return: None.
    """
    mean_scores = participant_stat_tools.build_mean_skills(population)
    stddev_scores = participant_stat_tools.build_standard_deviation_skills(population)

    # Plot gaussian curves for all participant skills
    for index in range(len(skills_markers.skill_tags)):
        plot_gaussian(mean_scores[index], stddev_scores[index], skills_markers.palette[index])
