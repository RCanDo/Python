
# coding: utf-8

# <title>pandas Data Structures</title>

# <h1>pandas Data Structures</h1>

# In[2]:


import numpy as np
import pandas as pd


# <h2>NumPy array creation via numpy.array</h2>

# In[3]:


ar1 = np.array([0,1,2,3]) # 1 dimensional array


# In[4]:


ar2=np.array([[0,3,5],[2,8,7]]) # 2D array


# In[5]:


ar1


# In[6]:


ar2


# <b>Shape of the array</b>

# In[7]:


ar2.shape


# <b>Number of dimensions</b>

# In[8]:


ar2.ndim


# <h2>NumPy array creation via numpy.arange</h2>

# In[10]:


ar3=np.arange(12);ar3


# In[11]:


# start, end (exclusive)
ar4=np.arange(3,10,3);ar4


# <h2>NumPy array creation via numpy.linspace</h2>

# In[12]:


# args - start element,end element, number of elements
ar5=np.linspace(0,2.0/3,4); ar5


# <h2>NumPy array via various other functions</h2>

# <h3>numpy.ones</h3>

# In[13]:


# Produces 2x3x2 array of 1's.
ar7=np.ones((2,3,2)); ar7


# <h3>numpy.zeros</h3>

# In[14]:


# Produce 4x2 array of zeros.
ar8=np.zeros((4,2));ar8


# <h3>numpy.eye</h3>

# In[15]:


# Produces identity matrix
ar9 = np.eye(3);ar9


# In[16]:


f_ar = np.array([3,-2,8.18])
f_ar


# <h3>numpy.diag</h3>

# In[17]:


# Create diagonal array
ar10=np.diag((2,1,4,6));ar10


# <h3>numpy.random.rand</h3>

# In[24]:


# Using the rand, randn functions
# rand(m) produces m random numbers uniformly distributed on (0, 1)
#np.random.seed(100) # Set seed
ar11=np.random.rand(5); ar11


# In[26]:


np.random.rand(3,3)


# In[27]:


# randn(m) produces m normally distributed (Gaussian) random numbers
ar12=np.random.randn(5); ar12


# <h3>numpy.empty</h3>

# In[30]:


ar13=np.empty((3,2)); ar13


# <h3>numpy.tile</h3>

# In[31]:


np.array([[1,2],[6,7]])


# In[32]:


np.tile(np.array([[1,2],[6,7]]),3)


# In[33]:


np.tile(np.array([[1,2],[6,7]]),(2,2))


# <h2>NumPy datatypes</h2>

# In[34]:


ar=np.array([2,-1,6,3],dtype='float'); ar


# In[35]:


ar.dtype


# In[36]:


ar=np.array([2,4,6,8]); ar.dtype


# In[37]:


ar=np.array([2.,4,6,8]); ar.dtype


# In[38]:


sar=np.array(['Goodbye','Welcome','Tata','Goodnight']); sar.dtype


# In[39]:


bar=np.array([True, False, True]); bar.dtype


# In[40]:


f_ar = np.array([3,-2,8.18])
f_ar


# In[41]:


f_ar.astype(int)


# <h2>NumPy indexing and slicing</h2>

# In[43]:


# print entire array, element 0, element 1, last element.
ar = np.arange(5); print(ar); ar[0], ar[1], ar[-1]


# In[44]:


# 2nd, last and 1st elements
ar=np.arange(5); ar[1], ar[-1], ar[0]


# In[45]:


# Reverse array using ::-1 idiom
ar=np.arange(5); ar[::-1]


# In[46]:


# Index multi-dimensional array


# In[47]:


ar = np.array([[2,3,4],[9,8,7],[11,12,13]]); ar


# In[48]:


ar[1,1]


# In[49]:


ar[1,1]=5; ar


# In[50]:


ar[2]


# In[51]:


ar[2,:]


# In[52]:


ar[:,1]


# In[53]:


ar = np.array([0,1,2])


# In[54]:


ar[5]


# <h2>Array slicing</h2>

# In[55]:


ar=2*np.arange(6); ar


# In[56]:


ar[1:5:2]


# In[57]:


ar[1:6:2]


# In[58]:


ar[:4]


# In[59]:


ar[4:]


# In[60]:


ar[::3]


