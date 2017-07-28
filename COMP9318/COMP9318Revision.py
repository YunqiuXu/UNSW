# COMP9318 Revision
+ Content:
        + Introduction
        + Data Warehouse, OLAP # Tut 1
        + Data Preprocessing
        + Classification # Tut 2
        + LR
        + Clustering # Tut 3
        + Association Rules # Tut 4
        + Recommendation Systems
+ Final Exam:
        + 2 hours, choose 1 + 6 questions from 9
        
######### 0. Introduction
+ Overview:
        + DM vs. KDD
        + Steps of KDD;iterative in nature;results need to be validated
        + Database (efficiency) vs. Machine learning (effectiveness) vs. Statistics (validity)
        + Cast a real problem into a data mining problem
        
## 0.1 DM vs. KDD
+ DM: Extraction of interesting patterns from large amount of data
+ KDD(knowledge discovery in databases) is just another name for DM
+ Or DM is the core of KDD
+ 注意不是所有东西都适合数据挖掘, 例如:
        + 演绎: 数据挖掘适合归纳而非演绎
        + 专家系统或者小项目 : 不满足huge amount of data
'''基本应用看一下'''
## 0.2 Steps of KDD
+ 'P11'的流程图
+ 'P12'的流程:
        + Get prior knowledge and goal
        + Data selection: create a target dataset
        + Data cleaning and preprocessing
        + Data reduction and transformation: 包括离散化, 特征选择, 降维等
        + Choosing functions of data mining
                + characterization
                + discrimination
                + association and correlation analysis
                + classification
                + regression
                + clustering
        + Choosing the mining algorithm(s)
                + e.g. for classification : LR / Tree / Bayes
        + Data mining # 数据挖掘只是KDD的一个步骤, 核心步骤
        + Pattern evaluation and knowledge presentation
        + Use of discovered data
## 0.3 DM vs. ML vs. Statistics
+ DM: efficiency
        + Find interesting things in massive data
+ ML: effectiveness
        + Machine learning investigates how computers can learn (or improve their performance) based on data
+ Statistics: validity
        + Statistics studies the collection, analysis, interpretation or explanation, and presentation of data
## 0.4 Practice
+ When face a real problem, we need to know:
        + Data to be mined
        + Knowledge to be mined
        + Techniques to be used
        + Potential applications
## 0.5 Major Issues:
+ 方法: 性能 / 评估 / 处理噪音 ...
+ 交互: 
+ 应用:

'最后再看下P24的Summary'
        
######### 1. Data Warehousing and OLAP
+ Overview:
        + DW vs. Data Mart --> 4 chars
        + OLTP vs. OLAP
        + Multidimentional (data cube)
                + fact / dimension / measure / hierarchies
                + cuboid / cube lattice
                + 3 kinds of schemas
                + 4 OLAP operations
                + ROLAP vs. MOLAP vs. HOLAP
        + Query processing : # see BUC and tutorial
                + Bitmap indexing
                + Join indexing
                + Cube by VS Group by
        Exception(not needed) : Design DW , ETL --> DW
        
## 1.1 Basic Concepts of DW
+ Definition:
        + A decision support database, separate from the organization’s operational database
        + Support information processing, provide consolidated historical data --> for 'analysis'
        
+ '重要' 4 characters:
        + 'subject-oriented': 
                + 比较主观, 没用的删去
                + 基于customer等项目, 重视对数据的model and analy, 而非日常操作和数据处理, 因此对制定决策没什么关系的数据都会被excluded
        + 'integrated': 
                + DW整合了多种数据来源
                + we need data cleaning and integration
        + 'time-variant': 
                + 持续时间长, 时间element包含在key内部(关系数据则不一定如此)
        + 'non-volatile': 
                + 放在DW中的数据不会被更新, 只能initial loading或accessing
                + 不存在关系数据中的事务处理/并发控制等
## 1.2 OLTP vs. OLAP
+ OLAP consists of : Multidimentional ~ / Relational ~
+ The archetecture of DW : 'P11'
        + Bottom: DW server
        + Middle: OLAP server
        + Top: client
+ '重要, OLTP vs OLAP(DB vs DW)' P13-P14
        + OLTransactionP是操作性数据 --> 某个客户：某某酒吧销售某某啤酒的价格是多少？
        + OLAnaliticalP是分析性数据 --> 某个投资商：每个酒吧在过去三个月里销售所有啤酒的平均价格是多少？ 
        + 差别1: 使用者, 前者为员工或者IT专家, 后者为知识工程师
        + 差别2: 功能, 前者是日常操作, 后者是决策制定
        + 差别3: 数据库类型, 前者是application-oriented, 后者是DW(subject-oriented)
        + 差别4: 数据, 前者是current/time-invariant/volatile, 后者相反(historical/多维度...)
        + 差别5: 操作, 前者可以读写或者事务处理, 后者non-volatile,只能读写
        + 差别6: 用户量, 前者几千, 后者几百
        + 差别7: 数据库大小, 前者GB级别, 后者TB级别
        
