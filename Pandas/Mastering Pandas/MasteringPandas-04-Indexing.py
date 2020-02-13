
# coding: utf-8

# <h1>Chapter 4: Indexing and Selecting</h1>

# First we import the standard <em>numpy</em> and <em>pandas</em> modules.

# In[3]:


import numpy as np
import pandas as pd


# Create a time series of crude oil spot prices for the 4 quarters of 2013, taken from IMF data:  

# In[4]:


SpotCrudePrices_2013_Data={
                'U.K. Brent' : {'2013-Q1':112.9, '2013-Q2':103.0, '2013-Q3':110.1, '2013-Q4':109.4},
                'Dubai':{'2013-Q1':108.1, '2013-Q2':100.8, '2013-Q3':106.1,'2013-Q4':106.7},
                'West Texas Intermediate':{'2013-Q1':94.4, '2013-Q2':94.2, '2013-Q3':105.8,'2013-Q4':97.4}}
                
SpotCrudePrices_2013=pd.DataFrame.from_dict(SpotCrudePrices_2013_Data)
SpotCrudePrices_2013


# Select the prices for the available time periods of Dubai crude using the [] operator:

# In[5]:


dubaiPrices=SpotCrudePrices_2013['Dubai']; dubaiPrices


# Select the columns in a particular order:

# In[6]:


SpotCrudePrices_2013[['West Texas Intermediate','U.K. Brent']]


# In[7]:


SpotCrudePrices_2013['Brent Blend']


# In[8]:


SpotCrudePrices_2013.get('Brent Blend')


# In[9]:


SpotCrudePrices_2013.get('U.K. Brent')


# In[10]:


SpotCrudePrices_2013.get('Brent Blend','N/A')


# In[11]:


SpotCrudePrices_2013['2013-Q1']


# In[12]:


dubaiPrices['2013-Q1']


# Retrieve values directly as an attribute 

# In[13]:


SpotCrudePrices_2013.Dubai


# In[14]:


SpotCrudePrices_2013


# Rename the column index names so they are all valid identifiers:

# In[20]:


SpotCrudePrices_2013.columns=['Dubai','UK_Brent', 
                                       'West_Texas_Intermediate']
SpotCrudePrices_2013


# SpotCrudePrices_2013.West_Texas_Intermediate

# Select by specifying column index number:

# In[18]:


SpotCrudePrices_2013[[1]]


# <h2>Range Slicing </h2>

# Obtain the 1st 2 rows:

# In[23]:


SpotCrudePrices_2013[:2]


# Obtain all rows starting from index 2:

# In[24]:


SpotCrudePrices_2013[2:]


# Obtain rows at interval of 2, starting from row 0:

# In[25]:


SpotCrudePrices_2013[::2]


# Reverse the order of rows in DataFrame:

# In[26]:


SpotCrudePrices_2013[::-1]


# <h4>Series behavior </h4>

# In[29]:


dubaiPrices=SpotCrudePrices_2013['Dubai']
dubaiPrices


# Obtain last 3 rows or all rows higher than the first.

# In[28]:


dubaiPrices[1:]


# Obtain all rows but the last:

# In[31]:


dubaiPrices[:-1]


# Reverse the rows:

# In[32]:


dubaiPrices[::-1]


# ## Label-oriented Indexing

# Create a DataFrame:

# In[33]:


NYC_SnowAvgsData={'Months' :          
                            ['January','February','March', 
                            'April', 'November', 'December'],
                            'Avg SnowDays' : [4.0,2.7,1.7,0.2,0.2,2.3],
                            'Avg Precip. (cm)' : [17.8,22.4,9.1,1.5,0.8,12.2],
                            'Avg Low Temp. (F)' : [27,29,35,45,42,32] }


# In[34]:


NYC_SnowAvgsData


# In[35]:


NYC_SnowAvgs=pd.DataFrame(NYC_SnowAvgsData,      
                      index=NYC_SnowAvgsData['Months'], 
                      columns=['Avg SnowDays','Avg Precip. (cm)',                                                               
                               'Avg Low Temp. (F)'])
NYC_SnowAvgs


# Using single label with <em>.loc</em> operator:

# In[36]:


NYC_SnowAvgs.loc['January']


# Using list or labels:

# In[37]:


NYC_SnowAvgs.loc[['January','April']]


# Using label range:

# In[38]:


NYC_SnowAvgs.loc['January':'March']


# Row index must be specified first:

# In[39]:


NYC_SnowAvgs.loc['Avg SnowDays']


# In[40]:


NYC_SnowAvgs.loc[:,'Avg SnowDays']


# Specific 'coordinate' selection

# In[41]:


NYC_SnowAvgs.loc['March','Avg SnowDays']


# Alternative style:

# In[42]:


