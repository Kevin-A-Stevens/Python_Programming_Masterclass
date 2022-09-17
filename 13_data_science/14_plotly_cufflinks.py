"""
pip3 install plotly
pip3 install cufflinks
pip3 install chart_studio
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import __version__
import cufflinks as cf
import chart_studio
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

# print(__version__)

init_notebook_mode(connected=True)
cf.go_offline()

# DATA
df = pd.DataFrame(np.random.rand(100,4),columns='A B C D'.split())
print(df.head())

df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
print(df2)

plt.show(df.iplot(kind='scatter',x='A',y='B',mode='markers'))






