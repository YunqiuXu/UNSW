# RL
1. 监督学习和强化学习的区别
+ 监督学习的数据集给定或连续或离散的label, 对输出数据进行预测或分类
+ 强化学习没有特定label, 目标是最大化输出的reward
+ 监督学习搞不定的:
    + 优化控制
    + 资源分配
    + 这些都没有明确目标 --> 使用强化学习最大化reward
    
2. 强化学习的框架
+ 与环境互动的agent
+ 状态集合S, 可选动作集合A
+ 对于当前时间t, agent从环境获取当前状态s_t, 选取动作a_t, 进入下一个状态s_t+1, 同时得到这一过程的回报r_t
+ Policy S->A: 找到最优化的策略p用于最大化累积回报
+ R(s,a): 回报函数, 计算在状态s下采取动作a能获取的回报
+ delta(s,a): 状态函数, 计算在状态s下采取动作a会得到的下一个状态

3. 优化模型: 'p7-8'
+ Finite horizon reward: 直接加和所有的reward, 易于计算
+ Infinite discounted reward: 加和reward时设置一定的权重(幂), 越远的权重越小, 理论易于推导
+ Average reward: 加和所有reward后取均值, 不容易实现, 因为还需要考虑非常非常远的reward

# P8的例子 k = 4, r = 0.9
+ finite horizon: r0 + r1 + r2 + r3
+ infinite discount: r0 + 0.9 r1 + 0.81 r2 + 0.729 r3 ...
+ average: r1 + 1/2 (r1 + r2) + 1/3 (r1+r2+r3) + 1/4 (r1+r2+r3+r4) ...

4. 强化学习分类:
+ 基于Value function的:
    + TD
    + Q
+ 基于Policy的:
    + 爬山
    + Policy Gradients
    + 进化
+ AC:
    + 前两个的结合, 一个用于选取动作, 一个用于价值评估
    
# 5. 基于value的学习
'注意下优化策略的定义'
5.1 Value function { V_pie: S -> R }: 给定策略pie 和 状态s, 用于计算reward r的函数
    + V_pie(s): average discount reward begins at state s and chooses action based on policy pie
    + V_pie*(s): value for optimal policy, i.e. the largest average discount reward obtained from start s
    + 价值函数的目标 'bootstrap过程': 随机选取一个value V, 在之后的迭代中不断提升V, 令最终得到的V尽可能接近最优的V
    + 一个典型的例子是K-多臂机器人: 每个动作会有不同的reward, 我们的目标是制定最佳决策以最大化累积回报
5.2 exploration - exploitation tradeoff
    + 在某些时间随机选取动作, 其他时间选取value最大的动作(softmax) --> 想想我们的作业
    + 在5%的时间里随机选取动作, 其余时间遵循Softmax(玻尔兹曼分布)
5.3 TD learning: 'P16'
    + 时间差分学习和MCMC的区别: TD是单步更新, 而MCMC是每回合更新, 因此TD的学习效率更高
    + 当状态函数和价值函数都是determistic的时候, 怎么计算价值
        V(st) <- rt + r V(st+1)
    + 当这两个函数都是stocastic的时候, 怎么计算价值 # 加一个学习速率
        V(st) <- V(st) + eta [ rt + r V(st+1) - V(st) ]
        
5.4 Q learning: 和TD学习类似, 只是用于计算价值的函数为Q函数
    + 之前的价值函数只输入状态, 根据状态获取价值
    + {Q_pie: S x A -> R}, 输入状态和动作
    + 看下'P17'的推导过程
    + 同样的, 看一下determistic和stocastic情况下计算Q value的区别'P18'
    + 'P19看下, 可能涉及计算!'

5.5 Value-based的优缺点:
+ 优点: 无论是TD还是Q, 最终都会收敛到最优状态, TD和Q都是单步更新, 主要区别是一个价值函数只考虑状态V(s), 另一个价值函数需要同时考虑状态和动作Q(s,a)
+ 缺点:
    + Delayed reinforcement: 因为需要考虑未来的动作, 因此当前动作的reward没法立刻得到, 结果是学习的速度会变慢
    + Finite search space:
        + 搜索空间很大的话, 不容易收敛
        + 对于每个状态都需要没完没了地访问
    + 真实环境下, lookup table是不适用的 --> need generalisation
5.6 如何选择target value:
+ 对于监督学习: behavioral cloning, 就是收集人类数据集进行拟合
+ 对于TD: 
    + 使用subsequent positons来refine the estimation of curr posiion
    + 不依赖于world model(游戏规则), 可以复习下9414的"known and unknown"
+ 结合学习和tree search --> 依赖于world model: TD-Root / TD-Leaf / MCTS ...

5.7 td for episodic 'P27'
+ episodic: 只有游戏结束才能获得reward, 这样单步更新其实跟回合更新没啥区别了
+ TD(lambda): 使用Tk作为Vk的训练结果

# 6. 基于策略的学习
1. PG可以根据奖惩情况来左右反向传递
+ 选择了动作1, 但reward信息显示是不好的动作 --> 减小反向传递力度 --> 下次被少选一点
+ 选择了动作2, reward信息显示是好动作 --> 增大反向传递力度 --> 下次被多选一点
+ 日这特么跟感知机更新差不多呀

2. 与基于价值的学习的区别: 不对价值函数进行优化, 而是直接优化策略本身
+ { pie_theta : S -> A } : 输入状态, 输出动作, 而不是之前的reward
+ 优化策略参数theta, 以得到最佳策略pie
+ 一个例子是爬山算法, 爬山是策略的一种, 可以到达局部最优态
3. Policy Gradients for episodic: 'P31'
+ 只有游戏最后才会获得价值r_total
+ PG 是爬山算法的一个替代品, 爬山算法随机更新, 而PG使用梯度上升
+ 看下那俩公式
+ 'P32'算法伪代码: 每次更新的是策略的参数
4. PG for non-episodic: 'P33' 
+ 每个动作都能获得价值, 比如吃豆人
+ 每个策略都是关于S的分布函数
+ log trick

#7. AC
+ AC是基于价值和基于策略的结合
+ 使用策略选取动作 --> actor
+ 使用价值评估动作 --> critic
    
    
    
    