NYC_SnowAvgs.loc['March']['Avg SnowDays']


# Using square brackets ( [ ] ):

# In[43]:


NYC_SnowAvgs['Avg SnowDays']['March']


# [ ] operator cannot be used to select rows directly.

# In[44]:


NYC_SnowAvgs['March']['Avg SnowDays']


# Use <em>.loc</em> operator instead

# In[45]:


NYC_SnowAvgs.loc['March']


# <h3>Selection using a Boolean array</h3>

# In[46]:


NYC_SnowAvgs.loc[NYC_SnowAvgs['Avg SnowDays']<1,:]


# In[47]:


SpotCrudePrices_2013.loc[:,SpotCrudePrices_2013.loc['2013-Q1']>110]


# In[48]:


SpotCrudePrices_2013.loc['2013-Q1']>110


# <h2>Integer-oriented Indexing</h2>

# Create DataFrame

# In[51]:


import scipy.constants as phys
import math


# In[55]:


sci_values=pd.DataFrame([[math.pi, math.sin(math.pi), 
                                    math.cos(math.pi)],
                                   [math.e,math.log(math.e), 
                                    phys.golden],
                                   [phys.c,phys.g,phys.e],
                                   [phys.m_e,phys.m_p,phys.m_n]],
                          index=list(range(0,20,5)))
sci_values


# Select first two rows using integer slicing:

# In[53]:


sci_values.iloc[:2]


# Select speed of light and acceleration of gravity in the 3rd row:

# In[54]:


sci_values.iloc[2,0:2]


# Arguments to <em>.iloc</em> are strictly positional:

# In[56]:


sci_values.iloc[10]


# Use <em>.loc</em> instead:

# In[57]:


sci_values.loc[10]


# Slice out specific row:

# In[58]:


sci_values.iloc[2:3,:]


# Obtain cross-section using integer position:

# In[59]:


sci_values.iloc[3]


# Attempt to slice past the end of the array : 

# In[60]:


sci_values.iloc[6,:]


# Selection of scalar values and timings.

# In[61]:


sci_values.iloc[3,0]


# In[62]:


sci_values.iat[3,0]


# In[63]:


get_ipython().magic('timeit sci_values.iloc[3,0]')


# In[65]:


get_ipython().magic('timeit sci_values.iat[3,0]')


# <h2>Mixed Indexing with the .ix operator</h2>

# In[67]:


stockIndexDataDF=pd.read_csv('data/stock_index_data.csv')


# In[68]:


stockIndexDataDF


# In[69]:


stockIndexDF=stockIndexDataDF.set_index('TradingDate')
stockIndexDF


# <b>Using a single label:</b>

# In[70]:


stockIndexDF.ix['2014/01/30']


# <b>Using list of labels</b>:

# In[71]:


stockIndexDF.ix[['2014/01/30']]


# <b>Difference between using scalar indexer and list indexer:</b>

# In[72]:


type(stockIndexDF.ix['2014/01/30'])


# In[73]:


type(stockIndexDF.ix[['2014/01/30']])


# <b>Using a label-based slice:</b>

# In[74]:


tradingDates=stockIndexDataDF.TradingDate


# In[75]:


stockIndexDF.ix[tradingDates[:3]]


# <b>Using a single integer:</b>

# In[76]:


stockIndexDF.ix[0]


# <b>Using a list of integers:</b>

# In[77]:


stockIndexDF.ix[[0,2]]


# <b>Using an integer slice:</b>

# In[78]:


stockIndexDF.ix[1:3]


# <b>Using a boolean array:</b>

# In[79]:


stockIndexDF.ix[stockIndexDF['Russell 2000']>1100]


# <h2>Multi-Indexing</h2>

# <b>Read stock index data:</b>

# In[81]:


sharesIndexDataDF=pd.read_csv('./data/stock_index_prices.csv')


# In[82]:


sharesIndexDataDF


# <b>Create a MultiIndex :</b>

# In[83]:


sharesIndexDF=sharesIndexDataDF.set_index(['TradingDate','PriceType'])


# In[84]:


mIndex=sharesIndexDF.index; mIndex


# In[85]:


sharesIndexDF


# <b>Apply get_level_values function:</b>

# In[86]:


mIndex.get_level_values(0)


# In[87]:


mIndex.get_level_values(1)


# In[88]:


mIndex.get_level_values(2)


# <b>Hierarchical indexing with a multi-indexed DataFrame:</b>

# In[89]:


sharesIndexDF.ix['2014/02/21']


# In[90]:


sharesIndexDF.ix['2014/02/21','open']


# <b>Slice using a multi-index:</b>

# In[91]:


sharesIndexDF.ix['2014/02/21':'2014/02/24']


# <b>Try slicing at a lower level:</b>

