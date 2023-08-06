# Finscreen
Simple module that screens stocks on FinViz and scrapes the data into dataframe.

## Usage
The module can scrape the data from overview, valuation, financial and technical tabs, based on desired filters, orders and range. The data then could be used to extract the tickers list or various stock indicators, such as stock's ROI or RSI. Which in-turn creates a convienient way to pick stocks based on desired criteria and use this data in more complex projects. 

### Installation
Install the package via pip:
```shell
pip install finscreen
```

### Get Started
FinScreen has the following functions that return a Pandas DataFrame:
```shell
1. get_overview
2. get_valuation
3. get_financials
4. get_technicals
```

#### Functions arguments
Each of the functions have the same 3 arguments that have the following usage:
```shell
filter (string): Configure desired filter on Finviz website and paste the string after 'f=' from URL. Leave empty if needed.
order (string): Click on desired order on Finviz Table and paste the string after 'o=' from URL. Defaults to tickers in alphabetical order.
rg (integer): Desired range of scraping. To get all results navigate to the last table and paste the integer from URL. ; Defaults to 100.
```

### Examples
Exporting data to Excel:
```shell
import os
import finscreen

# Creating folder for data
dir_path = os.getcwd() # Selects current working directory of a process
new_path = f"{dir_path}/finviz_data" 

if not os.path.exists(new_path):
    os.makedirs(new_path)

# Setting up arguments
filter = 'cap_largeover' # FinViz filter configured to screen companies with market capitalization of $10bln+
rg = 1000 # Screens first 1000 stocks
order = 'industry' # Stocks ordered by industry in alphabetical order

# Assigning data to dataframes
overview = finscreen.get_overview(filter = filter, order = order, rg = rg)
valuation = finscreen.get_valuation(filter = filter, order = order, rg = rg)
financial = finscreen.get_financials(filter = filter, order = order, rg = rg)
technical = finscreen.get_technicals(filter = filter, order = order, rg = rg)

# Exporting data to Excel
try:
    overview.to_excel(new_path+'/overview.xlsx')
    valuation.to_excel(new_path+'/valuation.xlsx')
    financial.to_excel(new_path+'/financial.xlsx')
    technical.to_excel(new_path+'/technical.xlsx')
except Exception:
    pass
```

Extracting tickers into a list and downloading their price/volume data using yfinance module:
```shell
from finscreen import get_overview
import yfinance as yf

df = get_overview(filter = 'fa_div_pos,fa_epsyoy_o15') # Screening first 100 stocks that have positive dividend yield and EPS growth in the current year of over 15%.

tickers_list = df.index.to_list()

universe = yf.download(tickers_list, 
                       period = '5y',
                       interval = '1d',
                       threads = True,
                       )
```





