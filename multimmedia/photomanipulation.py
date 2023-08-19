import glob
from typing import Literal

from PIL import Image

""" Utilities """


class GIF:
    def make_gif(
        frame_dir: str = ...,
        frame_type: Literal["jpg", "png"] = "jpg",
        save_as: str = ...,
        duration: int = 100,
        loop: int = 0,
        *args,
        **kwargs,
    ):
        """Static function for creating savable based on images in a directory

        Args:
            frame_dir (str, optional): directory where all frames are located. Defaults to ....
            frame_type (listeral): file extension of images in directory. Defaults to "jpg".
            save_as (str, optional): filename of gif. Defaults to ....
            duration (int, optional): duration of gif in seconds. Defaults to 100.
            loop (int, optional): option to loop gif a limited amount of times. Defaults to 0.
        """
        images = [
            Image.open(image) for image in glob.glob(f"{frame_dir}/*.{frame_type}")
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
