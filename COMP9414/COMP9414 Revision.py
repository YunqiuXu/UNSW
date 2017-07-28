# COMP9414 Revision
# I will reverse the chapters

# ------------------------------------------------------- #
# Q10 Uncertainty and Probability (W11)
+ 这章讲的概率之类的东西，不确定性，贝叶斯等等
+ 最一开始讲环境的时候有提到真实环境是stocastic & partial observable的 --> 信息不完整导致不确定性
+ 处理不确定性:
        + Default or nonmonotonic logic: Assume ...
        + Probability
        
+ 随机变量 / 概率分布
+ propositions(命题), 看下'P13'的格式
+ Prior / Joint / Conditional probability
+ 'P20' Joint Distribution
+ Conditional Independence
        + P(A|X,Y) = P(A|X)
        + P(A,B|X) = P(A|X)P(B|X)
+ Bayes Rule: 看下'P33'的栗子

+ 本部分练习题已完成

# ------------------------------------------------------- #
# *** #
# ------------------------------------------------------- #
# Q9 Perceptrons and NN (W10)
+ 线性可分 Perceptron 'P14' update the parameter
        + 1 misclassified as 0: need to make w larger
                + wk := wk + nxk
                + w0 := w0 + n
        + 0 misclassified as 1: need to make w smaller
                + wk := wk - nxk
                + w0 := w0 - n
+ Perceptron 无法处理非线性分类: e.g. XOR 
+ Multi-layer: forward pass and backward pass 'P29'

+ 本部分练习题已完成

# ------------------------------------------------------- #
# *** #
# ------------------------------------------------------- #
# Q8 Decision Tree (W9)

+ ID3 : Cross entropy, information gain
+ Laplace smoothing计算error 
        + E = 1 - (n+1) / (N+k)
        + 这里n指的正确分类的, 即主要类别
        + 那么问题来了, 既然是主要类别那还平滑个鸡巴
+ Pruning: minimal error
        + 判断剪枝前后错误率会不会提升
        + 'P25-26'看下比例
+ 本部分练习题已完成

# ------------------------------------------------------- #
# *** #
# ------------------------------------------------------- #
# Q7 Propositional and FOL (W8)
+ Logic agent: knowledge base, logical inference --> rules
+ Wumpus的栗子: 如果(1,2)有风, 则(1,3), (2,2), (1,1)中会有至少一个有怪兽, 不然这个风就没意义了
+ Knowledge base(KB): a set of sentences in a formal language. It takes a
Declarative approach to building an agent
+ KB Agent:
        + represent states, actions
        + incorporate new percepts
        + update internal representations of the world
        + deduce hidden properties of the world
        + determine appropriate actions
+ Model : m is a model of a sentence A if A is true in m
        + 构建模型: 先列真值表
        + KB对模型一定对, 模型对KB不一定对, KB包含在模型内部
+ Entailment: KB |= a
        + 意思: KB |= a iff KB -> a is valid 
        + e.g. (x+y = 4) |= (4 = x+y)
        + 对于模型M, 当且仅当M(KB) in M(a) 时, KB |= a才成立
        + KB = 规则 + 观察
'真值表找模型':
        + {A,B} 代表A = T, B = T时满足KB为T --> 因此是一个合格的模型
        + {} 代表所有变量都为F时KB为T --> 也是一个合格的模型
        + 如果KB本身就是Valid的, 那么所有模型都是True({AB}{A}{B}{})        

+ 'P16'栗子: 已知(1,1)安全
        + KB = (2,1)有风, a = (1,2)安全 --> KB |= a
        + a = (2,2)安全 --> KB |!= a
+ 命题逻辑: 可以复习下9020
        + CNF : and
        + DNF : or
        + Implis: A -> B 等价于 not A or B
        + A <-> B 等价于 A -> B and B -> A 
        + Generalization : P -> P or Q
        + Specialization : P and Q -> P
        + 逻辑等价: A |= B and B |= A
        + Satisfiable and Validity
        + Soundness and Completeness: 'P28'
+ 'Resolution的玩法': 这里举个栗子, 用 not H 简化 M and H
        + not H and (M and H) --> not H and M
        + 简化后, 再把 not H 从 not H and M中削去 --> M作为分母
        + 表示为: not H and (M and H) 横杠 M
+ 'Horn Clause':
        + 先把命题转换为CNF ... and ... and ...
        + 加入需要证明的命题的反证形式
        + 一个个看成不成立
        + Forward chaining(data driven) and backward chaining(goal driven)
        + 若最后发现不成立 --> 反正不成立 --> 原命题成立