# In[92]:


sharesIndexDF.ix[('2014/02/21','open'):('2014/02/24','open')]


# Sort first before slicing with a MultiIndex:

# In[93]:


sharesIndexDF.sortlevel(0).ix[('2014/02/21','open'):('2014/02/24','open')]


# In[94]:


sharesIndexDF.sortlevel(0).ix[('2014/02/21','close'):('2014/02/24','close')]


# <b>Pass list of tuples:</b>

# In[96]:


sharesIndexDF.sortlevel(0).ix[[('2014/02/21','open'),('2014/02/24','open')]]


# <b>Use of the swaplevel function:</b>

# In[98]:


swappedDF=sharesIndexDF[:7].swaplevel(0, 1, axis=0)
swappedDF


# In[99]:


reorderedDF=sharesIndexDF[:7].reorder_levels(['PriceType', 
                                                      'TradingDate'], 
                                                       axis=0)
reorderedDF


# <h2>Cross-sections</h2>

# <b>xs( ) method</b>

# In[102]:


sharesIndexDF.xs('open',level='PriceType')


# <b>swaplevel( ) alternative:</b>

# In[103]:


sharesIndexDF.swaplevel(0, 1, axis=0).ix['open']


# <h1>Boolean Indexing</h2>

# <B>Trading dates for which NASD closed above 4300:</b>

# In[116]:


sharesIndexDataDF


# In[119]:


sharesIndexDataDF.ix[(sharesIndexDataDF['PriceType']=='close') &                      (sharesIndexDataDF['Nasdaq']>4300) ]


# In[120]:


highSelection=sharesIndexDataDF['PriceType']=='high'
NasdaqHigh=sharesIndexDataDF['Nasdaq']<4300
sharesIndexDataDF.ix[highSelection & NasdaqHigh]


# <h2>isin, any all methods</h2>

# In[121]:


stockSeries=pd.Series(['NFLX','AMZN','GOOG','FB','TWTR'])
stockSeries.isin(['AMZN','FB'])


# In[122]:


stockSeries[stockSeries.isin(['AMZN','FB'])]


# In[131]:


australianMammals = {'kangaroo': {'Subclass':'marsupial', 
                              'Origin':'native'},
               'flying fox' : {'Subclass':'placental', 
                               'Origin':'native'},              
               'black rat': {'Subclass':'placental', 
                             'Origin':'invasive'},
               'platypus' : {'Subclass':'monotreme', 
                             'Origin':'native'},
               'wallaby' :  {'Subclass':'marsupial', 
                             'Origin':'native'},
        'palm squirrel' : {'Subclass':'placental', 
                           'Origin':'invasive'},
        'anteater':     {'Subclass':'monotreme', 
                         'Origin':'native'},
        'koala':        {'Subclass':'marsupial', 
                         'Origin':'native'}
}



# In[132]:


ozzieMammalsDF=pd.DataFrame(australianMammals)


# In[133]:


aussieMammalsDF=ozzieMammalsDF.T; aussieMammalsDF


# In[134]:


aussieMammalsDF.isin({'Subclass':['marsupial'],'Origin':['native']})


# In[137]:


nativeMarsupials={'Subclass':['marsupial'],
                            'Origin':['native']}


# In[142]:


nativeMarsupialMask=aussieMammalsDF.isin(nativeMarsupials).all(1)
aussieMammalsDF[nativeMarsupialMask]


# <h2>where() method</h2>

# In[143]:


np.random.seed(100)
normvals=pd.Series([np.random.normal() for i in np.arange(10)])
normvals


# <b>Difference between using where() and standard boolean as filter on Series object</b>

# In[144]:


normvals[normvals>0]


# In[145]:


normvals.where(normvals>0)


# <b>No Difference between using where() and standard boolean as filter on Pandas object</b>

# In[146]:


np.random.seed(100) 
normDF=pd.DataFrame([[round(np.random.normal(),3) for i in np.arange(5)] for j in range(3)], 
             columns=['0','30','60','90','120'])
normDF


# In[147]:


normDF[normDF>0]


# In[148]:


normDF.where(normDF>0)


# <b>mask() is inverse of where()</b>

# In[149]:


normDF.mask(normDF>0)


# <h2>Operations on Indexes</h2>

# <b>Read in stock index data</b>

# In[150]:


stockIndexDataDF=pd.read_csv('./data/stock_index_data.csv')


# In[151]:


stockIndexDataDF


# <b>Set the index of DataFrame to the TradingDate using set_index(..)</b>

# In[152]:


stockIndexDF=stockIndexDataDF.set_index('TradingDate')


# In[153]:


stockIndexDF


# <b>reset_index reverses set_index:</b>

# In[154]:


stockIndexDF.reset_index()


# This concludes the chapter. 
