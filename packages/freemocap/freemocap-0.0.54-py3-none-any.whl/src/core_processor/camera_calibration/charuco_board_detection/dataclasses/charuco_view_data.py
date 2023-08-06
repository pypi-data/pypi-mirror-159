from dataclasses import dataclass

import numpy as np

@dataclass
class CharucoViewData:
    charuco_corners: np.ndarray = None
    charuco_ids: np.ndarray = None
    aruco_square_corners: np.ndarray = None
    aruco_square_ids: np.ndarray = None
    full_board_found: bool = False
    some_charuco_corners_found: bool = False
    any_markers_found: bool = False
    image_width: int = None
    image_height: int = None