# In[61]:


ar


# In[62]:


ar[:3]=1;ar


# In[63]:


ar[2:]=np.ones(4);ar


# <h2>Array masking</h2>

# In[73]:


np.random.seed(10)
ar=np.random.randint(0,25,10); ar


# In[74]:


evenMask=(ar % 2==0); evenMask


# In[75]:


evenNums=ar[evenMask]; evenNums


# In[76]:


ar[(ar%2==0)]


# In[78]:


ar=np.array(['Hungary','Nigeria',
'Guatemala','','Poland','','Japan']); ar


# In[79]:


ar[ar=='']='USA'; ar


# In[80]:


ar=11*np.arange(0,10); ar


# In[81]:


ar[[1,3,4,2,7]]


# In[82]:


ar[1,3,4,2,7]


# In[83]:


ar[[1,3]]=50; ar


# <h2>Complex indexing</h2>

# In[84]:


ar=np.arange(15); ar


# In[85]:


ar2=np.arange(0,-10,-1); ar2


# In[86]:


ar2[::-1]


# In[87]:


np.arange(-10,0)


# In[88]:


ar[:10]=ar2; ar


# <h2>Copies and views</h2>

# <b>Modifying view modifies original array</b>

# In[89]:


ar1=np.arange(12); ar1


# In[90]:


ar2=ar1[::2]; ar2


# In[91]:


ar2[1]=-1; ar1


# <b>Use np.copy to force a copy</b>

# In[92]:


ar=np.arange(8);ar


# In[93]:


arc=ar[:3].copy(); arc


# In[94]:


arc[0]=-1; arc


# In[95]:


ar


# <h1>Operations</h1>
# <h2>Basic Operations</h2>

# <b>Element-wise</b>

# In[96]:


ar=np.arange(0,7)*5; ar


# In[97]:


ar=np.arange(5) ** 4 ; ar


# In[98]:


ar ** 0.5


# In[99]:


ar=3+np.arange(0, 30,3); ar


# In[100]:


ar2=np.arange(1,11); ar2


# In[101]:


ar-ar2


# In[102]:


ar/ar2


# In[103]:


ar*ar2


# <b>NumPy faster for this than Python</b>

# In[104]:


ar=np.arange(1000)
get_ipython().magic('timeit ar**3')


# In[105]:


ar=range(1000)
get_ipython().magic('timeit [ar[i]**3 for i in ar]')


# <b>Array multiplication is element wise</b>

# In[106]:


ar=np.array([[1,1],[1,1]]); ar


# In[107]:


ar2=np.array([[2,2],[2,2]]); ar2


# In[108]:


ar.dot(ar2)


# In[109]:


ar*ar2


# <b>Comparison and logical operations are also elememt-wise</b>

# In[110]:


ar=np.arange(1,5); ar


# In[111]:


ar2=np.arange(5,1,-1);ar2


# In[112]:


ar < ar2


# In[113]:


l1 = np.array([True,False,True,False])
l2 = np.array([False,False,True, False])
np.logical_and(l1,l2)


# In[116]:


l1 and l2


# In[115]:


[True,False,True,False] and [False,False,True, False]


# <b>Other operations are also element-wise</b>

# In[117]:


ar=np.array([np.pi, np.pi/2]); np.sin(ar)


# <b>For element-wise operations, the 2 arrays must be the same shape else an error results</b>

# In[118]:


ar=np.arange(0,6); ar


# In[119]:


ar2=np.arange(0,8); ar2


# In[120]:


ar*ar2


# <b>NumPy arrays can be transposed</b>

# In[121]:


ar=np.array([[1,2,3],[4,5,6]]); ar


# In[122]:


ar.T


# In[123]:


np.transpose(ar)


# <b>Compare arrays not element-wise but array-wise</b>

# In[124]:


ar=np.arange(0,6)
ar2=np.array([0,1,2,3,4,5])
np.array_equal(ar, ar2)


# In[125]:


np.all(ar==ar2)


# <h1>Reduction Operations</h1>

# In[126]:


ar=np.arange(1,5)
ar.prod()


# In[127]:


ar=np.array([np.arange(1,6),np.arange(1,6)]);ar


# In[128]:


#Columns
np.prod(ar,axis=0)


# In[129]:


