import pandas as pd

df = pd.read_csv("hospital_data.txt",delimiter="|")
#If wanted to read data from sql tables
# df = pd.read_sql_table('hospital_data', con=engine)  

# below loop will generate result_df based on Country column
# and prepare .txt file based on different countries 
for cname in df["Country"]:
    result_df = df[df["Country"] == cname]
    result_df.to_csv("Table_{}.txt".format(cname), sep="|", index=False)
    
# If wanted to write data to sql table.
#     result_df.to_sql(con=engine, name="Table_{}".format(cname),if_exists='append',index=False)