from krakentren import *
from pathlib import Path
import pandas as pd

pair = Coin("XXBTZEUR")

x = 1657964701

data = pair.get_ohlc_data("15", False, x)

print(data)
