# Autoencoder

## 1. Autoencoder networks
+ 之前讲的encoder network: 
    + N-M-N task, M相当于一个bottleneck(hidden layer)
    + 用于investigate hidden unit representations
+ Autoencoder: 'P4'
    + 全链接结构 : input -> [encode] -> hidden -> [decode] -> output
    + 目标: 令output尽可能接近地复现input
    + 经过hidden layer(bottleneck) : 数据被压缩
    + 与RBM的相似之处: 都用于自动提取输入数据的抽象特征
    + Loss function: 最小化input和output的distance
        + encoder : z = f(x)
        + decoder : g(f(x))
        + E = L(input, output) = L(x, g(f(x)))
    + 可以用于预训练, 之后去掉解码器, 加上别的神经网络 --> 自动编码器学到的特征可以当作其他网络初始化的权重
    
+ Greedy Layerwise Pretraining: Autoencoder 可替代 RBM
    + 先使用单隐藏层AE重建输入 --> encoder层作为之后深度网络的第一层
    + 训练每个subsequent layer用于重建前一层
    + 在最后加上分类层, 并使用反向传播训练整体
    '逐层训练网络的每一层,从而对整个网络进行权重初始化'
    '第一次训练单隐藏层, 训练结束后固定第一层, 训练双隐藏层, 然后固定前两层, 训练三隐藏层'
    
+ Avoid trival identity: more hidden than inputs
    + 学得太细了会过拟合 --> regularization(下一部分)
    + 所以我们之前看他的网络结构是两边粗中间细
    + 为了防止overfitting --> 介绍下面四种方法

## 2. Regularized Autoencoders 
+ 四种办法: 'sparse' / 'dropout' / 'contractive' / 'denoising'
2.1 Sparse AE 'P10'
+ 类似weight decay
+ 日啊那个公式不久是L1-regularization么 --> 部分隐藏单元变为0, 得到稀疏网络
2.2 AE with dropout at hidden layer(s)
2.3 Contractive AE
+ 这个是L2, 注意模里面取的是hi的梯度, 可以理解为隐藏层的变化幅度
+ 目标: 输入轻微变化时, 输出变化不要太大
2.4 Denoising AE
+ 给输入增加噪音, 但试图重现原输出
+ 使用编码器和解码器处理的是噪音x~, 然后和原数据xi做对比
+ 看下'P12'的伪代码
   + sample xi
   + generate noise x~
   + E = L(xi, g(f(x~))

2.5 Cost function: 将前向传播的cost function看作关于输出的概率分布 --> 最大化target values 的log概率
+ MSE: 高斯分布, 均值为网络输出
+ 交叉熵: 伯努利分布, 概率等于输出
+ Softmax: 玻尔兹曼分布

## 3. Stocastic encoder and decoders:
+ encoder: 给定输入x, 得到隐变量z的条件概率分布 'q_phi(z|x)'
+ decoder: 给定隐藏单元z, 得到输出x的条件概率分布 'p_theta(x|z)'
+ 对于RBM, 编码器和解码器都是伯努利分布
    
## 4. Generative Models
+ 从标准正太分布中采样获得隐变量z, 将这些z喂给decoder, 令生成的输出x与输入层的训练数据尽可能相似
+ 使用解码器生成和训练集相似的数据
    + 显式explicit生成模型: Variational AE
    + 隐式implicit生成模型: GAN, 和VAE的区别在于不需要population / 反向传播更新判别器然后再更新生成器 / 生成的图片更牛逼

## 5. Variational AE
+ 并非对每个xi生成单个的z, 而是通过encoder生成均值及标准差 --> 获取z关于xi的正态分布'q_phi(z|x^(i))'
+ 可以看下'P16'公式的两部分: 第一部分令从隐藏单元z解码得到的结果尽可能类似输入层结果xi, 第二部分encourges q(z|xi) to approximate p(z)
+ VAE和GAN的区别: VAE需要知道密度分布函数(population)
+ VAE的不足
    + blurry images --> GAN更牛逼
    + end up using a small number of dimensions available to z
    
