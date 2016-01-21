from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

dataset = datasets.load_iris()

model = DecisionTreeClassifier()

# Perform the machine learning steps- fit and predict
model.fit(dataset.data, dataset.target)
predicted = model.predict(dataset.data)
print(predicted)

expected = dataset.target
print(metrics.accuracy_score(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