#Rows
np.prod(ar,axis=1)


# In[130]:


ar=np.array([[2,3,4],[5,6,7],[8,9,10]]); ar.sum()


# In[131]:


ar.mean()


# In[132]:


np.median(ar)


# <h1>Statistical operators</h1>

# In[134]:


np.random.seed(10)
ar=np.random.randint(0,10, size=(4,5));ar


# In[124]:


ar.mean()


# In[135]:


ar.std()


# In[136]:


ar.var(axis=0) #across rows


# In[137]:


ar.cumsum()


# In[138]:


ar.cumsum(axis=0)


# <h1>Logical operators</h1>

# In[139]:


np.random.seed(100)
ar=np.random.randint(1,10, size=(4,4));ar


# In[140]:


(ar%7)==0


# In[141]:


np.any((ar%7)==0)


# In[142]:


np.all(ar<11)


# <h1>Broadcasting</h1>

# In[143]:


ar=np.ones([3,2]); ar


# In[144]:


ar2=np.array([2,3]); ar2


# In[145]:


ar+ar2


# <b>Broadcasting works across dimensions</b>

# In[146]:


ar=np.array([[23,24,25]]); ar


# In[147]:


ar.T


# In[137]:


ar.T+ar


# In[148]:


ar = np.array([[1,2,3]]); ar


# In[149]:


ar.T * ar


# <h1>Array shape manipulation<h1>
# <h2>Flattening a multi-dimensional array<h2>

# In[150]:


ar=np.array([np.arange(1,6), np.arange(10,15)]); ar


# In[151]:


ar.ravel()


# In[152]:


ar.T.ravel()


# <h2>Reshaping<h2>

# In[153]:


ar=np.arange(1,16);ar


# In[154]:


ar.reshape(3,5)


# In[155]:


ar


# <h2>Resizing</h2>

# In[156]:


ar=np.arange(5); ar.resize((8,));ar


# In[157]:


ar=np.arange(5);
ar


# <b>resize() only works if no otehr references to array, else error</b>

# In[158]:


ar2=ar


# In[159]:


ar.resize((8,));


# <b>Workaround is to use numpy.ndarray.resize() instead</b>

# In[160]:


np.resize(ar,(8,))


# In[161]:


ar


# <h2>Adding a dimension</h2>

# In[162]:


ar=np.array([14,15,16]); ar.shape


# In[163]:


ar


# In[164]:


ar=ar[:, np.newaxis]; ar.shape


# In[165]:


ar


# In[166]:


ar=np.array([14,15,16]); ar


# In[167]:


ar[np.newaxis, :]


# In[168]:


ar[np.newaxis, :,np.newaxis]


# <h1>Array sorting</h1>

# <b>Along y-axis<b>

# In[169]:


ar=np.array([[3,2],[10,-1]])
ar


# In[170]:


ar.sort(axis=1)
ar


# <b>Along x-axis</b>

# In[171]:


ar=np.array([[3,2],[10,-1]])
ar


# In[172]:


ar.sort(axis=0)
ar


# <h1>Data structures in pandas<h1>

# <h1>Series</h1>

# <h2>Series creation</h2>

# <h2>Using numpy.ndarray</h2>

# In[174]:


np.random.seed(100)
ser=pd.Series(np.random.rand(7)); ser


# In[175]:


import calendar as cal
monthNames=[cal.month_name[i] for i in np.arange(1,6)]
months=pd.Series(np.arange(1,6),index=monthNames);months


# In[176]:


months.index


# In[179]:


months.values


# In[180]:


months['March']


# In[181]:


months[2]


# In[184]:


months[['March','April']]


# In[185]:


months[monthNames[1:3]]


# <h2>Using Python dictionary</h2>

# In[186]:


currDict={'US' : 'dollar', 'UK' : 'pound',
'Germany': 'euro', 'Mexico':'peso',
'Nigeria':'naira',
'China':'yuan', 'Japan':'yen'}
currSeries=pd.Series(currDict); currSeries


# In[191]:


currSeries.name


# In[187]:


stockPrices = {'GOOG':1180.97,'FB':62.57,
'TWTR': 64.50, 'AMZN':358.69,
'AAPL':500.6}
stockPriceSeries=pd.Series(stockPrices,
index=['GOOG','FB','YHOO',
'TWTR','AMZN','AAPL'],
name='stockPrices')
stockPriceSeries


