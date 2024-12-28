"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
from datetime import datetime
#from datetime import date
#import datetime
from momentum_strategy_1_api import *
from stochastic_oscillator_1_api import *
from valid_date_return import *
from stochastic_charts_api import *
from data_snapshot_date_api import *
from volatility_skew_strategy_api import *
from volatility_charts_api import *
from trend_following_strategy_api import *
from trend_following_charts_api import *
from pairs_trading_strategy_api import *
import plotly.express as px
from ml_forecast_predict import *
from ml_forecast_charts_roc import *
from ml_forecast_metrics import *
import matplotlib.pyplot as plt1

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
warnings.filterwarnings('ignore')

st.sidebar.image("logo.jpg")
#st.sidebar.write('Last Refreshed On ' + str(data_snapshot_date()))
#st.sidebar.markdown(":red[Last Refreshed On]")
#st.sidebar.write(' ')
#st.sidebar.write(' ')
st.sidebar.write('--------------')
st.sidebar.subheader('Navigation Bar')
st.sidebar.page_link("open_hft_frontend.py", label="Quant Strategies", icon="🏠")
st.sidebar.page_link("pages/intraday_forecasts.py", label="Intraday ML Forecasts", icon="⛅")
st.sidebar.page_link("pages/backtests.py", label="Backtesting Module", icon="📠")
st.sidebar.write('🍵 Data Last Refreshed On ' + str(data_snapshot_date()))

#strategies=['Momentum Strategy','Stochastic Oscillator Strategy','Volatility Skew Strategy','Trend Following Strategy','Pairs Trading Strategy']

scrip_name=['ASIANPAINT','EICHERMOT','HEROMOTOCO','TATAMOTORS','APOLLOHOSP','SBIN','M&M',
          'BEL','JSWSTEEL','ICICIBANK','INDUSINDBK','ONGC','BAJAJ-AUTO','BRITANNIA','NESTLEIND',
          'HINDALCO','RELIANCE','TRENT','TATASTEEL','DRREDDY','SHRIRAMFIN','KOTAKBANK','HDFCBANK',
          'AXISBANK','NTPC','TECHM','SBILIFE','CIPLA','GRASIM','HINDUNILVR','LT','TATACONSUM','WIPRO',
          'TITAN','BPCL','INFY','SUNPHARMA','TCS','MARUTI','HCLTECH','COALINDIA','ULTRACEMCO']

st.sidebar.write('--------------')
#st.write("Data Refresh Date: "+str(data_snapshot_date()))


st.header('Using XGBoost ML model for Stock Prediction',divider='grey')

col1, col2 = st.columns(2)
with col2:
	df1=ml_model_predict()
	df1=df1[['ScripName','weighted_vol','weighted_daily_return','stochastic_signal','pred']]
	df1 = df1.sort_values(by=['pred'], ascending=False)
	#st.dataframe(df1)
	st.dataframe(df1,hide_index=True,
	  column_config=dict(
	    ScripName=st.column_config.TextColumn('Scrip Name'),
	    pred=st.column_config.NumberColumn('Buy Signal'),
	    weighted_vol=st.column_config.NumberColumn('Weighted Volatility'),
	    weighted_daily_return=st.column_config.NumberColumn('Weighted Daily Return'),
	    stochastic_signal=st.column_config.NumberColumn('Stochastic Signal')
	  )
	  )


with col1:
	with open('model.pkl', 'rb') as f:
		model = pickle.load(f)
	
	st.pyplot(plot_importance(model).figure)
	
	confusion_matrix=ml_metrics()
	cm_matrix = pd.DataFrame(data=confusion_matrix, columns=['Actual Positive:1', 'Actual Negative:0'], 
                                 index=['Predict Positive:1', 'Predict Negative:0'])
	#st.dataframe(cm_matrix)
	fig=px.imshow(cm_matrix,text_auto=True)
	st.plotly_chart(fig, use_container_width=True)




with col2:
	chart_roc=ml_model_charts_roc()
	fig = px.line(
	    chart_roc,
	    x="fpr_train",
	    y=["tpr_train"]  
	)
	fig.update_layout(
	title={
	    'text': "ROC Curve",
	    'y':0.9,
	    'x':0.5,
	    'xanchor': 'center',
	    'yanchor': 'top'})   
	fig.update_xaxes(title="False Positive Rate ")
	fig.update_yaxes(title="True Positive Rate ")
	fig.update_layout(showlegend=False)
  	
	st.plotly_chart(fig, use_container_width=True)


