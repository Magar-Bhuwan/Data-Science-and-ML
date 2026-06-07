import numpy as np


data = pd.DataFrame({
    "id":[1,3,5,7,9],
    "name":["John","Jane","Jennifer","Johan","Jeff"],
    "age":[25,-32,19,42,"55"],
    "gender" : ["M","M","Z","F","F"],
    "income":[400, 700, 300, np.nan, 600]
})