import pandas as pd
finaldf=pd.read_csv('final.csv')
finaldf=finaldf.sort_values('weighted_rating',ascending=False)
output=finaldf[['original_title','release_date','poster_link','runtime','weighted_rating']].head(10)
print(output)
