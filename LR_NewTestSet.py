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
fig, ax = plt.subplots(nrows=1, ncols=2)
fig.set_size_inches(15.0, 7.0)

#Inport and get training/test set
X = genfromtxt('/Users/matina/Desktop/descriptors/withmodel5/model5+SUB.csv', delimiter=',')
Y = genfromtxt('/Users/matina/Desktop/PipelineScripts/Reactionmatrix/Sub+ORCAY.csv', delimiter=',')
Xtest = genfromtxt('/Users/matina/Desktop/descriptors/withmodel5/modifications6-6+sub0.csv', delimiter=',')
# X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.1)
# r=X_train.shape[0]-1

# X_train, y_train = make_regression(n_samples=1000, n_features=4, n_informative=2, n_targets=1,random_state=0, shuffle=False)
# model = BaggingRegressor(LassoCV(cv=5,n_alphas=10000,selection='random',normalize=True,max_iter=1000000),bootstrap_features=True,
#                          n_estimators=50,oob_score = True, bootstrap=True)

model=LassoCV(cv=10,selection='random',fit_intercept=1,normalize=True,max_iter=10000).fit(X,Y) #Run CV
# reg=model.fit(X_train,y_train)

# plt.plot(model.alphas_,model.mse_path_)
# print(model.alpha_)


#Training set
predicted=model.predict(X)

print('Root Mean Squared Error Training Set:', np.sqrt(metrics.mean_squared_error(Y, predicted)))
print('R2 Training Set:',r2_score(Y, predicted))
# print("MSE Train Set", mean_squared_error(y_train, predicted))

ax[0].scatter(Y, predicted ,color= 'grey')
# z = np.polyfit(y_train, predicted, 1)
# p = np.poly1d(z)
# ax[0].plot(Y,p(Y))

ax[0].set_ylabel('Predicted Δ∆$G^{‡}$ (kJ/mol)',fontsize=20)
ax[0].set_xlabel('Experimental Δ∆$G^{‡}$ (kJ/mol)',fontsize=20)
# b1, m1 = np.polyfit(Y, predicted, 1)
# ax[0].plot(Y, b1 + m1 * Y, color= 'black')
ax[0].set_ylim(-2, 9)
ax[0].set_yticks(range(-2, 10, 2))
ax[0].set_xlim(-0.05, 9)
ax[0].set_xticks(range(0, 10, 2))
ax[0].tick_params(labelsize=20)

# #Coefficients
# # print(model.coef_,file=open("/Users/matina/Desktop/coef.txt", "a"))
# print(len(model.coef_))
# for i in range (len(model.coef_)):
#     Coefficients.append(model.coef_[i])
#     print(model.coef_[i], file=open("/Users/matina/Desktop/coef.csv", "a"))
Feat1=np.nonzero(model.coef_)
Feats.append(Feat1)
# print(Feat1)
X2=X[:,Feat1]
X2.shape

#Test Set
Yfit=model.predict(Xtest)
print(Yfit)
ax[1].hist(Yfit)
# print('Root Mean Squared Error Test Set:', np.sqrt(metrics.mean_squared_error(y_test, Yfit)))
# print('R2 Test Set:',r2_score(y_test, Yfit))
# print("MSE Test Set",mean_squared_error(y_test, Yfit))
# print("what is this score",model.oob_score_)
# print(Yfit)
# ax.scatter(y_test,Yfit, color= 'b', marker='x')
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

plt.savefig('/Users/matina/Desktop/model5Data.png')
plt.show()