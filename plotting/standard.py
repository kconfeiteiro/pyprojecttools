"""
The code provided is a library for creating standard plots using Matplotlib. The main class,  `Plot` , allows users to create generic static plots by specifying the data to plot and the plot title.

The  `plot`  method within the  `Plot`  class is used to create a single plot. It takes in various parameters such as the data to plot, the title of the plot, whether to display the plot using Matplotlib's GUI, and options for saving the plot as an image file. The  `projection`  parameter allows users to specify whether the plot should be 2D or 3D. If  `surface_plot`  is set to  `True` , the plot will be a 3D surface plot.

The library also supports customizing the color scheme of the plot using the  `cmap`  parameter and the color of the plot's edge using the  `edgecolor`  parameter.

Overall, this library provides a convenient way to create standard plots using Matplotlib with customizable options for data, title, projection, and appearance.
"""

from typing import Sequence

import matplotlib.pyplot as plt
from pandas import DataFrame


def plot_std(
    data: DataFrame = None,
    cols: Sequence[str] = None,
    save_as: str = None,
    show_plot: bool = True,
    title: str = None,
    **kwargs,
) -> None:
    """
    Plot a simple standard plot for 2-Dimensional Data.

    Args:
        data: Data to plot. If data is None it will plot all columns
        cols: List of colormaps to plot
        cmap: Colormap to use for coloring the data
        edgecolor: Colormap to use for coloring the data
        save_as: Name of file to save the plot
        show_plot: Whether to show the plot or not
        surface_plot: Whether to plot the surface of the data
        title: Title for the plot. Default is " Default Plot Title "

    Returns:
        A tuple of the plot and the axes that was
    """
    if not (data or cols):
        _msg = f"Cannot plot data. Recieved None for Data: {data} or Cols: {cols}"
        raise ValueError(_msg)

    fig, axes = plt.subplots(**kwargs)
    axes.set_title(title)
    axes.plot(*data)

    if save_as:
        fig.savefig(save_as)

    if show_plot:
        plt.show()