## 1.3 Multidimentional Model --> Data Cube
+ Basic concepts: # 例如Subject为分析总销售额
        + Fact: the subject it models, e.g. transactions / snapshots # 每次销售事务
        + Measures: numbers that can be aggregated # 卖了多少, 卖了多少钱, 成本 --> 计算为利润
        + Dimensions: context of the measure # 库存，品名，时间
        + Hierarchies: 'Provide contexts of different granularities (aka. grains)'
        + 多维度建模的目标: Surround facts with as much relevant context (dimensions) as possible
        
+ Data Cube / Cuboid: 2D --> 3D # 看下P20-21例子   
+ Lattice of the cuboids: 'P23'
        + 从底层的0d --> 1d --> 2d --> 最上层的3d不断细化
        + 最上层的细化到一个cuboid, 即base cuboid
+ '四种操作':
        + Roll-up: hierachy上移 --> 越来越细, 如按地点产品月份查询
        + Drill-down : hierachy下移 --> 变粗略, 如就按月份查询不限制地点与产品
        + Slice and Dice: 固定一个或多个维度, 切分, 如指定月份的情况
        + Pivoting: 一般取出两个维度作为输出维度, 其他维度在这俩维度方向上进行聚类
'需要能看懂例子, 并指出Fact / Measure / Dimensions'

## 1.4 Logical Models
+ ROLAP --> Star schema / Snowflake / Galaxy
+ MOLAP --> MDX '不考', 但需要了解怎样形成MOLAP架构
+ HOLAP --> Base ROLAP + Others MOLAP

## 1.5 ROLAP: 'P38 - P40'
+ Star schema:
        + 中间一个fact table, 连着一堆dimension tables
        + 每个维度用维度表来表示
        + 每个事务用fact table来表示 # 即一个tuple
        + 星星图 denormalized once from the universal schema
        + 星星图 control redundancy
+ Snowflake schema: 
        + 特殊的星星图
        + denormalized more than once --> shape a set of smaller dimension tables
+ Fact constallations:
        + 相当于一堆星星图组合起来
        + 几个星星(fact table)共享维度表
        
+ 使用星星图的好处: Facts and dimensions are clearly depicted --> easy to comprehend '看一下P41的操作'
        
        
## 1.6 Query Language in ROLAP
'P47 - P54'
+ Indexing:
        + Low-cadinality attributes --> Bitmap Index
        + High-cadinality attributes --> Join Indices, relates the values of
the dimensions of a star schema to rows in the fact table
+ Bitmap indexing
        + Each attribute has its own bitmap index table. 
        + Bitmap indexing reduces join, aggregation, and comparison operations to bit arithmetic.
+ Join indexing 
        + registers the joinable rows of two or more relations from a relational database
        + reducing the overall cost of OLAP join operations

+ Arbitrary selections on Dimensions
+ Coarse-grain Aggregations --> Multidimensional aggregations --> Replace GROUP BY by Cuboid --> 'CUBE BY'
+ CUBE BY is more efficient than GROUP BY

+ 'BUC-SR' --> inplement CUBE BY effeciently # P67 - 68

## 1.7 MOLAP
+ (Sparse) array-based multidimensional storage engine
+ Pros: 
        + small size (esp. for dense cubes)
        + fast in indexing and query processing
+ Cons:
        + scalability
        + conversion from relational data

+ 流程之前在做作业时学过, 现在再复习下: 'P71'
        + 首先将变量数字化
        + 然后使用injective map来实现从cell 到offset的映射
        + 如果offset是稀疏的, 就这样就行了
        + 否则给offset排序
        + 最后相当于用offset来表示之前的一堆乱七八糟的列向量

#%#%#%#%#%#%#%#%#%#%#$%#%#%#%#%#%#%#%#%
######### 2. Data Preprocessing
＋ Overview:
        + What it dirty data : 'incomplete / noisy / inconsistant'
        + How to handle missing data
        + How to normalize data?
        + How to handle noisy data?
                + binning , histogram
                + V-optimal , MaxDiff
        + How to discretize data?
        Exception : Feature selection , PCA ...
        
## 2.1 Real data is dirty
+ 3 kinds of dirty data
        + Incomplete --> missing value
        + Noisy --> outliers
        + Inconsistant --> discrepancies
+ * Why is data dirty(这个我觉得大致看下就行)

## 2.2 Major tasks of data preprocessing
'cleaning / integration / transformation / reduction / discretization'
+ Data cleaning --> missing / noisy / outliers / inconsistencies
+ Data integration --> 整合多种数据来源
+ Data transformation --> Normalization , aggragation
+ Data reduction --> 在不影响结果的前提下精简数据
+ Data discretization & Data type conversion

## 2.3 Data cleaninging --> noisy / outliers / inconsistancy / redundancy
+ Handle missing data --> fill with # P10
        + Ignore tuple if not many
        + global constant
        + attribute mean for all samples
        + attribute mean for samples of same class
        + most probable value
+ Handle noisy data # P11
        + Binning: 等宽或等深分割, 然后就能搞少数几个标签了(如平均值中位数) # 后面离散化时再看下
        + Clustering: 检测并移除离群点
        + Combined computer and human
        + Regression: 使用回归方程拟合

## 2.4 Data Integration --> Handling Redundancy
+ 通过相关度分析发现冗余的数据
+ 或者在一开始整合的时候就小心点

