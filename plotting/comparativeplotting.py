"""
This script utilizes the Comparative class to create static comparative plots for 2-3 variables. It takes a `DataFrame` object as input, which should contain the data to be plotted.

Workspace: NASA-Internship-2023
FIlename: correlative.py
Path: plotting\correlative.py

Notes:
------
- The Comparative class provides various options to customize the plot, such as specifying a common x-axis, setting the figure size, choosing plot types, and more.
- Ensure that the data provided is in the appropriate format and contains the necessary columns for plotting.
"""
from typing import List, Literal, Optional, Tuple, TypeAlias

import matplotlib.pyplot as plt
from pandas import DataFrame

from datahelpers import pull_columns
from dtypes import rect3d
from utilities.strtools import make_vec_comp_names as vect


_vcomptypes: TypeAlias = Optional[List[rect3d] | Literal["All"]]

def compare(
    data: DataFrame = None,
    common_xaxis: rect3d = "x",
    display: bool = True,
    figsize: Tuple[int, int] = None,
    figure_title: str = None,
    figure_xsuptitle: str = None,
    figure_ysuptitle: str = None,
    save_as: str = None,
    sharex: bool = False,
    subplot_types: Literal["scatter", "line"] = "line",
    vector_componenets: _vcomptypes = None,
    vector_types: List[str] = None,
    xlim: Tuple[int] = None,
    ylim: Tuple[int] = None,
    **kwargs,
):
    """
    Creates a static comparitive plot for 2-3 variables (creates `m x n` grid of comparative plots).

    Args:
        common_xaxis (list or str, optional): enables a common axis for each subplot. Defaults to "x".
        display (bool, optional): option to display via built-in GUI. Defaults to True.
        figsize (tuple, optional): tuple of desired figsize (units are in inches). Defaults to None.
        figure_title (str, optional): title for entire figure. Defaults to None.
        figure_xsuptitle (str, optional): x-subtitle for entire figure. Defaults to None.
        figure_ysuptitle (str, optional): y-subtitle for entire figure. Defaults to None.
        save_as (str, optional): name of file for saving. Defaults to None.
        sharex (bool, optional): enable if subplots share a common x-axis. Defaults to False.
        subplot_types (str, optional): plot type for subplots (line or scatter). Defaults to "line".
        vector_componenets (list of str, optional): components of 'vector_types' to plot (i.e, 'x', 'y', etc.). Defaults to None.
        vector_types (list of str, optional): denoted letter(s) for vector components (i.e, 'B', 'V', etc.). Defaults to None.
        xlim (tuple of int, optional): upper and lower limits of x-axis, formatted (lower, upper). Defaults to None.
        ylim (tuple of int, optional): upper and lower limits of y-axis, formatted (lower, upper). Defaults to None.
    """
    if vector_componenets in ["All", None]:
        vector_componenets = ["x", "y", "z"]

    COLUMNS = vect(vector_types, vector_componenets)
    DATA = pull_columns(*COLUMNS)

    x = data[common_xaxis]
    fig, axes = plt.subplots(len(vector_types), len(vector_componenets), **kwargs)
    if figsize:
        fig.set_figwidth(figsize[0])
        fig.set_figheight(figsize[1])

    if figure_title:
        fig.suptitle(figure_title)

    if figure_xsuptitle:
        fig.supxlabel(figure_xsuptitle)

    if figure_ysuptitle:
        fig.supylabel(figure_ysuptitle)

    for col, ax, colname in zip(DATA, axes.flatten(), COLUMNS):
        ax.yaxis.label.set(rotation="horizontal", ha="right")

        if subplot_types == "scatter":
            ax.scatter(x, col)
        else:
            ax.plot(x, col)

        ax.set_ylabel(f"${colname}$")
        if not sharex:
            ax.set_xlabel(f"${common_xaxis}$")

        if xlim:
            ax.set_xlim(*xlim)
        if ylim:
            ax.set_ylim(*ylim)

    if save_as:
        fig.savefig(save_as)

    if display:
        plt.show()
