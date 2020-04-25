#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:21:19 2020

@author: 
    
link: https://docs.streamlit.io/getting_started.html
"""

#%%
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib
import matplotlib.pyplot as plt

#%%
def main():

    st.title('Intro')
    
    #%% .write() 
    st.write("Hello!")
    
    df0 = pd.DataFrame({"f": [1, 2, 3, 4],
                        "g": [10, 20, 30, 40]})
    st.write(df0)
    
    #%% magic
    df1 = pd.DataFrame({"f": [1, 2, 3, 4],
                        "g": [10, 20, 30, 40],
                        "letters": ['a', 'b', 'c', 'd']})
    df1

    #%% line chart
    
    st.write('Line chart')
    
    df2 = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
            )
    
    st.line_chart(df2)
    
    #%%
    st.write('sth')
    
    #%%
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)
    
    #%%
    st.write('Interactivity')
    
    if st.checkbox('Show df2'):
        df2
    
    #%%
    option = st.selectbox('which nr do you like:',
                         df0['f'],
                         key=0
                         )
    'You selected: ', option

    #%% sidebar
    option2 = st.sidebar.selectbox('which nr do you like:',
                         df0['f'],
                         key=1
                         )
    'You selected: ', option2

    #%%
    import time
    
    'Long computations'
    last_iter = st.empty()
    bar = st.progress(0)
    
    for i in range(100):
        last_iter.text(f'Iteration {i+1}')
        bar.progress(i+1)
        time.sleep(.1)

    "... we're done!"

#%%
if __name__=="__main__":
    main()

#%%