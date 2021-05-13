import pandas as pd

data={
    'apples':[3,2,7,9],
    'oranges':[6,0,5,1]}

purchase=pd.DataFrame(data, index=['june','robert','lily','david'])

# with open('myfile.csv','w') as f:
    # purchase.to_csv(f)
