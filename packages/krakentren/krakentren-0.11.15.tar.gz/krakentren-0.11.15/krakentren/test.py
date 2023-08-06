from krakentren import *
from pathlib import Path
import pandas as pd

pair = Coin("XXBTZEUR")

data = pair.get_ohlc_data("15")

add_ta(data,
       sma1={'indicator': 'sma',
             'period': 10},
       sma2={'indicator': 'sma',
             'period': 20},
       mfi={'indicator': 'mfi',
            'period': 10},
       psl={'indicator': 'psl',
            'period': 10},
       chop={'indicator': 'chop',
             'period': 15},
       roc={'indicator': 'roc',
            'period': 20},
       adl={'indicator': 'adl'},
       psar={'indicator': 'psar',
             'af': 0.025,
             'max_af': 0.25})

my_list = data.columns.values.tolist()

for i in my_list:
    print(i)

# print(data)
