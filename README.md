# Stock Ticker Dashboard
if see error:
from pandas_datareader.fred import FredReader
	File "/usr/local/lib/python3.6/dist-packages/pandas_datareader/fred.py", line 1, in <module>
		from pandas.core.common import is_list_like
ImportError: cannot import name 'is_list_like'

replace from pandas.core.common import is_list_like with from pandas.api.types import is_list_like
