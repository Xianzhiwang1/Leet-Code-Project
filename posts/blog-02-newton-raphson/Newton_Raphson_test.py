# Newton Raphson test
import numpy as np
from matplotlib.patches import Patch
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
# from mlxtend.plotting import plot_decision_regions

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score


# Logistic Regression and Newton Raphson 
class Newton_Raphson():
    def __init__(self, *kernel, **kernel_kwargs):
        self.kernel = kernel
        self.kernel_kwargs = kernel_kwargs
        # self.beta_old = np.random.rand(3,1) 
        # self.beta = np.random.rand(3,1) 
        self.beta = None
        self.beta_old = None
        self.alpha = 0.5   
        self.reg = False 

    def sigmoid(self, x: np.array):
        return 1/(1+np.exp(-x))

    def prob(self, X: np.array, beta: np.array) -> np.array:
        '''
        prob stands for probability
        '''
        # return np.array(self.sigmoid(X.dot(beta)))
        # return self.sigmoid(X.T @ beta)
        # print(f"self.sigmoid shape: {(self.sigmoid(X @ beta)).shape}")
        return self.sigmoid(X @ beta)

    def Var(self, p: np.array):
        '''
        Var stands for Variance 
        '''
        # print(f"p: {p}")
        # print(f"1-p: {1-p}")
        # elementwise multiply
        # on_diag = p*(1-p)
        on_diag = np.multiply(p, (1-p)) 
        # print(f"on_diag: {on_diag}")
        # print(f"on_diag shape: {np.shape(on_diag)}")
        d = on_diag.reshape(-1)
        # on_diag = p @ (1-p).T
        # return np.diag(np.diag(on_diag))
        # print(np.diag(d))
        return np.diag(d)

    def Hessian(self, X: np.array, beta: np.array):
        '''
        print(f"X.T.shape {X.T.shape}")
        print(f"X.shape {X.shape}")
        print(f"V is Var; V.shape is: {V.shape}")
        print(XV.shape)
        result = np.dot(XV, X)
        '''
        V = self.Var(self.prob(X,beta))
        XV = X.T @ V
        result = XV @ X

        return result

    def update(self, y: np.array, X: np.array, beta: np.array) -> np.array:
        '''
        print(f"X.T.shape is: {X.T.shape}")
        print(f"y.shape is: {y.shape}")
        print(f"self.prob(X,beta).shape is: {self.prob(X,beta).shape}")
        grad = X.T @ (y - self.prob(X,beta))
        print(f"grad.shape: {grad.shape}")
        print(f"step shape: {step.shape}")
        '''
        grad = np.matmul(X.T, (y-self.prob(X,beta))) 
        # reguliazation
        if (self.reg):
            hessian = self.Hessian(X,beta) + np.eye(beta.shape[0])
            step = np.linalg.inv(hessian) @ grad
        # no reguliazation
        else:
            hessian = self.Hessian(X,beta)
            step = np.linalg.inv(hessian) @ grad
        step = self.alpha * step
        beta = beta + step 
        return beta

    def regress(self, y, X, max_iters = 1e1, tol=1e-8, converged=False):
        # it is very important to check the shape of X and y
        X = self.patek(X)
        y = y.reshape(-1,1)
        self.beta_old = np.ones((X.shape[1],1))
        self.beta_old = self.beta_old.reshape(-1,1)
        self.beta = np.random.rand(X.shape[1],1)
        self.beta = self.beta.reshape(-1,1)
        # self.beta = np.array([-5.4e-02,  6.8e-02, 2.3e-2]) 
        # print(f"learning rate is: {self.alpha}")
        # print(f"Regularization is: {self.reg}")
        
        iter_count = 0 
        while not converged and (iter_count<max_iters):
            iter_count += 1
            # print(f"self.beta {self.beta.shape}")
            # print(f"self.beta_old {self.beta_old.shape}")

            self.beta = self.update(y, X, self.beta)
            if (iter_count % 10 == 0):
                print(f"number of iteration: {iter_count}")
                print(f"beta: {self.beta}")
            # print(f"number of iteration: {iter_count}")
            # print(f"beta: {self.beta}")

            if not np.any(np.abs(self.beta_old - self.beta)>tol):
                converged = True
                print(f"Converged with {iter_count} iterations")
                print(f"The beta we end up with is: {self.beta}")
            self.beta_old = self.beta


        # self.beta = self.beta.to_numpy()

    def predict(self, X):
        X = self.patek(X)
        innerProd = X @ self.beta
        y_hat = 1 * (innerProd > 0)
        return y_hat

    def score(self,X,y):
        y = y.reshape(-1)
        mypredict = self.predict(X)
        mypredict = mypredict.reshape(-1)
        myscore = 1 * (mypredict == y) 
        return myscore.mean()

    def bare_bone_plot(self, X: np.array, y: np.array, size_1: int, size_2: int) -> None:
        plt.rcParams["figure.figsize"] = (size_1,size_2)
        mypredict = self.predict(X)
        # score = (mypredict == y).mean()
        print(f"the weight beta is: {self.beta}")
        a_0 = self.beta[0][0]
        a_1 = self.beta[1][0]
        a_2 = self.beta[2][0]
        fig = plt.scatter(X[:,0], X[:,1], c = y)
        xlab = plt.xlabel("Feature 1")
        ylab = plt.ylabel("Feature 2")
        f1 = np.linspace(-7.5, 7.5, 501)
        p = plt.plot(f1,  -(a_2/a_1) - (a_0/a_1)*f1, color = "black")
        # title = plt.gca().set_title(f"score is: {round(score,3)}")
        title = plt.gca().set_title("our regression")
    


    def helper_plot(self, X, y, subplot, label, F1,F2):
        '''
        Helper method for big_plot
        '''
        score = self.score(X,y) 
        a_0 = self.beta[0][0]
        a_1 = self.beta[1][0]
        a_2 = self.beta[2][0]
        fig = subplot.scatter(X[:,0], X[:,1], c = y)
        subplot.set(xlabel=F1, ylabel=F2, title=f"score: {round(score, 3)} using {label} data")
        # the line
        f1 = np.linspace(3.5, 14.5, 501)
        p = subplot.plot(f1,  -(a_2/a_1) - (a_0/a_1)*f1, color = "black")

    def big_plot(self, X_train, y_train, X_validate, y_validate, X_test, y_test, size_1, size_2, F1, F2):
        plt.rcParams["figure.figsize"] = (size_1,size_2)
        fig, axarr = plt.subplots(1,3)
        self.helper_plot(X_train, y_train, axarr[0], "training", F1, F2)
        self.helper_plot(X_validate, y_validate, axarr[1], "validation", F1, F2)
        self.helper_plot(X_test, y_test, axarr[2], "testing", F1, F2)
        plt.tight_layout()



    def patek(self, X: np.array) -> np.array:
        '''
        for padding
        '''
        return np.append(X, np.ones((X.shape[0],1)), 1)







