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
from backtest_trend_strategy_api import *
from backtest_stochastic_strategy_api import *
from backtest_momentum_strategy_api import *
from backtest_volatility_strategy_api import *
import plotly.express as px


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

strategies=['Momentum Strategy','Stochastic Oscillator Strategy','Volatility Skew Strategy','Trend Following Strategy']

scrip_name=['ASIANPAINT','EICHERMOT','HEROMOTOCO','TATAMOTORS','APOLLOHOSP','SBIN','M&M',
          'BEL','JSWSTEEL','ICICIBANK','INDUSINDBK','ONGC','BAJAJ-AUTO','BRITANNIA','NESTLEIND',
          'HINDALCO','RELIANCE','TRENT','TATASTEEL','DRREDDY','SHRIRAMFIN','KOTAKBANK','HDFCBANK',
          'AXISBANK','NTPC','TECHM','SBILIFE','CIPLA','GRASIM','HINDUNILVR','LT','TATACONSUM','WIPRO',
          'TITAN','BPCL','INFY','SUNPHARMA','TCS','MARUTI','HCLTECH','COALINDIA','ULTRACEMCO']

st.sidebar.write('--------------')
# Add a selectbox to the sidebar:
strategy_selectbox_side = st.sidebar.selectbox('Select your Quant Strategy', (strategies))


