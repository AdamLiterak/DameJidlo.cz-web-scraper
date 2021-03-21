import pandas as pd

#example list of lists
l = [["a",1,10],["b",1,11],["c",2,10]]

#creating a pandas df
df = pd.DataFrame({"city":[0],"restaurant":[0],"item":[0],"price":[0]})

print(df)

#loop to append values to the pandas df
for i in l:
    h = ["city","restaurant","item","price"]
    s = []
    s.append("praha")
    for j in i:
        s.append(j)
    #combines lists into a dictionary
    item_list = dict(zip(h,s))
    df = df.append(item_list, ignore_index=True)

print(df)