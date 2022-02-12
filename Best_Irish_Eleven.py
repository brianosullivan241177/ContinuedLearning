
import pandas as pd

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project_Final/Modified/players_21_22.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality_name','potential','international_reputation',
                                    'goalkeeping_handling'])
print(FifaAll_Players_DF.head()) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data tyoes

Irish_Players_LF_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality_name == 'Republic of Ireland') &
                                      (FifaAll_Players_DF.preferred_foot == 'Left')]
print(Irish_Players_LF_DF.head())

Irish_Players_RF_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality_name == 'Republic of Ireland') &
                                      (FifaAll_Players_DF.preferred_foot == 'Right')]
print(Irish_Players_RF_DF.head())



def findminmax(col):
    top = Irish_Players_RF_DF[col].idxmax()
    top_df = pd.DataFrame(Irish_Players_RF_DF.loc[0])
    bottom = Irish_Players_RF_DF[col].idxmin()
    bottom_df = pd.DataFrame(Irish_Players_RF_DF.loc[1])
    info_df = pd.concat([top_df, bottom_df], axis=1)
    return info_df




def Country(x):
    def findminmax(col):
        work = Irish_Players_RF_DF[col].idxmax()
        work_df = pd.DataFrame(Irish_Players_RF_DF.loc[work])
        return work_df
    return Irish_Players_RF_DF[Irish_Players_RF_DF['nationality_name'] == x ][['goalkeeping_handling', 'short_name']].sort_values\
        (by=['goalkeeping_handling'],ascending=False)


Country1 = Country("Republic of Ireland")
print(Country1)
goalkeeper = Country1.iloc[0][1]
print("The goalkeeper is :", goalkeeper)