## 2.5 Data Transformation
+ Smoothing / Aggragation / Generalization / Normalization / 创建新特征
+ Normalization: # P19
        + 归一化有助于排除量纲，将所有数据归于类似的范围
        + min-max : 适合极值已经确定的数据
        + z-score : 适合基于距离的数据, 如进行聚类分析时
        + decimal scaling
        
## 2.6 Data reduction: 降低维度, 数据压缩等
+ 高维数据很稀疏, 不易学习, 且距离量度变得没有意义
+ 考试不涉及模型选择与PCA

## 2.7 Data Discretization
+ 其实也算是数据类型转换: Neumerical/continuous --> Categorical
+ 离散数据对应概率质量函数, 连续数据对应概率密度函数
### 2.7.1 离散与连续的互相转化
+ Continuous --> Discrete
        + 去除噪音
        + 减少特异值, 使其更贴合模型, 提升性能
        + 降低数据量
+ Discrete --> Continuous
        + 平滑分布
        + 可以构建概率密度函数, 有助于模型泛化

### 2.7.2 Binning/Histogram analysis
+ 等宽切分:
        + 基于距离, 每个区间长度相同[(B-A) / N]
        + 对于不均匀(skewed)数据就苟屁啦
+ 等深切分:
        + 基于, 每个区间样本数相同
        + 数据被良好缩放'good data scaling'
        + 对于Categorical 属性不好搞
        
+ 实现切分: 尽可能最小化variance within same group
        + 动态规划'P49'
        + MaxDiff'P56': 这个有点像贪婪, 找最大的gap来做切分
### 2.7.3 Clustering analysis
+ 可以同时考虑多个属性 --> 相当于提升维度考虑问题了

### 2.7.4 Entropy-based discretization
+ 有监督的离散化方法
+ 这个有些类似决策树, 需要计算信息增益
+ 不断选择新的切分点, 直到最后信息增益不大

### 2.8 Kernel density estimation(KDE)
感觉没什么卵用的样子

### 2.9 OneHot encoding
+ 将类别数据转变为一系列二进制编码，方便分析比如逻辑回归等
+ 但不足是忽略了不同值间的相似性(把所有类别之间的差距都当一样了)

#%#%#%#%#%#%#%#%#%#%#$%#%#%#%#%#%#%#%#%        
######### 3. Classification
+ Overview:
        + Basic knowledge:
                + Overfitting模型太复杂, underfitting模型太简单
                + CV: K-fold, LOOCV
                + Classification vs. Regression: 一个是预测Labels一个是预测连续函数值
                + Supervised learning vs. Unsupervised learning: 一个是有标签(y)的一个没有瞎鸡巴找规律
                + Eager learning vs. lazy learning(instance-based): 懒惰学习完全基于数据集, 没了数据集就傻逼了, 没有显性的学习过程, 预测比较慢 'P89'
        + Decision tree:
                + ID3
                + Pruning: pessimistic
                + Rule-based(derive rules from the tree)
                + CART, gini index
'Why rule is better than tree': when pruning a tree we remove all the subset, but when pruning a rule, we just remove its preconditions --> less restrctive
        + NB:
                + Smoothing
                + 2 ways to apply NB on test data: Multinomial or Bernoulli?
        + Logistic Regression / MaxEnt Classifier
                + MLE of parameters
                + Regularization
                + Gradient ascend

## 3.1 Decision Tree
### 3.1.1 三种决策树
+ Entropy and Information Gain --> ID3, 先选择信息增益比较大的属性
+ Information Gain Ratio --> C4.5, 解决了属性不均衡的问题(ID3中选择比较多的属性信息增益比较大)，本课程不涉及C4.5
+ SPRINT: CART
        + Attribute list: 
                + 连续的属性排序, 新加一列index为排序前的位置(因此index是乱序的)
                + 离散的属性不排序, 新加一列index就是从1开始(升序)
                + 看下'tut2'
        + Gini Index : 假定所有属性都是连续的, 找基尼指数最小的位置进行切分
        + 切分点: 范围中点, e.g. 23-32 is 27.5
        + 注意CART一定是二叉树形式

### 3.1.2 剪枝 --> avoid overfitting
+ 后剪枝比前剪枝更有实践意义, 前剪枝不知在哪里停呀
+ Minimum description length (MDL) principle: stop growth of the tree when the encoding is minimized
+ 悲观剪枝: 本课程只涉及悲观剪枝, 可以和COMP9414, COMP9417结合
        + 错误率: 当前结点内样本中少数派所占比例(相当于被错误分类了)
        + 惩罚因子: 空结点的惩罚因子为0.5, 非空结点的惩罚因子为0.5*子结点数量
        + 剪枝后的错误率(加上相应惩罚因子)降低了--> 执行剪枝

### 3.1.3 决策树的优缺点
+ 优点
        + 学习速度较快, 之前对比过LR后者很慢
        + 可解释性强, 易于理解
        + 精度尚可
        + 可以使用SQL查询数据: e.g. SELECT ... WHERE 条件A & 条件B & 条件C
+ 缺点
        + 模型可能会很复杂, 易于导致OVERFITTING
        + 决策树对缺失值很敏感
+ 改进决策树性能的一些方法: 将连续属性离散化, 处理缺失值, 特征工程构建新的属性