# <h2>Using scalar values</h2>

# In[192]:


dogSeries=pd.Series('chihuahua', index=['breed','countryOfOrigin', 'name', 'gender'])
dogSeries


# In[193]:


dogSeries=pd.Series('pekingese'); dogSeries


# In[194]:


type(dogSeries)


# In[196]:


ss = pd.Series(['a','b','c']); ss


# In[201]:


ss = pd.Series(['a','b','c'],index = ['p','q','r']); ss


# In[202]:


ss[['p','q']]


# <h1>Operations on Series</h1>

# <h2>Assignment</h2>

# In[203]:


currDict['China']


# In[204]:


stockPriceSeries['GOOG']=1200.0
stockPriceSeries


# <b>KeyError is raised if you try to retrieve a missing label</b>

# In[205]:


stockPriceSeries['MSFT']


# <b>Use get() to avoid this</b>

# In[206]:


stockPriceSeries.get('MSFT',np.NaN)


# <h2>Slicing</h2>

# In[207]:


stockPriceSeries[:4]


# In[208]:


stockPriceSeries[stockPriceSeries > 100]



# <h2>Other operations</h2>

# In[209]:


np.mean(stockPriceSeries)


# In[210]:


np.std(stockPriceSeries)


# <b>Element-wise operations</b>

# In[211]:


ser


# In[212]:


ser*ser


# In[213]:


np.sqrt(ser)


# <b>Data ia automatically aligned on basis of the label</b>

# In[214]:


ser[1:]


# In[215]:


ser[1:] + ser[:-2]


# <h1>DataFrame</h1>
# 

# <h1>DataFrame Creation</h1>
# 

# <h2>Using dictionaries of Series</h2>

# In[216]:


stockSummaries={'AMZN': pd.Series([346.15,0.59,459,0.52,589.8,158.88],
                                  index=['Closing price','EPS','Shares Outstanding(M)',
                                         'Beta', 'P/E','Market Cap(B)']),
                'GOOG': pd.Series([1133.43,36.05,335.83,0.87,31.44,380.64],
                                  index=['Closing price','EPS','Shares Outstanding(M)',
                                         'Beta','P/E','Market Cap(B)']),
                  'FB': pd.Series([61.48,0.59,2450,104.93,150.92],
                                  index=['Closing price','EPS','Shares Outstanding(M)',
                                         'P/E', 'Market Cap(B)']),
                'YHOO': pd.Series([34.90,1.27,1010,27.48,0.66,35.36],
                                  index=['Closing price','EPS','Shares Outstanding(M)',
                                         'P/E','Beta', 'Market Cap(B)']),
               'TWTR':pd.Series([65.25,-0.3,555.2,36.23],
                                  index=['Closing price','EPS','Shares Outstanding(M)',
                                         'Market Cap(B)']),
               'AAPL':pd.Series([501.53,40.32,892.45,12.44,447.59,0.84],
                                  index=['Closing price','EPS','Shares Outstanding(M)','P/E',
                                         'Market Cap(B)','Beta'])}


# In[217]:


stockDF=pd.DataFrame(stockSummaries); stockDF


# In[218]:


stockDF=pd.DataFrame(stockSummaries,
index=['Closing price','EPS',
       'Shares Outstanding(M)',
    'P/E', 'Market Cap(B)','Beta']);stockDF


# In[219]:


stockDF=pd.DataFrame(stockSummaries,
        index=['Closing price','EPS',
               'Shares Outstanding(M)',
               'P/E', 'Market Cap(B)','Beta'],
        columns=['FB','TWTR','SCNW'])
stockDF


# In[220]:


stockDF.index


# In[221]:


stockDF.columns


# <h2>Using a dictionary of ndarrays/lists</h2>

# In[222]:


algos={'search':['DFS','BFS','Binary Search','Linear','ShortestPath (Djikstra)'],
      'sorting': ['Quicksort','Mergesort', 'Heapsort','Bubble Sort', 'Insertion Sort'],
      'machine learning':['RandomForest','K Nearest Neighbor','Logistic Regression',
                          'K-Means Clustering','Linear Regression']}
algoDF=pd.DataFrame(algos); algoDF


