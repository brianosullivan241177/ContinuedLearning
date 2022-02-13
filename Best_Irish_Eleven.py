
import pandas as pd

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project_Final/Modified/players_21_22.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality_name','potential','international_reputation',
                                    'goalkeeping_handling','defending_sliding_tackle','passing','defending','skill_long_passing',
                                    'power_strength','dribbling','pace','movement_agility'])
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

Irish_Players_RF_DF['Right_fullback_mean']=Irish_Players_RF_DF['defending_sliding_tackle'] \
                                  + Irish_Players_RF_DF['passing'] + Irish_Players_RF_DF['defending'] + \
                                  Irish_Players_RF_DF['skill_long_passing'] + Irish_Players_RF_DF['power_strength']
Irish_Players_RF_DF


def Country(x):
    def findminmax(col):
        work = Irish_Players_RF_DF[col].idxmax()
        work_df = pd.DataFrame(Irish_Players_RF_DF.loc[work])
        return work_df
    return Irish_Players_RF_DF[Irish_Players_RF_DF['nationality_name'] == x ][['Right_fullback_mean', 'short_name']]\
        .sort_values(by=['Right_fullback_mean'],ascending=False)

Country1 = Country("Republic of Ireland")
print(Country1)
Rightfullback1=Country1.iloc[0][1]
print("The right fullback one is :", Rightfullback1)
Rightfullback2=Country1.iloc[1][1]
print("The right fullback two is :", Rightfullback2)


# Left full back
Irish_Players_LF_DF['Left_fullback_mean']=Irish_Players_RF_DF['defending_sliding_tackle'] \
                                  + Irish_Players_RF_DF['passing'] + Irish_Players_RF_DF['defending'] + \
                                  Irish_Players_RF_DF['skill_long_passing'] + Irish_Players_RF_DF['power_strength']
Irish_Players_LF_DF
def Country(x):
    def findminmax(col):
        work = Irish_Players_LF_DF[col].idxmax()
        work_df = pd.DataFrame(Irish_Players_LF_DF.loc[work])
        return work_df
    return Irish_Players_LF_DF[Irish_Players_LF_DF['nationality_name'] == x ][['Left_fullback_mean', 'short_name']]\
        .sort_values(by=['Left_fullback_mean'],ascending=False)

Country1 = Country("Republic of Ireland")
print(Country1)
Leftfullback1=Country1.iloc[0][1]
print("The Left fullback one is :", Leftfullback1)
Leftfullback2=Country1.iloc[1][1]
print("The Left fullback two is :", Leftfullback2)

print(Irish_Players_RF_DF.head())

# Excludes the right full back from being picked in midfield
Excludealreadypicked = Irish_Players_RF_DF.drop(Irish_Players_RF_DF[Irish_Players_RF_DF['short_name']==Rightfullback2].index, inplace = True)

print(Irish_Players_RF_DF.head())



