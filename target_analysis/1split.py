import numpy as np
import pandas as pd

DF = pd.read_csv(r'train.csv')
for val in DF.Asset_ID.unique():
    print(val)
    DF[DF.Asset_ID==val].sort_values(by=['timestamp'],ascending=True).to_csv(r'splitdata/Asset'+str(val)+'.csv',index=None)