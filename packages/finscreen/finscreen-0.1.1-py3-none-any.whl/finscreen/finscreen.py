import requests 
import os
import typing
import pandas as pd
from tqdm import tqdm


# Creating headers to access FinViz
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
   
# Scraping the data to Dataframes
def get_overview(filter: str = '', order: str = 'ticker', rg: int = 100) -> pd.DataFrame:
    """
    Scrape the Overview Tab to a dataframe. 
    Before specifying arguments, make sure you're using correct tab.
    
    Arguments:
        filter: Configure desired filter on Finviz website and paste the string after 'f=' from URL. Leave empty if needed.
        order: Click on desired order on Finviz Table and paste the string after 'o=' from URL. Defaults to tickers in alphabetical order.
        rg: Desired range of scraping. To get all results navigate to the last table and paste the integer from URL. ; Defaults to 100.
    Returns:
        Pandas dataframe with the data
    """
    
    overview = pd.DataFrame()
    
    for i in tqdm(range(0, rg, 20)):

        screen = requests.get(f'https://finviz.com/screener.ashx?v=111&f={filter}&r={i}&o={order}', headers = headers).text 
        tables = pd.read_html(screen)
        tables = tables[-2]
        tables.columns = tables.iloc[0]
        tables = tables[1:]
        overview = overview.append(tables, ignore_index = True)

    overview = overview.drop_duplicates(subset = 'Ticker')
    overview.set_index('Ticker', inplace = True)
    overview = overview.drop(['No.'], axis = 1)
    overview = overview.replace('-', '0')
    
    # Changing percentages to numerical type
    for col in overview:
        overview[col] = overview[col].str.rstrip('%')
    
    overview = overview.apply(pd.to_numeric, errors = 'ignore')
    overview['Change'] = overview['Change'].div(100)
    
    return overview    

def get_valuation(filter: str = '', order: str = 'ticker', rg: int = 100) -> pd.DataFrame:
    """
    Scrape the Valuation Tab to a dataframe. 
    Before specifying arguments, make sure you're using correct tab.
    
    Arguments:
        filter: Configure desired filter on Finviz website and paste the string after 'f=' from URL. Leave empty if needed.
        order: Click on desired order on Finviz Table and paste the string after 'o=' from URL. Defaults to tickers in alphabetical order.
        rg: Desired range of scraping. To get all results navigate to the last table and paste the integer from URL. ; Defaults to 100.
    Returns:
        Pandas dataframe with the data.
    """
    
    valuation = pd.DataFrame()
    
    for i in tqdm(range(0, rg, 20)):

        screen = requests.get(f'https://finviz.com/screener.ashx?v=121&f={filter}&r={i}&o={order}', headers = headers).text 
        tables = pd.read_html(screen)
        tables = tables[-2]
        tables.columns = tables.iloc[0]
        tables = tables[1:]
        valuation = valuation.append(tables, ignore_index = True)

    valuation = valuation.drop_duplicates(subset = 'Ticker')
    valuation.set_index('Ticker', inplace = True)
    valuation = valuation.drop(['No.'], axis = 1)
    valuation = valuation.replace('-', '0')
    
    for col in valuation:
        valuation[col] = valuation[col].str.rstrip('%')
    
    valuation = valuation.apply(pd.to_numeric, errors = 'ignore')
    
    valuation[[
        'EPS this Y', 
        'EPS next Y', 
        'EPS past 5Y', 
        'EPS next 5Y', 
        'Sales past 5Y', 
        'Change']] = valuation[[
            'EPS this Y', 
            'EPS next Y', 
            'EPS past 5Y',
            'EPS next 5Y', 
            'Sales past 5Y', 
            'Change']].div(100)
        
    return valuation

def get_financials(filter: str = '', order: str = 'ticker', rg: int = 100) -> pd.DataFrame:
    """
    Scrape the Financial Tab to a dataframe. 
    Before specifying arguments, make sure you're using correct tab.
    
    Arguments:
        filter: Configure desired filter on Finviz website and paste the string after 'f=' from URL. Leave empty if needed.
        order: Click on desired order on Finviz Table and paste the string after 'o=' from URL. Defaults to tickers in alphabetical order.
        rg: Desired range of scraping. To get all results navigate to the last table and paste the integer from URL. ; Defaults to 100.
    Returns:
        Pandas dataframe with the data.
    """
    
    financial = pd.DataFrame()
    
    for i in tqdm(range(0, rg, 20)):

        screen = requests.get(f'https://finviz.com/screener.ashx?v=161&f={filter}&r={i}&o={order}', headers = headers).text 
        tables = pd.read_html(screen)
        tables = tables[-2]
        tables.columns = tables.iloc[0]
        tables = tables[1:]
        financial = financial.append(tables, ignore_index = True)

    financial = financial.drop_duplicates(subset = 'Ticker')
    financial.set_index('Ticker', inplace = True)
    financial = financial.drop(['No.'], axis = 1)
    financial = financial.replace('-', '0')
    
    for col in financial:
        financial[col] = financial[col].str.rstrip('%')
    
    financial = financial.apply(pd.to_numeric, errors = 'ignore')
    
    financial[['Dividend', 
               'ROA', 
               'ROE', 
               'ROI', 
               'Gross M', 
               'Oper M', 
               'Profit M', 
               'Change']] = financial[[
                   'Dividend', 
                   'ROA', 
                   'ROE', 
                   'ROI', 
                   'Gross M', 
                   'Oper M', 
                   'Profit M', 
                   'Change']].div(100)
        
    return financial  
    
def get_technicals(filter: str = '', order: str = 'ticker', rg: int = 100) -> pd.DataFrame:
    """
    Scrape the Technical Tab to a dataframe. 
    Before specifying arguments, make sure you're using correct tab.
    
    Arguments:
        filter: Configure desired filter on Finviz website and paste the string after 'f=' from URL. Leave empty if needed.
        order: Click on desired order on Finviz Table and paste the string after 'o=' from URL. Defaults to tickers in alphabetical order.
        rg: Desired range of scraping. To get all results navigate to the last table and paste the integer from URL. ; Defaults to 100.
    Returns:
        Pandas dataframe with the data.
    """
    
    technical = pd.DataFrame()
    
    for i in tqdm(range(0, rg, 20)):

        screen = requests.get(f'https://finviz.com/screener.ashx?v=171&f={filter}&r={i}&o={order}', headers = headers).text 
        tables = pd.read_html(screen)
        tables = tables[-2]
        tables.columns = tables.iloc[0]
        tables = tables[1:]
        technical = technical.append(tables, ignore_index = True)

    technical = technical.drop_duplicates(subset = 'Ticker')
    technical.set_index('Ticker', inplace = True)
    technical = technical.drop(['No.'], axis = 1)
    technical = technical.replace('-', '0')
    
    for col in technical:
        technical[col] = technical[col].str.rstrip('%')
    
    technical = technical.apply(pd.to_numeric, errors = 'ignore')
    technical[['SMA20', 
               'SMA50', 
               'SMA200', 
               '52W High', 
               '52W Low', 
               'Change', 
               'from Open', 
               'Gap']] = technical[['SMA20', 
                                    'SMA50', 
                                    'SMA200', 
                                    '52W High', 
                                    '52W Low', 
                                    'Change', 
                                    'from Open', 
                                    'Gap']].div(100)
        
    return technical

    