from typing import Union

import numpy as np
import talib

from jesse.helpers import slice_candles


def avgprice(candles: np.ndarray, sequential: bool = False) -> Union[float, np.ndarray]:
    """
    AVGPRICE - Average Price

    :param candles: np.ndarray
    :param sequential: bool - default: False

    :return: float | np.ndarray
    """
    candles = slice_candles(candles, sequential)

    res = talib.AVGPRICE(candles[:, 1], candles[:, 3], candles[:, 4], candles[:, 2])

    return res if sequential else res[-1]
