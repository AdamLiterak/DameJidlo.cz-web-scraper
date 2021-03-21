#adding all the datasets into one set and adjusting item price
import pandas as pd

#fce that returns price as a number
def adjust(s):
    text = []
    for i in s:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]:
            text.append(i)
        else:
            pass
    x = "".join(text)
    return float(x.replace(",","."))


df1 = pd.read_csv("praha_restaurants_full_set.csv")
df2 = pd.read_csv("brno_restaurants_full_set.csv")
df3 = pd.read_csv("ostrava_restaurants_full_set.csv")
df4 = pd.read_csv("plzen_restaurants_full_set.csv")
df5 = pd.read_csv("olomouc_restaurants_full_set.csv")
df6 = pd.read_csv("pardubice_restaurants_full_set.csv")
df7 = pd.read_csv("hradec_kralove_restaurants_full_set.csv")
df8 = pd.read_csv("ceske_budejovice_restaurants_full_set.csv")
df9 = pd.read_csv("usti_nad_labem_restaurants_full_set.csv")
df10 = pd.read_csv("liberec_restaurants_full_set.csv")

df_all = df1.append(df2)
df_all = df_all.append(df3)
df_all = df_all.append(df4)
df_all = df_all.append(df5)
df_all = df_all.append(df6)
df_all = df_all.append(df7)
df_all = df_all.append(df8)
df_all = df_all.append(df9)
df_all = df_all.append(df10)

df_all['item_price'] = df_all.item_price.apply(adjust)

df_all.to_csv("damejidlo_dataset_final")
