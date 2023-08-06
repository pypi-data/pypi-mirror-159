import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import sklearn as sk
from sklearn import datasets
from sklearn.datasets import make_blobs
from time import time
from bisect import bisect_left
class gradeEvaluation():
    def __init__(self, method='dominate', direction='min', levels=4, percent=None):
        self.levels=levels
        self.method=method
        self.direction=direction
        if percent==None:
            self.percent=[1/levels for i in range(1, levels+1)]   # 按等级分四个比例
        else:
            self.percent=[i/sum(percent) for i in percent]
            self.levels=len(percent)
    def _paretoFront(self, x,):
        """
        note：内部函数，不建议直接调用
        函数功能：判断各样本是否为pareto第一前沿
        函数描述：输入二维数据及最优方向，判断各样本是否为pareto第一前沿
        输入参数：x: 二维数据，二维列表或二维数组
                 'direction'：最优方向，默认越小越优---多个指标需要设置相同的优化方向
        输出参数：一维1-0数组，表示各样本是否属于pareto第一前沿
        """
        m, n=x.shape
        result=[]
        for i, xi in enumerate(x):
            if self.direction=='min':
                judge1=(x<=xi).sum(axis=1)
                judge2=(x<xi).sum(axis=1)
            else:
                judge1=(x>=xi).sum(axis=1)
                judge2=(x>xi).sum(axis=1)
            result.append(sum([(judge1[i]==n  and judge2[i]>=1) for i in range(m)]))
        return np.array([int(i==0) for i in result])
    def paretoFront(self, x,):
        """
        note：...
        函数功能：计算各样本所属前沿
        函数描述：输入二维数据及最优方向，计算各样本所属前沿
        输入参数：x: 二维数据，二维列表或二维数组
                 'direction'：最优方向，默认越小越优---多个指标需要设置相同的优化方向
        输出参数：整形1维数组，表示各样本所属前沿
        """
        m, n= x.shape
        x=np.c_[x, [i for i in range(m)]]   # tracker is ready
        tracker, pf=[], []
        i=0
        while True:
            i+=1
            _=self._paretoFront(x[:, :-1],)
            tracker+=(x[_==1])[:,-1].tolist()
            pf+=([i for j in range(sum(_))])
            x=x[_==0]
            if x.shape[0]==0:
                break
        res=pd.DataFrame([tracker, pf]).T
        res.sort_values(0, inplace=True)
        return res.iloc[:,1].values 
    def _paretoLevel_by_front(self, xfront, percent,):
        """
        note:内部函数，不建议直接调用
        函数功能：计算pareto等级
        函数描述：基于原始样本x和其被支配数量pl，将数据分为levels个等级，给出各个样本所属等级
        输入参数：x: 二维数据，二维列表或二维数组
                 pl:支配各个样本的样本数量
                 levels：拟分级数量
        输出参数：一维数组，按顺序的各个样本的所属等级
        """
        pfx, pfxn=[], []
        unique=np.unique(xfront)
        for i in unique:
            pfxn.append(len(xfront[xfront==i]))    # 从小到大排序的每个支配度的数量
        cumsum=np.cumsum(pfxn)/len(xfront)   # 各个支配度的累加比例
        ids=[]
        percent=np.cumsum(self.percent)
        for i, percent_i in enumerate(percent):
            mid=np.abs((cumsum-percent_i))
            idi=np.argmin(mid)
            ids.append(unique[idi])
            cumsum=cumsum[idi+1:]
            unique=unique[idi+1:]
            if len(cumsum)==0:
                break
        return np.array([bisect_left(ids, i)+1 for i in xfront]), [int(i) for i in ids]
    def paretoDonimate(self, x,):
        """
        note：内部函数，不建议单独使用
        函数功能：计算支配各个样本的所有样本数量
        函数描述：输入二维数据及最优方向，计算支配各个样本的样本数量
        输入参数：x: 二维数据，二维列表或二维数组
                 'direction'：最优方向，默认越小越优---多个指标需要设置相同的优化方向
        输出参数：pl：一维数组，按顺序的，支配各个样本的样本数量
        """
        x=np.array(x)
        m, n=x.shape
        pl=[]
        for i, xi in enumerate(x):
            if self.direction=='min':
                judge=(x<xi).sum(axis=1)
            else:
                judge=(x>xi).sum(axis=1)
            judge=(judge==n).sum()
            pl.append(judge)
        return np.array(pl)
    def _paretoLevel_by_dominate(self, xdominate,):
        """
        note:内部函数，不建议直接调用
        函数功能：计算pareto等级
        函数描述：基于原始样本x和其被支配数量pl，将数据分为levels个等级，给出各个样本所属等级
        输入参数：x:二维数据，二维列表或二维数组
                 pl:支配各个样本的样本数量
                 levels：拟分级数量
        输出参数：一维数组，按顺序的各个样本的所属等级
        """
        pfx, pfxn=[], []
        unique=np.unique(xdominate)
        for i in unique:
            pfxn.append(len(xdominate[xdominate==i]))    # 从小到大排序的每个支配度的数量
        cumsum=np.cumsum(pfxn)/len(xdominate)   # 各个支配度的累加比例
        ids=[]
        percent=np.cumsum(self.percent)
        for i, percent_i in enumerate(percent):
            mid=np.abs((cumsum-percent_i))
            idi=np.argmin(mid)
            ids.append(unique[idi])
            cumsum=cumsum[idi+1:]
            unique=unique[idi+1:]
            if len(cumsum)==0:
                break
        return np.array([bisect_left(ids, i)+1 for i in xdominate]), [int(i) for i in ids]
    def fit(self, x,):
        """
        note:训练函数
        函数功能：训练pareto评级器，获得当前样本pareto前沿/被支配度，等级，等级区间
        函数描述：基于原始样本x，获得当前样本pareto前沿/被支配度，等级，等级区间
        输入参数：x:二维数据，二维列表或二维数组
        输出参数：样本pareto前沿/被支配度，等级，等级区间属性
        """
        self.x0=x
        m,n=np.array(x).shape
        self.dim=n
        if self.method=='front':
            xfront=self.paretoFront(x,)
            grade, ids=self._paretoLevel_by_front(xfront, levels=self.levels, percent=self.percent)
            self.fd=xfront
        else:
            xdominate=self.paretoDonimate(x,)
            grade, ids=self._paretoLevel_by_dominate(xdominate,)
            self.fd=xdominate
        self.grade=grade
        self.ids=ids
    def _evaluation(self, x):
        """
        note:内部函数，不建议直接调用
        函数功能：评估函数
        函数描述：获得当前样本pareto前沿/被支配度，等级
        输入参数：x:单元素二维数据，形式为[[1,2]]
        输出参数：获得当前样本pareto前沿/被支配度，等级
        """
        x=np.array(x)
        if self.method=='front':   
            x=np.r_[x, self.x0,]
            i=0
            while True:
                i+=1
                _=self._paretoFront(x, direction=self.direction)
                if _[0]==1:
                    break
                x=x[_==0]
                if x.shape[0]==0:
                    break
            fd=i
        else:
            n=len(x)
            if self.direction=='min':
                judge=(self.x0<x).sum(axis=1)
            else:
                judge=(self.x0>x).sum(axis=1)
            judge=(judge==n).sum()
            fd=judge
        grade=bisect_left(self.ids, fd)+1
        if grade>self.levels:
            grade=self.levels
        return fd, grade
    def evaluation(self, x):
        """
        note:
        函数功能：评估函数
        函数描述：获得当前样本pareto前沿/被支配度，等级
        输入参数：x:任意元素二维数据，形式为[[1,2]] 或[[1,2], [0, 3]...]
        输出参数：获得当前样本pareto前沿/被支配度，等级
        """
        x=np.array(x)
        if x.ndim<2:
            raise Exception('x must a 2D data.')
        fd, grade=[], []
        for xi in x:
            fd_i, grade_i=self._evaluation([xi])
            fd.append(fd_i)
            grade.append(grade_i)
        return fd, ranking
    def show(self, size=(10, 10), dpi=120):
        """
        note:
        函数功能：可视化
        函数描述：等级评价的二维/三维可视化
        输入参数：画布尺寸,dpi
        输出参数：二维三维可视化图片
        """
        fig=plt.figure(figsize=size, dpi=dpi)
        if self.dim==2:
            for i in range(1, self.levels+1):
                plt.scatter(self.x0[self.grade==i][:,0], self.x0[self.grade==i][:,1])
        elif self.dim==3:
            ax = plt.axes(projection='3d')
            for i in range(1, self.levels+1):
                ax.scatter(self.x0[self.grade==i][:,0], self.x0[self.grade==i][:,1], self.x0[self.grade==i][:,2],)
        else:
            raise Exception('x0 is not a 2D or 3D data.')      