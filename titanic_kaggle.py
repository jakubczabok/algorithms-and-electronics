# This is my solution to titanic kaggle competition https://www.kaggle.com/competitions/titanic/overview

import pandas as pd

data=pd.read_csv("/train.csv")
test=pd.read_csv("/test.csv")
test_ids=test["PassengerId"]

# finding lenght of name, people with longer names usually had some important titles and where more likely to survive
def lenOfName(data):
    for i in range(len(data)):
      data.Name[i]=len(data.Name[i])
    return data

# dropping less important columns and filling gaps in data with median
def clean(data):
    data=data.drop(["Ticket", "Cabin", "PassengerId"],axis=1)

    cols=["SibSp", "Parch", "Fare", "Age"]
    for col in cols:
        data[col].fillna(data[col].median(),inplace=True)

    data.Embarked.fillna("U",inplace=True)
    return data

data=lenOfName(data)
test=lenOfName(test)
data=clean(data)
test=clean(test)

from sklearn import preprocessing
le=preprocessing.LabelEncoder()
cols=["Sex", "Embarked"]
for col in cols:
    data[col]=le.fit_transform(data[col])
    test[col]=le.fit_transform(test[col])

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

y=data["Survived"]
x=data.drop("Survived",axis=1)

x_train, x_val, y_train, y_val=train_test_split(x,y,test_size=0.2,random_state=42)


clf=LogisticRegression(random_state=0,max_iter=10000).fit(x_train,y_train)
prediction=clf.predict(x_val)

from sklearn.metrics import accuracy_score

accuracy_score(y_val,prediction)

submission_preds=clf.predict(test)

df=pd.DataFrame({"PassengerId": test_ids.values,"Survived": submission_preds,})

df.to_csv("/content/submission.csv",index=False)
