# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler  # 引入归一化的包
from sklearn.cross_validation import cross_val_score
import xlrd


def linearRegressionFile(fileName):
    # 加载数据
    data = loadDataFromeExcel(fileName)
    train_df = data.filter(regex='ANS|TH|U|K')
    # print train_df
    train_np = train_df.as_matrix()
    # print train_np

    X = np.array(train_np[:, 0:-1], dtype=np.float64)  # X对应0到倒数第2列
    Y = np.array(train_np[:, -1], dtype=np.float64)  # y对应最后一列

    # print X
    # print Y

    # 归一化操作
    scaler = StandardScaler()
    scaler.fit(X)
    x_train = scaler.transform(X)
    print "newData"
    # 线性模型拟合
    model = linear_model.LinearRegression()
    model.fit(x_train, Y)

    print "model.coef_ "
    print model.coef_  # Coefficient of the features 决策函数中的特征系数
    print "model.intercept_ "
    print model.intercept_  # 又名bias偏置,若设置为False，则为0

    print "验证的份情况"
    scores = cross_val_score(model, X, Y, cv=5)
    print(scores.mean(), scores)


def linearRegression():
    # 加载数据
    data = loadDataFromeExcel("5.xlsx")
    train_df = data.filter(regex='ANS|TH|U|K')
    # print train_df
    train_np = train_df.as_matrix()
    # print train_np

    X = np.array(train_np[:, 0:-1], dtype=np.float64)  # X对应0到倒数第2列
    Y = np.array(train_np[:, -1], dtype=np.float64)  # y对应最后一列

    # print X
    # print Y

    # 归一化操作
    scaler = StandardScaler()
    scaler.fit(X)
    x_train = scaler.transform(X)
    print "newData"
    # 线性模型拟合
    model = linear_model.LinearRegression()
    model.fit(x_train, Y)

    print "model.coef_ "
    print model.coef_  # Coefficient of the features 决策函数中的特征系数
    print "model.intercept_ "
    print model.intercept_  # 又名bias偏置,若设置为False，则为0

    print "验证的份情况"
    scores = cross_val_score(model, X, Y, cv=5)
    print(scores.mean(), scores)


def loadtxtAndcsv_data(fileName, split, dataType):
    return np.loadtxt(fileName, delimiter=split, dtype=dataType)


def loadDataFromeExcel(fileName):
    newFileName = "../../Resource/" + fileName
    data = pd.read_excel(newFileName)
    return data


def loadDataFromeExcel2(fileName):
    newFileName = "../../Resource/" + fileName
    data = xlrd.open_workbook(newFileName)
    table = data.sheets()[0]
    nrows = table.nrows
    lisall = []
    for i in xrange(1, nrows):
        rowValues = table.row_values(i)  # 某一行数据
        l = []
        for item in rowValues:
            l.append(item)
        lisall.append(l)
    return lisall


# 加载npy文件
def loadnpy_data(fileName):
    return np.load(fileName)


if __name__ == "__main__":
    linearRegressionFile("1.xlsx")
    linearRegressionFile("2.xlsx")
    linearRegressionFile("3.xlsx")
    linearRegressionFile("4.xlsx")
    linearRegressionFile("5.xlsx")
    linearRegressionFile("9.xlsx")
