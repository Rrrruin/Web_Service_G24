import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import main

store = pd.read_csv("store.csv")
sample = pd.read_csv("sample_submission.csv")
test= pd.read_csv("test.csv")
train = pd.read_csv("train.csv")

fig = plt.figure(figsize = (7,5));
ax=fig.add_subplot(1,1,1) # 在画布上申请一个坐标轴
# 参数分别是子图的总行数、总列数和子图的位置（第几个子图）
ax.hist(train['Sales'],bins=25)
ax.set_title("Sales Feature Distribution", fontsize = 14)
ax.set_xlabel("Values")
ax.set_ylabel("Number of Records")
ax.set_ylim((0,300000))
fig.show()


train['Sales'] = train['Sales'].apply(lambda x: np.log(x + 1)) #该函数使用比较方便
fig = plt.figure(figsize = (7,5));
ax=fig.add_subplot(1,1,1)
ax.hist(train['Sales'],bins=25)
ax.set_title("Sales Feature Distribution", fontsize = 14)
ax.set_xlabel("Values")
ax.set_ylabel("Number of Records")
ax.set_ylim((0,300000))
fig.show()


train['Sales'] = train['Sales'].apply(lambda x: np.log(x + 1)) #该函数使用比较方便
fig = plt.figure(figsize = (7,5));
ax=fig.add_subplot(1,1,1)
ax.hist(train['Sales'],bins=25)
ax.set_title("Sales Feature Distribution", fontsize = 14)
ax.set_xlabel("Values")
ax.set_ylabel("Number of Records")
ax.set_ylim((0,300000))
fig.show()

store['CompetitionDistance'] = store['CompetitionDistance'].apply(lambda x: np.log(x + 1))
fig = plt.figure(figsize = (7,5));
ax=fig.add_subplot(1,1,1)
ax.hist(store['CompetitionDistance'],bins=25)
ax.set_title("CompetitionDistance Feature Distribution", fontsize = 14)
ax.set_xlabel("Values")
ax.set_ylabel("Number of Records")
ax.set_ylim((0,600))
fig.show()

store['CompetitionDistance'] = store['CompetitionDistance'].apply(lambda x: np.log(x + 1))
fig = plt.figure(figsize = (7,5));
ax=fig.add_subplot(1,1,1)
ax.hist(store['CompetitionDistance'],bins=25)
ax.set_title("CompetitionDistance Feature Distribution", fontsize = 14)
ax.set_xlabel("Values")
ax.set_ylabel("Number of Records")
ax.set_ylim((0,600))
fig.show()

store['CompetitionDistance'] = store['CompetitionDistance'].apply(lambda x: np.log(x + 1))
fig = plt.figure(figsize = (7,5));
ax=fig.add_subplot(1,1,1)
ax.hist(store['CompetitionDistance'],bins=25)
ax.set_title("CompetitionDistance Feature Distribution", fontsize = 14)
ax.set_xlabel("Values")
ax.set_ylabel("Number of Records")
ax.set_ylim((0,600))
fig.show()

model = main.model1
feature_importance = model.feature_importances_
feature_importance = 100.0 * (feature_importance / feature_importance.max())
test_new_final = main.test_new_final
print('特征：', test_new_final.columns)
print('每个特征的重要性：', feature_importance)

sorted_idx = np.argsort(feature_importance) # 取顺序索引
pos = np.arange(sorted_idx.shape[0]) # 取范围值
plt.barh(pos, feature_importance[sorted_idx], align='center')
plt.yticks(pos, test_new_final.columns[sorted_idx]) # 标注的是列索引
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Variable Importance')
plt.show()