if (strategy_selectbox_side==strategies[0]):
	start_date=  st.date_input('Select Start Date for Backtesting', value=pd.to_datetime("2023-01-01",format="%Y-%m-%d").date())
	end_date=  st.date_input('Select End Date for Backtesting', value=pd.to_datetime("2023-01-31",format="%Y-%m-%d").date())
	df=backtest_momentum(start_date,end_date)
	avg_OC_return=df.loc[:, 'OC_return'].mean()
	avg_OH_return=df.loc[:, 'OH_return'].mean()
	cum_return=1
	for i in range(0,len(df)):
		r=(1+df['OC_return'].iloc[i]) 
		cum_return=cum_return*r
	cum_return=cum_return-1
	st.divider()
	col1, col2 = st.columns(2)
	with col1:
		st.caption("1⃣ Average Backtested Daily Returns (for Buy-Open & Sell-Close) are "+str(round(avg_OC_return,4)*100)+str("%"))
		st.caption("2⃣ Average Backtested Daily Returns (for Buy-Open & Sell-High) are "+str(round(avg_OH_return,4)*100)+str("%"))
	with col2:
		st.caption("3⃣ Cumulative Backtested Returns (for Buy-Open & Sell-Close) are "+str(round(cum_return,4)*100)+str("%"))
		cum_return=1
		for i in range(0,len(df)):
			r=(1+df['OH_return'].iloc[i]) 
			cum_return=cum_return*r
		cum_return=cum_return-1
		st.caption("4⃣ Cumulative Backtested Returns (for Buy-Open & Sell-High) are "+str(round(cum_return,4)*100)+str("%"))
	#st.dataframe(df)
	st.divider()
	fig1 = px.line(
      df,
      x="Datetime",
      y=["OC_return"]  
    )
	fig1.add_hline(y=avg_OC_return,line_dash='dash',line_color="red")
	fig1.update_layout(title={'text': "Backtesting Daily Returns (Buy-Open & Sell-Close)",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
	fig1.update_xaxes(title=" ")
	fig1.update_yaxes(title=" ")
	fig1.update_layout(showlegend=False)
	st.plotly_chart(fig1, use_container_width=True)
	st.divider()
	fig2 = px.line(
      df,
      x="Datetime",
      y=["OH_return"]  
    )
	fig2.add_hline(y=avg_OH_return,line_dash='dash',line_color="red")
	fig2.update_layout(title={'text': "Backtesting Daily Returns (Buy-Open & Sell-High)",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
	fig2.update_xaxes(title=" ")
	fig2.update_yaxes(title=" ")
	fig2.update_layout(showlegend=False)
	st.plotly_chart(fig2, use_container_width=True)

if (strategy_selectbox_side==strategies[1]):
	start_date=  st.date_input('Select Start Date for Backtesting', value=pd.to_datetime("2023-01-01",format="%Y-%m-%d").date())
	end_date=  st.date_input('Select End Date for Backtesting', value=pd.to_datetime("2023-01-31",format="%Y-%m-%d").date())
	df=backtest_stochastic(start_date,end_date)
	avg_OC_return=df.loc[:, 'OC_return'].mean()
	avg_OH_return=df.loc[:, 'OH_return'].mean()
	cum_return=1
	for i in range(0,len(df)):
		r=(1+df['OC_return'].iloc[i]) 
		cum_return=cum_return*r
	cum_return=cum_return-1
	st.divider()
	col1, col2 = st.columns(2)
	with col1:
		st.caption("1⃣ Average Backtested Daily Returns (for Buy-Open & Sell-Close) are "+str(round(avg_OC_return,4)*100)+str("%"))
		st.caption("2⃣ Average Backtested Daily Returns (for Buy-Open & Sell-High) are "+str(round(avg_OH_return,4)*100)+str("%"))
	with col2:
		st.caption("3⃣ Cumulative Backtested Returns (for Buy-Open & Sell-Close) are "+str(round(cum_return,4)*100)+str("%"))
		cum_return=1
		for i in range(0,len(df)):
			r=(1+df['OH_return'].iloc[i]) 
			cum_return=cum_return*r
		cum_return=cum_return-1
		st.caption("4⃣ Cumulative Backtested Returns (for Buy-Open & Sell-High) are "+str(round(cum_return,4)*100)+str("%"))
	#st.dataframe(df)
	st.divider()
	fig1 = px.line(
      df,
      x="Datetime",
      y=["OC_return"]  
    )
	fig1.add_hline(y=avg_OC_return,line_dash='dash',line_color="red")
	fig1.update_layout(title={'text': "Backtesting Daily Returns (Buy-Open & Sell-Close)",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
	fig1.update_xaxes(title=" ")
	fig1.update_yaxes(title=" ")
	fig1.update_layout(showlegend=False)
	st.plotly_chart(fig1, use_container_width=True)
	st.divider()
	fig2 = px.line(
      df,
      x="Datetime",
      y=["OH_return"]  
    )
	fig2.add_hline(y=avg_OH_return,line_dash='dash',line_color="red")
	fig2.update_layout(title={'text': "Backtesting Daily Returns (Buy-Open & Sell-High)",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
	fig2.update_xaxes(title=" ")
	fig2.update_yaxes(title=" ")
	fig2.update_layout(showlegend=False)
	st.plotly_chart(fig2, use_container_width=True)

if (strategy_selectbox_side==strategies[2]):
	start_date=  st.date_input('Select Start Date for Backtesting', value=pd.to_datetime("2023-01-01",format="%Y-%m-%d").date())
	end_date=  st.date_input('Select End Date for Backtesting', value=pd.to_datetime("2023-01-31",format="%Y-%m-%d").date())
	df=backtest_vol_skew(start_date,end_date)
	avg_OC_return=df.loc[:, 'OC_return'].mean()
	avg_OH_return=df.loc[:, 'OH_return'].mean()
	cum_return=1
	for i in range(0,len(df)):
		r=(1+df['OC_return'].iloc[i]) 
		cum_return=cum_return*r
	cum_return=cum_return-1
	st.divider()
	col1, col2 = st.columns(2)
	with col1:
		st.caption("1⃣ Average Backtested Daily Returns (for Buy-Open & Sell-Close) are "+str(round(avg_OC_return,4)*100)+str("%"))
		st.caption("2⃣ Average Backtested Daily Returns (for Buy-Open & Sell-High) are "+str(round(avg_OH_return,4)*100)+str("%"))
	with col2:
		st.caption("3⃣ Cumulative Backtested Returns (for Buy-Open & Sell-Close) are "+str(round(cum_return,4)*100)+str("%"))
		cum_return=1
		for i in range(0,len(df)):
			r=(1+df['OH_return'].iloc[i]) 
			cum_return=cum_return*r
		cum_return=cum_return-1
		st.caption("4⃣ Cumulative Backtested Returns (for Buy-Open & Sell-High) are "+str(round(cum_return,4)*100)+str("%"))
	#st.dataframe(df)
	st.divider()
	fig1 = px.line(
      df,
      x="Datetime",
      y=["OC_return"]  
    )
	fig1.add_hline(y=avg_OC_return,line_dash='dash',line_color="red")
	fig1.update_layout(title={'text': "Backtesting Daily Returns (Buy-Open & Sell-Close)",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
	fig1.update_xaxes(title=" ")
	fig1.update_yaxes(title=" ")
	fig1.update_layout(showlegend=False)
	st.plotly_chart(fig1, use_container_width=True)
	st.divider()
	fig2 = px.line(
      df,
      x="Datetime",
      y=["OH_return"]  
    )
	fig2.add_hline(y=avg_OH_return,line_dash='dash',line_color="red")
	fig2.update_layout(title={'text': "Backtesting Daily Returns (Buy-Open & Sell-High)",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
	fig2.update_xaxes(title=" ")
	fig2.update_yaxes(title=" ")
	fig2.update_layout(showlegend=False)
	st.plotly_chart(fig2, use_container_width=True)



if (strategy_selectbox_side==strategies[3]):
	start_date=  st.date_input('Select Start Date for Backtesting', value=pd.to_datetime("2023-01-01",format="%Y-%m-%d").date())
	end_date=  st.date_input('Select End Date for Backtesting', value=pd.to_datetime("2023-01-31",format="%Y-%m-%d").date())
	df=backtest_trend(start_date,end_date)
	avg_OC_return=df.loc[:, 'OC_return'].mean()
	avg_OH_return=df.loc[:, 'OH_return'].mean()
	cum_return=1
	for i in range(0,len(df)):
		r=(1+df['OC_return'].iloc[i]) 
		cum_return=cum_return*r
	cum_return=cum_return-1
	st.divider()
	col1, col2 = st.columns(2)
	with col1:
		st.caption("1⃣ Average Backtested Daily Returns (for Buy-Open & Sell-Close) are "+str(round(avg_OC_return,4)*100)+str("%"))
		st.caption("2⃣ Average Backtested Daily Returns (for Buy-Open & Sell-High) are "+str(round(avg_OH_return,4)*100)+str("%"))
	with col2:
		st.caption("3⃣ Cumulative Backtested Returns (for Buy-Open & Sell-Close) are "+str(round(cum_return,4)*100)+str("%"))
		cum_return=1
		for i in range(0,len(df)):
			r=(1+df['OH_return'].iloc[i]) 
			cum_return=cum_return*r
		cum_return=cum_return-1
		st.caption("4⃣ Cumulative Backtested Returns (for Buy-Open & Sell-High) are "+str(round(cum_return,4)*100)+str("%"))
	#st.dataframe(df)
	st.divider()
	fig1 = px.line(
      df,
      x="Datetime",
      y=["OC_return"]  
    )
	fig1.add_hline(y=avg_OC_return,line_dash='dash',line_color="red")
	fig1.update_layout(title={'text': "Backtesting Daily Returns (Buy-Open & Sell-Close)",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
	fig1.update_xaxes(title=" ")
	fig1.update_yaxes(title=" ")
	fig1.update_layout(showlegend=False)
	st.plotly_chart(fig1, use_container_width=True)
	st.divider()
	fig2 = px.line(
      df,
      x="Datetime",
      y=["OH_return"]  
    )
	fig2.add_hline(y=avg_OH_return,line_dash='dash',line_color="red")
	fig2.update_layout(title={'text': "Backtesting Daily Returns (Buy-Open & Sell-High)",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
	fig2.update_xaxes(title=" ")
	fig2.update_yaxes(title=" ")
	fig2.update_layout(showlegend=False)
	st.plotly_chart(fig2, use_container_width=True)