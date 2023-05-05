import numpy as np
from sklearn.datasets import make_blobs
from matplotlib.patches import Patch
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
from itertools import combinations
from sklearn.linear_model import LogisticRegression
le = LabelEncoder()

# for plotting decision region
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from mlxtend.plotting import plot_decision_regions

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score


# Logistic Regression and Newton Raphson 
class Newton_Raphson():
    def __init__(self, *kernel, **kernel_kwargs):
        self.kernel = kernel
        self.kernel_kwargs = kernel_kwargs
        self.beta_old = np.array([-5.49836039e-02,  6.80093332e-05])
        self.beta = np.array([1.01422606, 0.07874342])
        self.alpha = 0.5   
        self.reg = True

    def sigmoid(self, x: np.array):
        return 1/(1+np.exp(-x))

    def prob(self, X: np.array, beta: np.array):
        '''
        probability
        '''
        return np.array(self.sigmoid(X.dot(beta)))
        # return self.sigmoid(X.T @ beta)
        # return self.sigmoid(X @ beta)

    def Var(self, p: np.array):
        on_diag = p*(1-p)
        d = on_diag.reshape(-1)
        return np.diag(d)

    def Hessian(self, X: np.array, beta: np.array):
        '''
        print(f"X.T.shape {X.T.shape}")
        print(f"X.shape {X.shape}")
        print(f"VAR.shape {V.shape}")
        print(XV.shape)
        '''
        V = self.Var(self.prob(X,beta))
        XV = X.T @ V
        # result = np.dot(XV, X)
        result = XV @ X

        return result

    def update(self, y, X, beta):
        '''
        print(X.T.shape)
        print(y.shape)
        print(self.prob(X,beta).shape)
        '''
        grad = X.T @ (y-self.prob(X,beta))
        # no reguliazation
        if (self.reg):
            hessian = self.Hessian(X,beta)
            step = np.linalg.inv(self.Hessian(X,beta)) @ grad
        # reguliazation
        else:
            hessian = self.Hessian(X,beta) + np.eye(beta.shape[0])
            step = np.linalg.inv(hessian) @ grad
        # print(f"step: {step.shape}")
        step = self.alpha * step
        beta = beta + step 
        return beta

    def regress(self, y, X, max_iters = 1e1, tol=1e-8, converged=False):
        self.beta_old = np.array([1,1])
        self.beta = np.array([-5.4e-02,  6.8e-05]) 
        self.beta = self.beta.reshape(-1,1)
        self.beta_old = self.beta_old.reshape(-1,1)
        print(self.alpha)
        
        iter_count = 0 
        while not converged and (iter_count<max_iters):
            iter_count += 1
            # print(f"self.beta {self.beta.shape}")
            # print(f"self.beta_old {self.beta_old.shape}")

            self.beta = self.update(y, X, self.beta)
            print(f"number of iteration: {iter_count}")
            print(f"beta: {self.beta}")

            if not np.any(np.abs(self.beta_old - self.beta)>tol):
                converged = True
            self.beta_old = self.beta


        # self.beta = self.beta.to_numpy()

    def predict(self, X):
        innerProd = X @ self.beta
        y_hat = 1 * (innerProd > 50)
        return y_hat

    def simple_plot(self, model, X,y):
        plot_decision_regions(X, y, clf=model)
        self.mypredict = model.predict(X)
        title = plt.gca().set(title=f"Accuracy={(self.mypredict==y).mean()} using {model}",
        # title = plt.gca().set(title=f"Accuracy using {model}",
                            xlabel="Feature 1",
                            ylabel="Feature 2")







