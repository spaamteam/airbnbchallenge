from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import cross_validation as cv

dataset = datasets.load_iris()

X_train, X_test, y_train, y_test = cv.train_test_split(dataset.data, dataset.target, test_size=0.4, random_state=0)

model = DecisionTreeClassifier()

# Perform the machine learning steps- fit and predict

#model.fit(dataset.data, dataset.target)
model.fit(X_train, y_train)

#predicted = model.predict(dataset.data)
predicted = model.predict(X_test)
print(predicted)

#expected = dataset.target
expected = y_test
print(metrics.accuracy_score(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