## 3.2 Bayesian Classifiers
+ 贝叶斯理论基本概念
+ 条件独立性假设
+ Smoothing --> 防止分母为0 # P52
        + Add-1 Smoothing: 在估计条件概率的时候分子+1, 分母+类别数量
                + 防止 no-class 或者过小的概率
        + 例如对于二分类问题, 原来的1/3 --> (1+1) / (3+2)
        + 多项式贝叶斯和伯努利贝叶斯的平滑方式可能有差别, 注意下
+ 三种基本贝叶斯模型: 
        + 高斯贝叶斯: 
                + 适合处理Numeric Values --> P(X_i = v_j|C_k)
                + 注意也可以把feature values离散化 --> binning
        + 多项式贝叶斯: 离散变量 --> count
        + 伯努利贝叶斯: 离散变量 --> 0-1
+ NB in test classification: '多项式贝叶斯 & 伯努利贝叶斯 P62-72'
        + 文本分类中多项式模型更牛逼
        + 伯努利贝叶斯需要特征选择 --> 否则噪音很大
        + 多项式贝叶斯一般不需要特征选择
+ Log形式的贝叶斯分类器 --> 防止欠拟合 # P67
        C = argmax{log(p_c) + sum(log P(x_i|c_j)))
+ NB的优势: 
        + 快且易于实现
        + 大部分情况下结果还不错
+ NB的不足:
        + 不一定满足条件独立性假设
        + 对先验概率的估计并不一定精确 --> 改进: 逻辑回归
        
## 3.3 KNN
+ KNN是典型的instance-based learning: 学习时间短, 预测时间长
+ 注意需要标准化 --> 消除量纲
+ 高维数据 --> 维数灾难
+ 无关变量可能会影响距离度量
+ k值小overfitting, k值大overfitting
+ 升级版: distance-weighted, 距离平方的倒数作参数, 距离越近权重越大
        
+ lazy和eager的区别:
        + Lazy method may consider query instance x q when deciding how to
generalize beyond the training data D
                + 只是简单存储数据, 预测新样本时才分析新样本和已有数据的关系
                + 局部近似, 不需要训练但决策慢, 耗费存储空间
        + Eager method cannot since they have already chosen global
                + 使用已有样本得到目标函数, 之后预测时就不需要样本了
                + 考虑到了所有训练样本, 为全局近似, 训练慢决策快
approximation when seeing the query

## 3.4 Logistic Regression
+ Generative model vs. Discriminative
        + G --> get P(y|x) from P(x,y), e.g. NB, Hidden Markov
        + D --> model P(y|x) directly, e.g. LR, Tree, KNN
        + instance-based : kNN
+ 线性回归最小二乘拟合:
        + sum(yhat^i * x_i^i) = sum(y^i * x_i^i), 前面是估计值, 后面是真实值
        + 对于1-D, y^i = w_0 + w_1 * x_1^i, x_0 = 1, 因此我们把n个样本的情况加起来:
                + sum[(w_0 + w_1 * x_1^i) * 1] = sum[y^i * 1]
                + sum[(w_0 + w_1 * x_1^i) * x_i^i] = sum[y^i * x_i^i]
                + 根据这两个式子可以得到w_0, w_1
        + 对于矩阵形式: w = (X^T * X)^(-1) * X^T * Y, X每行是一个样本x^(i)^T

+ Logistic Regression:
        + Sigmoid function: 决策边界 p(x,w) >= 0.5
        + General log likelihood # P14 log形式
        + Partial derivatives

+ MLE: # P14
        + The likelihood of x^(i) is ...
        + The likelihood of whole training dataset is ... 
        + Log likelihood is ...
        
+ Gradient Ascent / SGD version : P18
        + w_j := w_j + alpha * sum[(yi - pxi) * xij]
        + SGD versin: w_j := w_j + alpha * (yi - px(i)) * x(i)j
        + 注意, 求最大似然用梯度上升, 求最小cost func用梯度下降
+ Regularization
        + Ridge --> L2
        + Lasso --> L1 --> may result in sparse models
        + --> L(w) + lambda * R(w)

+ Logistic for multiple classes --> MaxEnt
        + Pr(c|x) ~ exp(w_c^T * x)
        
logit(p) = log(p / (1-p)), here p is P(Y = 1 | X)


                
#%#%#%#%#%#%#%#%#%#%#$%#%#%#%#%#%#%#%#%
######### 4. Clustering
+ Overview:
        + Clustering criteria:
                + Minimize intra-cluster distance
                + Maximize inter-cluster distance
        + Distance:
                + Deal with different types of variables
                + Distance functions: Manhattan, Eculidean, ...
                + Metric distance functions
        + k-means: 
                + Algorithm
                + Pros and cons
        + Hierarchical clustering:
                + agglomerative
                + single-link / complete-link / group average  hierarchical clustering

## 4.1 Basic concept
+ What is good clustering
        + high intra-class similarity
        + low inter-class similarity
+ Data matrix and dissimilarity matrix
+ 输入数据方阵(M个features), 输出相似度/不相似度矩阵(N*N, 每个样本)

## 4.2 Similarity Measure
+ 数据类型多样, 因此不那么容易判断两个样本的相似度
+ Interval-scaled variables标准化来消除量纲: 
        + 注意s_f和m_f的计算方式:Mean absolute deviation 'P12'
        + 然后使用z-score进行标准化, 使用MSD比标准差更鲁棒
