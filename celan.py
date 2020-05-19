import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import sklearn
from pandas import DataFrame as df
import simplejson as json


def predict_regLineaire(equipe_param,annee_param):
    #load the file

    data_file = "DATAFACTORY1.xlsx"
    labelencoder = LabelEncoder()
    data = pd.read_excel(data_file)
    #get special column (equipe,annee de saisie,date de saisie et equivalent celan)
    post_data = data.iloc[:, [2, 3, 10, 22]].dropna()
    post_data.columns = ['equipe', 'annee_saisie','mois', 'eq_celan']
    #extract month from the date (date de saisie => mois de saisie)
    post_data['mois']=pd.DatetimeIndex(post_data.mois).month
    labelencoder.fit(post_data['equipe'])
    post_data['equipe']=labelencoder.transform(post_data['equipe'])

    result = {}
    #fill dict with data from post_data to have the sum of equivalent celan for each equipe and for each month of the year
    for index, row in post_data.iterrows():
        team = int(row.equipe)
        year = int(row.annee_saisie)
        month = int(row.mois)
        if result.get(team) == None:
            result[team] = {}
        if result[team].get(year) == None:
            result[team][year] = {}
        if result[team][year].get(month) == None:
            result[team][year][month] = row.eq_celan
        else:
            result[team][year][month] = result[team][year][month] + row.eq_celan

    #from dict to dataFrame (equipe, annee de saisie, mois de saisie et somme d equivalent celan)
    res_eq=[]
    res_annee=[]
    res_mois=[]
    res_som_celan=[]
    for eq in range(0,4):
        for annee in range(2013,2020):
            if(result[eq].get(annee)!= None):
                for mois in range(1,13):
                    if(result[eq][annee].get(mois)!= None):
                        res_eq.append(eq)
                        res_annee.append(annee)
                        res_mois.append(mois)
                        res_som_celan.append(result[eq][annee][mois])

    final_data = pd.DataFrame({'equipe': res_eq,'annee': res_annee,'mois': res_mois,'som_celan': res_som_celan})


    X = final_data.values[:, :-1]
    Y = final_data.values[:, -1]


    if(equipe_param=="AFD"):
        equi=0
    elif (equipe_param=="IDF"):
        equi=1
    elif (equipe_param=="PS1"):
        equi=2
    elif (equipe_param=="PS2"):
        equi=3

    an=annee_param

    # Create linear regression object
    model = LinearRegression()
    model.fit(X, Y)

    equipes=[]
    annees=[]
    moiss=[]
    res=[]


    #predict sum of celan for the equipe passed in params for the 12 months of the year passed in params
    for i in range(1,13):
        d = {'equipe': equi, 'annee_saisie': an,'mois':i}
        pred=pd.DataFrame(data=d,index=[0])
        celan_y_pred = model.predict(pred)
        equipes.append(equipe_param)
        annees.append(an)
        moiss.append(i)
        res.append(celan_y_pred)

    df1 = pd.DataFrame({'equipe':equipes,'annee':annees,'mois':moiss,'y_pred': res})
    #convert to a list (serialize with Json : list in python => array in Json)
    #the list => [[equipe,annee,mois,som_celan_predicted]]
    #df_list=json.dumps(df1.to_dict(orient='list'))
    df_list=df1.to_json(orient='records')
    return df_list
