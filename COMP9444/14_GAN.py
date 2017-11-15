# GAN
1. Generator(Artist) + Discriminator(Critic)
+ 基本原理可以看下我的git: https://github.com/YunqiuXu/Readings/blob/master/GAN_series.md
+ 生成器G: 
    + z: 用于生成数据的"噪音", 正太分布采样
    + 最小化log(1-D(G(z))
    + 即最大化D(G(z)) --> 生成接近真实的数据, 这样D的判别结果会接近1
    # 其实这里和denoising AE也有共通之处: 都是根据样本生成噪音
+ 判别器D:
    + 判断输入样本x是否为真实数据, 是1否0
+ 总体loss function: 'p26'
    + 这两个B玩零和游戏
    + 最小化D loss和G loss的加和
    + min_theta max_psi --> theta是G的参数, psi是D的参数

2. GAN优化方式
+ D: 梯度上升 --> max psi
+ G: 梯度下降 --> min theta
+ P28讲了一种优化: D不变依然使用梯度上升, G也使用梯度上升:
    + max_theta E_z( log( D_psi( G_theta(z) ) ) ) --> 最大化theta
    + 可以更专注于被错误分类的图片 # 原来用梯度下降的时候过度专注被正确分类的了
    
3. GAN与其他学习(e.g. VAE)的不同
+ 不需要population: one network produces a range of all images x, with different values for the latent z # 这句话还不大理解
+ differentials使用反向传播通过D然后进入G: 先经过D然后进入D中的G
+ 生成以假乱真的图片
4. 训练过程
+ 看下'P30'的伪代码(其实就是在那两个部分的优化加上了minibatch)

5. 构架细节 # 这个其实是DCGAN
+ 图片被正则化到[-1, 1]
+ pooling layer变为
    + 正卷积判别, 反卷积生成
    + D: strided convolutions
    + G: ractional-strided convolutions
+ DG都用了BN
+ activate function
    + G: output layer tanh, all others ReLU
    + D: LeakyReLU
        
4. GAN 可能出现的问题及解决措施
+ oscillation波动: 不稳定, 训练时间长, 且生成图片的质量难以提升
+ mode collapse: 生成样本多样性少, 只能收敛成为少数图片进行输出
    'poor diversity --> converge to a few(or only one) images'
    + Conditioning augmentation
    + Minibatch features: fitness sharing
    + unrolled GANs: 每一步并不把判别模型 D 这个学习的雪球给滚起来，而是把 K 次的 D 都存起来，然后根据损失（loss）来选择最好的那一个
    