+ 评估相似度: 计算距离
        + L_p: Minkowski
        + L_1: Mahnattan
        + L_2: Eculidean
        + L_inf: Chebeshev

+ Binary variables: Jaccard coefficient, 注意这里距离是用来度量不相似度的, 相似度见推荐系统
        + Contingency table 'P16' --> 注意区分下对称和不对称的
        + 对称的 --> invariant : d(i,j) = (01 + 10) / (00 + 01 + 10 + 11)
        + 不对称的 --> noninvariant : d(i,j) = (01 + 10) / (01 + 10 + 11)
        + '再理解下P17的例子'
                + '性别'是对称的
                + '是否'是不对称的, 不需要'NN'
                + '这里只计算了不对称的'

+ Nominal Variables: 每个特征可以有多种选择
        + Simple matching: d(i,j) = (p(total) - m(count)) / p(total), 看两个样本有多少特征是不一样的
        + One-hot Encoding, 这个应该更好吧

+ Ordinal and ratio variables
        + Ordinal中顺序非常重要
                + 可以用rank替换原值
                + 类似z-score, 将每个变量标准化
                + 计算相似度方法类似interval-scaled variables
        + 成比例的变量: 非线性比例, 例如指数状 --> 使用log transformation    
   
         
## 4.3 Partitioning Algorithms --> K-means
'PAM, k-means++ or GMM'不考察细节, 但需要知道优点缺点和基本原理
+ 性能评估: 
        + 对每个聚类, cost(C_i) --> 聚类内点到质心距离的平方和
        + 对模型: 所有聚类cost的和
+ K-means是EM算法的一个实例: 看下基本原理和例子
        + 停止条件: 新质心和旧质心一样或者差别小于threshold
+ Pros and cons #P29
        + Pros: 
                + efficient, O(tkn) 比PAM的O(k(n-k)^2)效率高
                + can be used if no guarantee on quality
        + Cons:
                + Local minimum --> 改进: 模拟退火 / 遗传算法
                + Need to define mean --> 遇到categorical 变量就傻逼了
                + Need to choose k in advance
                + Hard to handle noisy data and outliers --> preprocessing
                + If cluster is not convex --> hard to partition

+ k-medoids(PAM):
        + 和K-means的不同: 
                + 不是计算质心, 而是在已有点内选择medoids
                + cost: 交换medoid会不会增加cost --> 如果cost会减少, 交换
                + 停止条件: 不需要再交换medoid-nonmedoid, or total swapping cost不下降
        + PAM算法的优势在于：
                + PAM算法比K-平均算法更健壮，中点对'对“噪声”和孤立点数据不敏感',不会像质心那样多个离群点就跑偏了
                + 它能够处理不同类型的数据点
                + 它对小的数据集非常有效
        + 存在的问题: 对大数据集没效率 --> 比K-means复杂度高
        
+ Gaussian Mixture Model(GMM): k-means可以被认为是GMM的特殊形式
        + GMM允许软间隔: soft cluster assignment --> 一个样本被归类为一个聚类的概率
        + 使用EM达到局部最优
        + 上面的方法都是判别模型, 可以看下之前学得判别模型和生成模型的区别
        
## 4.4 Hierarchical Clustering
+ 两种类型:
        + Buttom-up(allo): 每次合并距离最近的cluster, 直到最后就剩一个聚类了
        + Top-down(divise): 每次分裂直到每个聚类内至少一个样本或者达到聚类数量
        + 前者更好: 后者分裂方法太多了
+ 关键点: 评估聚类的相似度
        + MIN/Single-link: 
                + 两个聚类相似度最大(距离最近)的两个点作为相似度
                + Pros: 可以处理non-elliptical
                + Cons: 对outliers敏感
        + MAX/Complete-link: 
                + 两个聚类相似度最小(距离最大)的两个点作为相似度
                + Pros: 对离群点不敏感
                + Cons: 
                        + Tends	to	break	large	clusters
                        + Biased towards globular clusters
        + Centroid-based: 两个聚类的中点
        + Group Average: 
                + 两个聚类点对的全连接取平均值
                + 看下'P63'公式, 几点注意:
                        + 组内点的连线也要计入在内
                        + 分子要乘以2: 42和24都要算
                        + 分母: (|C1|+|C2|)*(|C1|+|C2|-1)
                + 不使用简单平均距离的原因: 需要保证no inversions
        + Centroid和Group对噪音和离群点同样不敏感, 但要求是globular cluster(球状)
+ 看下'P53-59'的例子
+ 总体而言Hierarchical和之前Partitional Algorithm相比的缺点:
        + 复杂度高, O(n^2)
        + 无法撤销之前已经做过的, 分裂了就分裂了没法再回去, 不像Kmeans那样理论上可以无限循环     
        + 可能聚类成链状(如果本身就是链状的, 那还不错)
        
        
'总结下三种聚类的优缺点'
+ K-means: 
        + 速度快
        + 容易local minimum, 对离群点敏感
        + 搞不定non-convex
+ PAM:
        + 对离群点不敏感
        + 复杂度高, 对大机群没效率
+ GMM: 
        + 软间隔
