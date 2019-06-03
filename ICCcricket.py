import pandas as pd
import numpy as np

final_df = pd.DataFrame()
for i in np.arange(2):
    url = "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;page="+str(i)+";spanmin1=01+Jan+2007;spanval1=span;template=results;type=aggregate"
    df = pd.read_html(url)[2]
    final_df = pd.concat([final_df, df])

final_df.drop(columns= 'Unnamed: 10' ,axis=1,inplace=True)
final_df.columns = ['Span','Matches_Played','Matches_Won',
                    'Matches_Tied','Matches_No_Result',
                    'Runs_Scored','Wickets_Taken','Balls_Bowled',
                    'Avg_Runs/Wkt','Avg_Runs/Over']
final_df.drop_duplicates(subset ="Span", keep = "first", inplace = True)
final_df= final_df.reset_index(drop=True)

final_df.to_excel("ODI_Overall.xlsx")


print(final_df.columns)



import pandas as pd
dfs = []
i = 0
while i < 26:
    url = (
        "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;page="+str(i)+";spanmin1=01+Jan+2007;spanval1=span;template=results;type=bowling"
    )
    dframe = pd.read_html(url, attrs={"class": "engineTable"})
    dfs.append(dframe[2].drop(columns="Unnamed: 14"))
    i = i + 1

result = pd.concat(dfs)
result = result.reset_index(drop=True)
print(result)