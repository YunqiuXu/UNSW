# 受限玻尔兹曼机
+ 除了课件的ref: 
    + http://blog.csdn.net/xbinworld/article/details/44901865
    + http://blog.csdn.net/xbinworld/article/details/45013825
    + http://blog.csdn.net/xbinworld/article/details/45128733
    + http://blog.csdn.net/xbinworld/article/details/45274289

## 1. Hopfield Network
+ 基于能量的模型: 趋向能量降低 --> 局部最优
+ Hopfield Network 'P6'
    + 神经元xi并非连续的, 而是取离散值: 正负一
    + 权重: wii = 0, wij = wji
    + 神经元基于current values of neighbouring neurons被迭代更新
+ 设置一个初始状态x, 每次迭代反转一个神经元的值(e.g. 1 --> -1), 最终停留在低能状态(局部最优)
    + sum(wij * xj) + b_i > 0 --> 设置为1, =0为xi, <=为-1
+ 看下'P8-9'的栗子: Hebbian learning
+ 可被存储在Hopfield中的Pattern数量p与网络中神经元数量成比例(e.g. p/d < 0.138)
+ 该网络用于store and retrieve特定项目 --> 由此可引出生成式模型 --> RBM

## 2. Boltzmann Machine
2.1 与Hop的异同
+ 与Hopfield能量函数长得很像
    + 有重复地选取一个神经元xi, 决定是否对其进行反转(改变状态)
+ 区别:
    + xi 取值为0/1而非正负1
    + 用于生成新状态, 而非提取旧状态(Hop)
    + 更新不是deterministic的 --> 使用sigmoid进行stocastic update
        + 对于hopfield, 绝对不会跃迁到高能级 --> 因此会得到局部最小
        + 对于Boltzmann, 通过一定概率翻转
        + 很像爬山和模拟退火的区别
+ 说白了, BM的操作类似Hop, 但是神经元更新存在一定随机性, 而不是像Hop那样是determistic的
    + 对Hop: 只有delta_E <= 0时才更新
    + 对BM: 两种更新都以概率方式表示, 即使是小概率事件也可能发生

2.2 玻尔兹曼分布: 状态空间的概率分布函数 'P13'
+ 其中分母为partition function, 类似Softmax, 保证概率加和为1 --> 不容易计算
+ 替代 'Gibbs Sampling' : 
    + 基于临近states的相对概率, 在分布函数中采样
    + p = 1 / (1 + e ^ k), k = - delta_E / T
    + 对某一个神经元xi, 获取将其翻转为1或0的概率: P(xi=1), P(xi=0)
    
+ 多次迭代后we can obtain a sample from Boltzmann distribution: 
    + 若T接近于无限, 取01的可能性相等 --> 正太分布
    + 若T接近于0, 等同于Hopfield, 不允许能量增加
    + T温度需要保持固定, 否则一开始虽然会高但最后会减少(模拟退火)

2.3 BM的不足
+ 每个单元的prob必须为关于周围单元的线性可分函数
+ 如果可见单元(input)和隐藏单元(hidden)完全可分的话BM会很牛逼: 若input-to-input / hidden-to-hidden, 训练时间太长
+ 因此引入RBM, 以二分图的形式直接把输入层和隐藏层分开

     

## 3. RBM
3.1 结构:
+ 受限: 每个神经元的概率必须是周围神经元的线性可分函数
+ RBM中输入层和隐藏层可以看作一个二分图
    + 隐藏层通过学习一些隐藏特征, 对输入的数据分布进行建模
    + 不存在vtv / hth, 输入层所有与隐藏层所有相连
+ 为什么用二分图 # 也可参考2.3
    + 若输入层单元相连或者隐藏层单元相连, 训练时间过长
    + 因此我们加入限制: 只允许visible-to-hidden
3.2 能量函数: 'P18'
'E(v,h) = - sum_i(bi * vi) - sum_j(cj * hj) - sum_ij(vi * wij * hj)'
+ vi: 输入层第i个神经元的状态 # 注意为binary vector
+ hj: 隐藏层第j个神经元的状态
+ bi: 输入层第i个神经元的bias
+ cj: 隐藏层第j个神经元的bias
+ wij: 即隐藏单元i和输入单元j的连接权重
+ 训练目标: 最大化输入数据的expected log probability
    + 分布: P(hk = 1 | v), P(vk = 1 | h)
3.3 Alternating Gibbs采样
+ 根据每一个分量的相对于其他分量的条件概率P(Xk|X−k)，对该分量进行采样
+ 在玻尔兹曼分布中根据以下规律采样:
    + v0: 随机选取
    + h0: 从p(h|v0)中采样
    + v1: 从p(v|h0)中采样
    + h1: 从p(h|v1)中采样
    + ...
3.4 另一种训练手段: Contrastive Divergence 'P22未看, 注意这个会考!'    
+ 这个和word2vec中的negative sampling有些像: 并不能保证收敛到最佳, 但实际效果不错
+ 步骤:
    + 1. 从训练集中选取一个或多个正样本{v^(k)}
    + 2. 对每个正样本v^(k), 从p(h|v^(k))中选取h^(k)
    + 3. 使用A Gib Sam生成假样本{v-^(k)}
    + 4. 更新bi, cj, wij
        + bi <- bi + eta(vi - vi_fake)
        + cj <- cj + eta(vi - vi_fake)
        + wij <- wij + eta(vi*hj - vi_fake*hj_fake)
    + 训练目标: 提升log p(v^k, h^k) - log p(v_fake^k, h_fake^k)
+ 快速版本'P23'
    + take just one additional sample instead of running for many iterations # 加速这一过程
    + 其实就是不像之前那样选取一个或多个了, 就选取一个
        + v0, h0为正样本 --> v1, h1就是负样本
        + 采样 -> 重构 -> 采样 -> ...

## 4. BM的用途: Greedy Layerwise Pretraining
+ 成对的层被当作RBM训练 --> 结果被用作初始权重和偏置
+ 注意后面AE也可以做这个

    