+ Hierarchical:
        + 距离和规则容易定义, 不一定要是convex, 不需要提前制定聚类数量
        + 复杂度高, 且无法撤销undo, 可能受离群点影响
'注意对于catgorical数据搞不定'

#%#%#%#%#%#%#%#%#%#%#$%#%#%#%#%#%#%#%#%           
######### 5. Association Rule Mining
+ Overview:
        + 使用aprori或者fp-growth得到频繁项集, 然后基于频繁项集生成关联规则
        + Inputs and Outputs:
                + Input: transaction db
                + Output(threshold):
                        + frequent itemset # minsup
                        + association rules # minconf
        + Apriori:
                + Why use it?
                + 2 versions of Apriori property
                + Apriori algorithm
                        + How to find frequent itemsets
                        + How to derive association rules
                                       
        + FP-Growth:
                + Why use it?
                + How to mine association rules
        + Derive association rules from the frequent itemsets

## 5.1 Basic Concepts
+ 看下P5的例子
+ Threshold:
        + support(X U Y) : 同时包含XY的概率
        + confidence(X -> Y) : 包含X的条件下包含Y的概率
        + 对rule A->C # 出现A的前提下C也出现的概率
                + support(A U C) = P(A and C)
                + support(A) = P(A)
                + conf(A,C) = support(A U C) / support(A) = P(AC) / P(A)
+ '一个栗子' 以前的期末考试:
        + conf(None -> A) = sup(None U A) / sup(None) = sup(A) / 1 = sup(A)
        + conf(A -> None) = sup(None U A) / sup(A) = sup(A) / sup(A) = 1
        + sup(None) = 1, 因为任何集合都包含了空集, 可以认为空集出现的概率为 1
                

+ 给定最小support和confidence作为threshold:
        + 频繁项集为support不小于min_support的项集, 例如min_support = 0.5, sup(AC) = 0.5即为一个频繁项集
        + 关联规则为频繁项集中满足min_conf的规则
                + E.G. min_confidence = 0.7
                + 假若对之前的频繁项集{AC}, A->C (0.5,0.6), C->A (0.5,0.7)
                + 括号内前面的数字为support,之前已经验证满足min_support了
                + 括号后面为confidence, 可以看出C->A为一条关联规则 
                
+ 挖掘关联规则: 使用aprori或者fp-growth得到频繁项集, 然后基于频繁项集生成关联规则
+ 总共会有多少个candidates呢: C(5,0) + C(5,1) + C(5,2) + C(5,3) + C(5,4) + C(5,5)

## 5.2 Apriori
+ Apriori property: 任何频繁项集的子集也是频繁项集
        + 例如P(ABC) > 0.5, P(AB) 也一定 > 0.5
        + 逆反命题: 若一个项集不是频繁的, 包含其的项集也不是频繁的
+ Arpiori算法原理 :如果我们判断AB不是频繁的, 我们就不需要花时间搞ABC,ABD,...了
        + 首先寻找单个的项集并计算support, 排除其中不满足min_sup的, 得到一阶频繁项集
        + 基于一阶频繁项集构建二阶项集(只能包含一阶频繁项集中元素), 然后重复之前的步骤得到二阶频繁项集
        + 重复上述过程直到找到最高阶频繁项集
        # 其实就是个从一般到特殊的过程，一般的都过不去就不搞特殊的了
        
+ 'P15'几个重点:
        + 生成项集: self-joining上一层元素, then pruning(移除不存在的)
        + 合适的频繁项集: 自己的任何一个子集都是频繁项集
        + 例如'P14'从 L2 可以生成{ABC,BCE,ACE},但ABC的子集AB不行, ACE的子集AE不行, 最后就剩下BCE

+ 从频繁项集中得到规则:
        + 对频繁项集ABC, 需要判断A->BC,B->AC,C->AB,AC->B,AB->C,BC->A是否为关联规则
        + 给定频繁项集X, 对X的任何一个非空子集A, 我们需要判断A->X-A是否为关联规则, 即conf(A,X-A) > min_conf
        
+ 这里引出FP-Tree: Apriori得到频繁项集的过程有点费时间, 而获得关联规则真的需要频繁项集么

## 5.3 FP-Tree
+ 构建 'P34-41' # http://www.cnblogs.com/zhangchaoyang/articles/2198946.html
        + 先把每个条目中的频繁元素找出来，删去不频繁的，然后按频繁程度降序排序 'P34'
        + 构建FP-tree 'P35'
        + 头表与FPtree相连
+ 关联规则挖掘: e.g. [f,c,a,b,m,p]
        + 从头表最后一个元素开始(i.e. p)
        + 找到p的CPB, CPB是以该元素为结尾但不包括该元素的单链或者树, 将CPB上的元素count设置为与p相同:
                + fcam:2
                + cb:1
        + 在CPB中寻找符合min_sup的元素(c:3),和p一起组成二阶频繁项集: pc
        + 对这些元素递归式构建fp-tree, 由于只有单链 --> 返回pc, pc已经存在, 停止
        + 在头表中删除p, 对下一个元素m继续刚刚的过程
+ FP-Growth is much faster than Apriori # P43
        + 分治算法
        + 不需要生成所有的项集, 也不用检验他们是否是频繁的了
        + Compressed structure
        + No repeated scan of entire database
        + basic ops—counting local freq items and building sub FP-tree, no pattern search and matching


