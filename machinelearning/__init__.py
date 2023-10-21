"""
This library handles everything related to machine learning.

Library Information
-------------------
Workspace: pyprojecttools
FIlename: __init__.py
Path: machinelearning\__init__.py
Date: October, 20 2023

Notes
------


"""

import pickle
from typing import Literal, Callable


def load_save_model(
    model: Callable = None,
    model_file_path: str = None,
    mode: Literal["wb", "w", "r", "rb"] = None,
):
    """
    Saves or loads a machine learning model depending on the `mode` value.

    Parameters
    ----------
    model : Callable, optional
        Model that you want to save or load, by default None
    model_file_path : str, optional
        Path that you want to save the model, by default None
    mode : Literal, optional
        Mode that you want to load or save the model with, by default "wb"

    Returns
    -------
    Model or None
        Returns the model if a model is loaded, returns None otherwise.
    """
    with open(model_file_path, mode) as file:
        if mode in ["wb", "w"]:
            pickle.dump(model, file)
            return None
        elif mode in ["r", "rb"]:
            model = pickle.load(file)
            return model
        else:
            return None
