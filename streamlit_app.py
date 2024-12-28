#----------------------------------------------------------------------------------------------
#Community Cloud | Deployment Guidelines
#1. Make sure to modify the "devcontainer.json" file in the .devcontainer folder in root directory
#2. Change the name of execution file to open_hft_frontend.py
#----------------------------------------------------------------------------------------------


#--------------------------------------------------------------------
#IMPORT ALL EXTERNAL REQUIRED LIBRARIES & DEPENDENCIES
#--------------------------------------------------------------------
import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import warnings

#--------------------------------------------------------------------
#IMPORT ALL INTERNAL REQUIRED LIBRARIES & DEPENDENCIES
#--------------------------------------------------------------------
from api.momentum_strategy_1_api import *
from api.data_snapshot_date_api import *
#from stochastic_oscillator_1_api import *
#from valid_date_return import *
#from stochastic_charts_api import *
#from volatility_skew_strategy_api import *
#from volatility_charts_api import *
#from trend_following_strategy_api import *
#from trend_following_charts_api import *
#from pairs_trading_strategy_api import *


#--------------------------------------------------------------------
#SET DISPLAY PARAMETERS FOR STREAMLIT
#--------------------------------------------------------------------
st.set_page_config(layout="wide", initial_sidebar_state="expanded")
warnings.filterwarnings('ignore')

#--------------------------------------------------------------------
#SECTION 2 - INTERNAL VARIABLE DECLARATION
#--------------------------------------------------------------------
strategies=['Momentum Strategy','Stochastic Oscillator Strategy','Volatility Skew Strategy','Trend Following Strategy','Pairs Trading Strategy']

scrip_name=['ASIANPAINT','EICHERMOT','HEROMOTOCO','TATAMOTORS','APOLLOHOSP','SBIN','M&M',
          'BEL','JSWSTEEL','ICICIBANK','INDUSINDBK','ONGC','BAJAJ-AUTO','BRITANNIA','NESTLEIND',
          'HINDALCO','RELIANCE','TRENT','TATASTEEL','DRREDDY','SHRIRAMFIN','KOTAKBANK','HDFCBANK',
          'AXISBANK','NTPC','TECHM','SBILIFE','CIPLA','GRASIM','HINDUNILVR','LT','TATACONSUM','WIPRO',
          'TITAN','BPCL','INFY','SUNPHARMA','TCS','MARUTI','HCLTECH','COALINDIA','ULTRACEMCO']


#--------------------------------------------------------------------
#HOME PAGE CODE STARTS HERE
#--------------------------------------------------------------------
#SECTION 1 - SIDE PANEL CODE
#--------------------------------------------------------------------
st.sidebar.image("logo.jpg")
st.sidebar.write('--------------')
st.sidebar.subheader('Navigation Bar')
st.sidebar.page_link("streamlit_app.py", label="Quant Strategies", icon="🏠")
st.sidebar.page_link("pages/intraday_forecasts.py", label="Intraday ML Forecasts", icon="⛅")
st.sidebar.page_link("pages/backtests.py", label="Backtesting Module", icon="📠")
st.sidebar.write('🍵 Data Last Refreshed On ' + str(data_snapshot_date()))
st.sidebar.write('--------------')
strategy_selectbox_side = st.sidebar.selectbox('Select your Quant Strategy', (strategies))

#--------------------------------------------------------------------
#SECTION 1 - MAIN PANEL CODE & FUNCTIONAL CALLS
#--------------------------------------------------------------------

if (strategy_selectbox_side==strategies[0]):
  'Below are the stock recommendations for ', strategy_selectbox_side
  df1=momentum_strategy_1(str(data_snapshot_date()))
  st.dataframe(df1,hide_index=True,
    column_config=dict(
      R1Y_return=st.column_config.NumberColumn('R1Y Return', format='%.2f %%'),
      R6M_return=st.column_config.NumberColumn('R6M Return', format='%.2f %%'),
      R3M_return=st.column_config.NumberColumn('R3M Return', format='%.2f %%'),
      R1M_return=st.column_config.NumberColumn('R1M Return', format='%.2f %%'),
      Momentum_Score=st.column_config.NumberColumn('Momentum Score', format='%.2f')
      )

    )
  '-----------------------------------------'
  st.write("""
  **🌁Legend**

  • **R1Y Return** - _Rolling 1 Years Return_  
  • **R6M Return** - _Rolling 6 Months Return_  
  • **R3M Return** - _Rolling 3 Months Return_  
  • **R1M Return** - _Rolling 1 Months Return_  
  • **Momentum Score** - _Arithmetic Average of R1Y, R6M, R3M & R1M Percentiles_
  """)
  '-----------------------------------------'
  




else:
  'Strategy not yet configured'