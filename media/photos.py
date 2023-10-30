"""
Helper functions for manipulation of images, plots, etc.

Script Information
------------------
- Creator: Krystian D. Confeiteiro
    - Contact: confeitk@outlook.com
- Workspace: pyprojecttools
- FIlename: photomanipulation.py
- Path: multimmedia\photomanipulation.py
- Date: September, 14 2023
"""

from glob import glob
from typing import Literal

from PIL import Image


def make_gif(
    frame_dir: str = None,
    frame_type: Literal["jpg", "png"] = "jpg",
    save_as: str = None,
    duration: int = 100,
    loop: int = 0,
    *args,
    **kwargs,
):
    """
    Static function for creating savable based on images in a directory.

    Args:
        duration (int, optional): Duration of gif in seconds. Defaults to 100.
        frame_dir (str, optional): Directory where all frames are located. Defaults to None.
        frame_type (listeral): File extension of images in directory. Defaults to "jpg".
        loop (int, optional): Option to loop gif a limited amount of times. Defaults to 0.
        save_as (str, optional): Filename of gif. Defaults to None.
    """
    images = [
        Image.open(image)
        for image in glob("{}\\*.{}".format(frame_dir, frame_type.replace(".", "")))
    ]

    first_frame = images[0]
    first_frame.save(
        save_as,
        format="GIF",
        append_images=images,
        save_all=True,
        duration=duration,
        loop=loop,
        *args,
        **kwargs,
    )