#%#%#%#%#%#%#%#%#%#%#$%#%#%#%#%#%#%#%#%
######### 6. Recommendation System
+ Overview: 
        + Problem definition
        + 3 Kinds of RS: pros? cons?
                + Content-based
                + Collaborative filtering; pearson correlation
                + Matrix factorization-based; stochastic gradient descend.
        + Variants of Matrix factorization
        Exception: detailed model
        
## 6.1 Problem definition
+ Formal Model: X(Customer) * S(Items) --> R(Recommandation)
        
+ Unity Matrix
+ Key problems: 获取已知评分/推测未知评分/评估系统性能
        + How to gather known ratings for utility matrix
        + How to predict unknown ratings from known ones
                + Utility matrix maybe sparse --> 大部分人不打分, 除非那些特别惹眼的
                + Cold start --> 如何处理新物品和新用户
                + 3 approaches:
                        + Content-based
                        + Collaborative filtering
                        + Latent factor based
        + How to measure the performance
        
## 6.2 Content-Based RS --> 根据相似物品打分推荐
+ 我给某些项目打了高分, 下次向我推荐类似的项目
        + 对于某用户打高分的项目, 获取它们的item-profile
        + 根据对item-profile的分析, 得到该用户的user-profile
        + 对于某新项目, 若其item-profile符合该用户的user-profile, 进行推荐
+ 对每个item创建item profile(特征集), 然后用TF-IDF获取需要的features
+ TF-IDF : 'P14 用于文本挖掘' 
        + What is TF_{ij}
                + f_{ij}: item j 中term i出现的频率
                + 'TF_{ij} = f_{ij} / max_kf_{kj} # 需要的term的频率 / 该term中最频繁的term的频率'
        + What is IDF_i
                + 'IDF_i = log(所有items / 出现term_i的items)'
        + TF-IDF score: 'w_{ij} = TF_{ij} * IDF_i'
        + 最后得到的item profile为一系列有着最高TF-IDF score的terms以及score
+ Prediction: 
        + Input: user profile x, item profile i
        + Output: u(x,i) = cos(x,i) '这里使用cosine计算相似度'
        + 之前通过TF-IDF得到了一个项目的item-profile, 对于一个用户, 获取他打分较高的items, 根据item-profile找规律构建user-profile, 对于新项目, 先获取这个项目的item-profile, 然后计算和user-profile的相似度进行打分
        
+ Pros:
        + 不需要从别人那里获取信息, 只需要考虑当前的人和给定的项目 --> no cold start
        + 可以满足那些爱好特殊的用户(unpopular tastes)
        + 可以推荐小众产品(unpopular items) --> no first-rater problem
        + 可以为推荐提供解释, 可解释性强(list the content-features)
+ Cons: 
        + 不好找features, 图片音乐电影什么的features都是不一样的, TF-IDF仅适用于文本资料
        + 对于新用户不好提供推荐(新用户没给项目打过分, 没法构建user-profile)
        + Overspecialization
                + 只能推荐和用户之前喜好类似的项目
                + 推荐被局限在user-profile, 而用户的爱好可能是多样的
                + Unable to exploit quality judgments of other users

## 6.3 Collaborative Filtering --> 根据相似人的打分推荐
### 6.3.1 User-User 
+ 找到和我类似的用户们, 假若他们都喜欢吃饭睡觉打豆豆, 那我也应该喜欢吃饭睡觉打豆豆
+ 用户相似度评估 'P20 注意'
        + 用户x的数据r_x为其对一系列物品的打分: [3,1,5,_,2,...]
        + Jaccard similarity measure: '注意和第八章的区分下,第八章度量不相似度, 这里度量相似度'
                + 打乱顺序, 化为集合
                + J(A,B) = (A and B) / (A or B) = 11 / (01 + 10 + 11)
                + 缺点是ignore the value of ratings, 例如只要有打分相同的, 就算作一样哪怕不是用一部电影
                + e.g. A = [4,_,_,5,1,_,_], B = [5,5,4,_,_,_,_], C = [_,_,_,2,4,5,_] 
                        + A = {4,5,1}, B = {4,5}, C = {2,4,5}
                        + sim(A,B) = 2/3, sim(A,C) = 1/2 --> AB相似度更高
        + Cosine similarity measure
                + 空值算作0
                + C(A,B) = <A,B> / <||A||*||B||>
                + 缺点是不好判定缺失值, 没打分的当负数
                + 解决方法: 标准化(提前减去行均值)
                + e.g. 
                        + A = [4,_,_,5,1,_,_] 
                        + 均值为10/3 , A = [2/3,_,_,5/3,-7/3,_,_]
                        + 空的算作0 --> A = [2/3,0,0,5/3,-7/3,0,0] 
        + Pearson correlation coefficient
                + 就是计算相关系数咯, 要提前求出A,B的平均值, 然后用下面的公式
                + P(A,B) = Cov(A,B) / sqrt(Var(A) * Var(B))
                + 注意同样需要减去平均值, 然后把缺失值设为0
                + 看起来这个是三个里面表现最好的
                
