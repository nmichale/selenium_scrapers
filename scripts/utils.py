import dateutil
import datetime
import pandas as pd
from six import string_types

def date_callback(ctx, param, value):
    return dateutil.parser.parse(value).date() if isinstance(value, string_types) else value

date_click_last_bday = dict(default=(datetime.datetime.now() + pd.offsets.BDay(-1)).date(), callback=date_callback)

date_click_last_day = dict(default=(datetime.datetime.now() + pd.offsets.Day(-1)).date(), callback=date_callback)