+ 命题逻辑的不足: 把命题分解成了一堆小句子, 改进 -> FOL
        + FOL = objects + predicates + functions
        + E.G.1 对于任何男人, 有小鸡鸡 and 有胡子
        + E.G.2 存在男人, 有小鸡鸡 or 有胡子

+ 本部分练习题已完成

# ------------------------------------------------------- #
# *** #
# ------------------------------------------------------- #
# Q6 Constraint Satisfaction (W6)
+ 地图着色 / 八皇后问题 / 密码计算 / 数独
+ 三要素: variable / domain / constraint
+ 回溯法(试错思想) : 搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径
+ 路径搜索与约束搜索的区别:
        + 约束搜索不知道目标, 但容易找到路径
        + 路径搜索有明确目标, 但路径不好找
+ 变量赋值:
        + MRV: 最小剩余值, 选择约束最多的变量赋值(让自己无路可走)
        + Degree Heuristic: 给变量赋值时, 尽可能增加剩余变量的约束(让后人无路可走)
        + LCV: 给变量赋值的时候尽可能让约束最少(让后人的路更多)
+ 冲突检查:
        + Forward checking: 
                + 先确定第一个的颜色, 然后第二个, 第三个...
                + 直到遇到没法选的
        + Constraint propagation: 
                + 类似前项检查, 和前项检查相比, 可以尽早查到不满足约束的, 更早停止
                + 每次更新都检查下是否有不满足约束的, 一旦发现冲突就停止
        + Arc consistency: 
                + 有点像特殊的约束传播
                + 不仅检查不满足约束的, 还排除一些会造成冲突的值
                + 'X --> Y consistant: 对每个X取值, 都可以取到y保持和谐'
+ 局部搜索: 八皇后问题:
        + 随机初始化
        + 每次变动一个变量
        + 局部搜索/爬山算法: h为错误数量, 每次改一个看会不会优化, 优先选择冲突最少的改动

        + 改进: 模拟退火, 各个方向都走, 小方向可能有偏差大方向正确
                + 要是下降--> 立刻下降(h1 is lower than h0)
                + 要是上升, 可能两边走
                + P = e ^ {- (h1 - h0) / T} # h1 is new, h0 is prev


# ------------------------------------------------------- #
# *** #
# ------------------------------------------------------- #
# Q5 Games (W5)
+ Game Tree: 类似宽度优先, 给出所有可能
+ Minimax 'P16'
+ alpha-beta pruning
        + alpha part: if alpha >= beta, return alpha 
        + beta part: if alpha >= beta, return beta
+ 会画图, 会分析时间复杂度
+ Expectimax: 
        + 在dice layer计算乘概率后的值
        + 可以计算exact value
        + max - chance - min
        + 看下这个的剪枝



# ------------------------------------------------------- #
# *** #
# ------------------------------------------------------- #
# Q4 Hruristic Path Search (W4)
+ f(n) = g + h
        + g : try to be closest from start
        + h : try to be closest to goal
        h = 0 --> only g, ucs --> optimal but not efficient
        g != 0 and h != 0 -->  
        g = 0 --> only h, greedy --> efficient but not optimal
+ A* / IDA*(low memory)
+ h() is admissible: 真实路径永远不小于h(), 启发式得到的路径是最短的
+ h1 domianate h2: 都是admissible的, h1 的值 >= h2
        e.g. Manhattan >= Eculidean >= Chebeshev
+ Goal: 在满足admissible的基础上尽可能大
+ 8-puzzle

!!!!!!!!!
+ Greedy : f = h, 效率高, 但是incomplete and non-optimal
+ Best first search: f = g, 包括UCS/DFS/BFS # 注意greedy 和 best first search不一样
        + BFS是UCS的特殊形式: 每条边权重相同的UCS
        + UCS/BFS 是完全和优化的, 但效率低
        + DFS: f = -g
+ A*: f = g + h, 完全和优化的
+ IDA* / IDS: 完全和优化的, 省空间
+ admissible / dominate

# ------------------------------------------------------- #
# *** #
# ------------------------------------------------------- #
# Q3 Path Search (W3)



# ------------------------------------------------------- #
# *** #
# ------------------------------------------------------- #
# Q2 Prolog



# ------------------------------------------------------- #
# *** #
# ------------------------------------------------------- #
# Q1 Environment / Agent (W1)



# ------------------------------------------------------- #
