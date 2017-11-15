# Reinforce Learning and DQN
# 可以参考周莫烦的视频教程
# 算法综述: http://blog.csdn.net/mmc2015/article/details/55271605



# 1. DQN
1.1 为什么使用: 
+ 虽然lookup table 保证收敛, 但对于复杂的实际问题, lookup table不足以存储繁多的状态
1.2 类似Q-learning, DQN的更新为 'p12'
+ 最小化Q-l中括号里面的部分的平方
+ 使用一系列Qw进行学习, 最终得到最佳策略 # 可参考之前AC的笔记
+ 梯度仅仅对 Qw(st,at) 这部分起作用
+ 还是不足以解决雅达利游戏: temporal correlations between samples --> 选取了相似的样本不利于学习
1.3 Experience Replay: 
+ 构建经历数据库 <s_t, a_t, r_t, s_t+1>, 随机采样学习, 打乱经历之间的相关性, 防止样本间的temperal correlations

# 2. DQN Improvements
2.1 Priorised Replay
+ weight experience according to surprise --> 赋予经验样本权重, error大的优先度高
+ error即为之前中括号内容的绝对值!
+ 优先学习Q预测值与实际值偏离大的
+ 在正负样本不对称的情况下, 可以更有效地找到需要学习的样本
    
2.2 Double Q-Learning
+ 相同的网络(权重)用于选择动作和评估动作 --> confirmation bias (over estimation), 即Q值过大
+ 因此使用两个网络:
    + w_new: 当前权重, 用于选择动作
    + w_old: 旧权重, 用于评估动作
+ 如何得到w_old: periodically calculated from distributed values of w
2.3 Advantage Function (Dueling DQN)
+ 普通DQN的Q值独立于action, 无论做什么动作对下一个状态没什么影响 : Q(s,a) = V(s)
+ 这里加入Activantage function : Q(s,a) = V_u(s) + A_w(s,a)
    + A(s,a): 在状态s选择动作a的好处或坏处, 用这个函数选择动作
+ 当可用动作越高, 学习难度就越大, 不过 Dueling DQN 还是会比 Natural DQN 学习得更快. 收敛效果更好
        
## 3. Actor-Critic
+ 为什么用: PG适合回合更新, 对于non-episodic, 难以估计Q_pie_theta(s,a), 因此我们按照上次课件里说的, 选取一系列Q函数Q_w不断学习逼近Q_pie_theta, 在这个过程中, 策略pie_theta也被学习了
+ 因此我们引入AC: 使用PG选取动作, 使用Q函数进行评估
+ 看下'P20'的伪代码
    + 取样: r_t, s_t+1, a_t+1
    + 更新: dE/dQ, theta, w

## 4. A2C
+ 加入Advantage的AC

+ Advantage Actor Critic: 'p21'
    + 加入了advantage function 和 AC
    + DDPG: Google DeepMind 提出的一种使用 Actor Critic 结构, 但是输出的不是行为的概率, 而是具体的行为, 用于连续动作 (continuous action) 的预测. DDPG 结合了之前获得成功的 DQN 结构, 提高了 Actor Critic 的稳定性和收敛性
    
## 5. A3C
'P22'
+ 使用PG选择动作
+ 使用TD value function 计算V_u(s)
+ 使用n-step sample估计Q(st,at): 这个类似infinite discount, 只不过有上限n
+ 更新策略theta: 和之前的不同之处在于, 把'Q_w(st,st)'换成了'Q(st,at)-V_u(st)'
+ 最后, 更新价值函数(Q - V_u)^2

## 6. 爬山 --> 看上一节课的就好

## 7. Evolutionary Computation algorithms
+ 这个还是要看下的, 可能会考!!

## 8. Variational Inference / KL-Divergence
+ 这个在RBM和VAE那边也有, 日!
    
