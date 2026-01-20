import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn.datasets import make_classification
from mlxtend.plotting import plot_decision_regions

X, y = make_classification(
    n_samples=100, 
    n_features=2, 
    n_informative=2, 
    n_redundant=0, 
    n_classes=2, 
    n_clusters_per_class=1, 
    random_state=41, 
    hypercube=False, 
    class_sep=10
)

p = Perceptron()
p.fit(X, y)


print("Weights (Coef):", p.coef_)
print("Bias (Intercept):", p.intercept_)

accuracy = p.score(X, y)
print("Accuracy score is", accuracy)

plt.figure(figsize=(8, 6))
plot_decision_regions(X, y, clf=p, legend=2)

plt.title('Perceptron Decision Boundary (Practical 1)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()