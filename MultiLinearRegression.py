import numpy as np
import sklearn
from sklearn.linear_model import LassoCV,ElasticNetCV, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib. pyplot as plt
from sklearn.model_selection import cross_val_predict
from numpy import genfromtxt
from sklearn import metrics
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import BaggingRegressor
from sklearn.datasets import make_regression

Coefficients,Feats = [],[]
# fig, ax = plt.subplots(nrows=1, ncols=1, sharex='all', sharey=False)
fig, ax = plt.subplots(nrows=1, ncols=1)
fig.set_size_inches(8.0, 7.0)

#Inport and get training/test set
X = genfromtxt('/mnt/d/Sterimol/Model5Toms.csv', delimiter=',')
Y = genfromtxt('/mnt/d/Sterimol/Sub+ORCAY.csv', delimiter=',')

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.1)
r=X_train.shape[0]-1
#Xtest2 = genfromtxt('/Users/matina/Desktop/descriptors/alldes/modifications3-3+sub0.csv', delimiter=',')
# X_train, y_train = make_regression(n_samples=1000, n_features=4, n_informative=2, n_targets=1,random_state=0, shuffle=False)
# model = BaggingRegressor(LassoCV(cv=5,n_alphas=10000,selection='random',normalize=True,max_iter=1000000),bootstrap_features=True,
#                          n_estimators=50,oob_score = True, bootstrap=True)

model=LassoCV(cv=10,selection='random',fit_intercept=1 ,normalize=True,max_iter=10000).fit(X_train,y_train) #Run CV
# reg=model.fit(X_train,y_train)

# plt.plot(model.alphas_,model.mse_path_)
# print(model.alpha_)


#Training set
predicted=model.predict(X_train)

print('Root Mean Squared Error Training Set:', np.sqrt(metrics.mean_squared_error(y_train, predicted)))
print('R2 Training Set:',r2_score(y_train, predicted))
# print("MSE Train Set", mean_squared_error(y_train, predicted))

ax.scatter(y_train, predicted ,color= 'grey')
# z = np.polyfit(y_train, predicted, 1)
# p = np.poly1d(z)
# ax[0].plot(Y,p(Y))

ax.set_ylabel('Predicted Δ∆$G^{‡}$ (kJ/mol)',fontsize=20)
ax.set_xlabel('Experimental Δ∆$G^{‡}$ (kJ/mol)',fontsize=20)
b1, m1 = np.polyfit(y_train, predicted, 1)
ax.plot(y_train, b1 + m1 * y_train, color= 'black')
ax.set_ylim(-2, 9)
ax.set_yticks(range(-2, 10, 2))
ax.set_xlim(-0.05, 9)
ax.set_xticks(range(0, 10, 2))
ax.tick_params(labelsize=20)

#Coefficients
#print(model.coef_,file=open("/mnt/d/Sterimol/Model4coef.csv", "a"))
print(len(model.coef_))
for i in range (len(model.coef_)):
    Coefficients.append(model.coef_[i])
    print(model.coef_[i], file=open("/mnt/d/Sterimol/Model5coef.csv", "a"))
Feat1=np.nonzero(model.coef_)
Feats.append(Feat1)
print(Feat1)
X2=X[:,Feat1]
X2.shape

#Test Set
Yfit=model.predict(X_test)
#Yfit2=model.predict(Xtest2)
#print(Yfit2)
print('Root Mean Squared Error Test Set:', np.sqrt(metrics.mean_squared_error(y_test, Yfit)))
print('R2 Test Set:',r2_score(y_test, Yfit))
# print("MSE Test Set",mean_squared_error(y_test, Yfit))
# print("what is this score",model.oob_score_)
# print(Yfit)
ax.scatter(y_test,Yfit, color= 'b', marker='x')
# z = np.polyfit(y_test, Yfit, 1)
# p = np.poly1d(z)
# ax[1].plot(Y,p(Y))

# ax[1].set_ylabel('Predicted Δ∆$G^{‡}$ (kJ/mol)',fontsize=25)
# ax[1].set_xlabel('Experimental Δ∆$G^{‡}$ (kJ/mol)',fontsize=25)
# b1, m1 = np.polyfit(y_test,Yfit, 1)
# ax[1].plot(y_test, b1 + m1 * y_test, color= 'black')
# ax[1].set_ylim(-1, 9)
# ax[1].set_yticks(range(-1, 10, 2))
# ax[1].set_xlim(-0.05, 9)
# ax[1].set_xticks(range(0, 10, 2))
# ax[1].tick_params(labelsize=25)


plt.show()