+ 先构建相似度矩阵(任意两个用户的相似度), 然后根据相似度矩阵预测推荐
        + 这个类似knn
        + 对于用户x, 项目i
        + 先找到与x最接近的k个用户, 他们对i打分的权重平均值, 即为x对i的打分预测
        + r_{xi} = sum(sim(x,y) * r_{yi}) / sum(sim(x,y))

### 6.3.2 Item-Item
+ 喜欢吃饭睡觉的人多半喜欢打豆豆, 感觉这个有点像关联规则, 寻找相关性比较密切的项目
+ 对于某个用户x, 某个item i, 先找到和i类似的项目, x对这些项目打分的权重平均值, 即为对i打分的预测
        + 计算项目相似度然后得到相似度矩阵
        + r_{xi} = sum(sim(i,j) * r_{xj}) / sum(sim(i,j))
+ 'P24-28 Item-Item CF注意看下'
        + 行为电影, 列为用户, 我们需要预测用户5对电影1的打分
        + 找与电影1最接近的2部电影
        + 计算余弦相似度(记得先减去均值)
        + 然后我们可以发现和电影1最相似的两部电影是电影3(0.41)和电影6(0.59)
        + 用户5对这两部电影的打分为 2,3
        + 因此我们可以预测用户5对电影1的打分为 (0.41 * 2 + 0.59 * 3) / (0.41 + 0.59)
+ 'P29' II实际使用中的公式, 需要baseline --> 防止过于极端的情况出现
+ 一般II比UU表现要好, 因为人的爱好太特别了, 项目要相对简单

+ Pros:
        + 不需要进行特征选择, 可以搞定任何类型的项目
+ Cons:
        + Cold Start : 需要初始数据集(一大堆用户推荐), 没法冷启动
        + Sparse Matrix : 不容易寻找打分相似的用户
        + First Rater: 对于原来从没出现过的项目, 没人为其打过分, 就傻逼了
        + Popularity bias: 
                + 如果一个人的爱好很特别 --> 强行找类似, bias很大
                + 倾向于推荐人民群众喜闻乐见的
 
### 6.3.3 Hybrid Methods
+ 多种推荐系统的结果综合下
+ 在协同过滤中添加基于内容的方法
+ 这里的问题主要是平衡多种推荐系统的话语权
 
## 6.4 Evaluate the system
+ 评估方法:
        + RMSE: sqrt(MSE)
        + Precision of top 10
        + Rank Correlation
+ 在实际应用时我们只能预测这些高评分的项目: RMSE会惩罚对高评分项目表现好但低评分项目表现差的模型
+ 复杂度: 主要是KNN部分比较费时间
+ 数据量多多益善

## 6.4 Latent factor Model
'P53-74'


'不考SVD'

+ LFM is based on SVD: 
        + 'P54' R = Q(items-factors) * PT(factors-users)
                + 这里的factors实际上被隐藏, 因此是隐语义模型
        + SVD isn’t defined when entries are missing
        + 通过特殊化方法来找到P/Q
                + PQ将user/movie映射到隐语义空间
        + Goal: min(sum((r_{xi} - q_i * p_x)^2)) --> minimize SSE
+ How to find the latent factors: # cols in Q, rows in PT
        + 我们的目标是最小化SSE, 这个模型倾向于过拟合
        + regularization: 
                + 添加正则项: min[error + lam * length] 
                + \lambda * [sum(|p_x|^2) + sum(|q_i|^2)]
+ SGD: 
        + Init P and Q, missing values are 0
        + GD: for each step compute all ratings, then update:
                + P := P - lr * partial_P
                + Q := Q - lr * partial_Q
                + here lr is learning rate   
        + SGD: 2 for-loops 'P73 这里需要记一下'
        for until convergence
                for each r_{xi} 
                        + e_{xi} = 2(r_{xi} - q_i * p_x)
                        + 'q_i := q_i + miu_1 * (e_{xi} * p_x - 2 * lr2 * q_i)'
                        + 'p_x := p_x + miu_2 * (e_{xi} * q_i - 2 * lr1 * p_x)'
                        + here miu is learning rate
        + SGD VS GD:
                + GD每次更新需要计算所有ratings, 而SGD每次就一个rating
                + SGD 小碎步瞎鸡巴走(improve the value in a noisy way), 大方向对, 虽然需要迭代次数更多, 但计算更快 
        + 注意更新过程中几个参数同时更新, 更新中用到的都是旧参数
 
## 6.5 Matrix factorization
+ 'Variations : low-rank / k-means / non-negative'


+ 定义: 给定M, 找到两个矩阵UV满足
        + M 近似等于UV
        + U,V都满足某些约束条件
+ 栗子:
        + Low-rank matrix factorization, 例如推荐系统
                + 矩阵M(m*n) ~ U(m*k) V(k*n)
                + Loss function: ||M - UV||^2
                + 约束: rank(U) and rank(V) <= k << min(m,n)
        + K-means
                + 矩阵M(m*n) ~ U(m*k) V(k*n)
                + Loss function: ||M - UV||^2
                + 约束: 行列都必须是独热编码
                
        + Non-negative Matrix Factorization, 例如计算机视觉和文件聚类
                + M(m*n) ~ U(m*k) V(k*n), 注意M > 0
                + Loss function: ||M - UV||^2
                + 约束: U > 0, V > 0




        
        
