import pandas as pd
import os

user = os.environ.get('USER', os.environ.get('USERNAME'))
filepath = f"C:/Users/{user}/Downloads/Assets.csv"

crestron = pd.read_csv(filepath)

def mac_with_dots(series):
    '''requires pandas. accepts a pandas series of mac addresses, and returns that series, formatted with dots separating the hex octets. original format must be consistent.
    Example: C44268xxxxxx or C4-42-68-xx-xx-xx become C4.42.68.xx.xx.xx
    
    :param series: pandas series
    :returns: pandas series'''

    if series[0][2] == '-':
        s = (series.str.slice(start=0, stop=2) + "." +
        series.str.slice(start=3, stop=5) + "." +
        series.str.slice(start=6, stop=8) + "." +
        series.str.slice(start=9, stop=11) + "." +
        series.str.slice(start=12, stop=14) + "." +
        series.str.slice(start=15, stop=17))
    else:
        s = (series.str.slice(start=0, stop=2) + "." +
            series.str.slice(start=2, stop=4) + "." +
            series.str.slice(start=4, stop=6) + "." +
            series.str.slice(start=6, stop=8) + "." +
            series.str.slice(start=8, stop=10) + "." +
            series.str.slice(start=10, stop=12))
    return s
    

crestron['Mac Address'] = mac_with_dots(crestron['Mac Address'])

crestron.to_csv(filepath, index=False)