# In[223]:


pd.DataFrame(algos,index=['algo_1','algo_2','algo_3','algo_4','algo_5'])


# <h2>Using a structured array</h2>

# In[228]:


memberData = np.zeros((4,),
             dtype=[('Name','a15'),
                    ('Age','i4'),
                   ('Weight','f4')])
memberData


# In[225]:


memberData[:] = [('Sanjeev',37,162.4),
                 ('Yingluck',45,137.8),
                 ('Emeka',28,153.2),
                 ('Amy',67,101.3)]
memberData


# In[226]:


memberDF=pd.DataFrame(memberData)
memberDF


# In[227]:


pd.DataFrame(memberData, index=['a','b','c','d'])


# <h2>Using a Series structure</h2>

# In[229]:


currSeries.name='currency'
pd.DataFrame(currSeries)


# <h1>DataFrame Operations</h1>

# <h2>Selection</h2>

# In[230]:


memberDF['Name']


# <h2>Assignment</h2>

# In[231]:


memberDF['Height']=60;memberDF


# <h2>Deletion</h2>

# In[232]:


del memberDF['Height']; memberDF


# In[233]:


memberDF['BloodType']='O'
bloodType=memberDF.pop('BloodType'); bloodType


# In[234]:


memberDF


# <h2>Insertion</h2>

# In[235]:


memberDF.insert(2,'isSenior',memberDF['Age']>60);
memberDF


# In[236]:


memberDF.insert(3,'isLight',memberDF['Weight']<150); memberDF


# <h2>Alignment</h2>

# In[237]:


ore1DF=pd.DataFrame(np.array([[20,35,25,20],
                              [11,28,32,29]]),
                    columns=['iron','magnesium',
                             'copper','silver'])
ore2DF=pd.DataFrame(np.array([[14,34,26,26],
                              [33,19,25,23]]),
                    columns=['iron','magnesium',
                            'gold','silver'])
ore1DF+ore2DF


# In[238]:


ore1DF + pd.Series([25,25,25,25],
index=['iron','magnesium','copper','silver'])


# <h2>Other mathematical operations</h2>

# In[239]:


np.sqrt(ore1DF)


# <h1>Panel</h1>
# <h1>Panel Creation</h1>

# <h2>Using 3D NumPy array with axis labels</h2>

# In[240]:


stockData=np.array([[[63.03,61.48,75],
                     [62.05,62.75,46],
                     [62.74,62.19,53]],
                   [[411.90, 404.38, 2.9],
                    [405.45, 405.91, 2.6],
                    [403.15, 404.42, 2.4]]])
stockData


# In[241]:


stockHistoricalPrices = pd.Panel(stockData,
                                 items=['FB', 'NFLX'],
                                 major_axis=pd.date_range('2/3/2014',periods=3),
                                 minor_axis=['open price', 'closing price', 'volume'])
stockHistoricalPrices


# <h2>Using a Python dictionary of DataFrame objects</h2>

# In[242]:


USData=pd.DataFrame(np.array([[249.62 , 8900],
                              [282.16,12680],
                              [309.35,14940]]),
                    columns=['Population(M)','GDP($B)'],
                    index=[1990,2000,2010])
USData


# In[243]:


ChinaData=pd.DataFrame(np.array([[1133.68, 390.28],
                                 [1266.83,1198.48],
                                 [1339.72, 6988.47]]),
                       columns=['Population(M)','GDP($B)'],
                       index=[1990,2000,2010])
ChinaData


# In[244]:


US_ChinaData={'US' : USData,
              'China': ChinaData}
pd.Panel(US_ChinaData)


# <h2>Using the DataFrame.to_panel method</h2>

# In[245]:


mIdx = pd.MultiIndex(levels=[['US', 'China'],
                             [1990,2000, 2010]],
                     labels=[[1,1,1,0,0,0],[0,1,2,0,1,2]])
mIdx


# In[246]:


ChinaUSDF = pd.DataFrame({'Population(M)' : [1133.68, 1266.83, 1339.72, 
                                                        249.62, 282.16,309.35], 
                                     'GDB($B)': [390.28, 1198.48, 6988.47, 8900,12680,14940]}, 
                          index=mIdx)
ChinaUSDF


# In[247]:


ChinaUSDF.to_panel()

