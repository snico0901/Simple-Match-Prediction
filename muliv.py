import pandas as pd

def load_dataset():
    data = pd.read_csv('muvliv.csv')
    dataset = data[['HomeTeam','AwayTeam','FTHG','FTAG','FTR']]

    return dataset

dataset = load_dataset()

manU = 0
lpool = 0
draw = 0

home = dataset[['HomeTeam']].values.tolist()
result = dataset[['FTR']].values.tolist()



for i in range(len(dataset)):
    if home[i] == ['Man United'] and result[i] == ['H']:
        manU+=1
    elif home[i] == ['Man United'] and result[i] == ['A']:
        lpool+=1
    elif home[i] == ['Liverpool'] and result[i] == ['H']:
        lpool+=1
    elif home[i] == ['Liverpool'] and result[i] == ['A']:
        manU+=1
    elif home[i] == ['Man United'] or home[i] == ['Liverpool'] and result[i] == ['D']:
        draw+=1


chanceMUWin = (manU/(manU+lpool+draw))*100
chanceLivWin = (lpool/(manU+lpool+draw))*100
chanceDraw = (draw/(manU+lpool+draw))*100


print("Manchester United vs Liverpool Prediction")
print("(based on historical data)")
print("Manchester United win: {} %".format(chanceMUWin))
print("Liverpool Win: {} %".format(chanceLivWin))
print("Match Draw: {} %".format(chanceDraw))