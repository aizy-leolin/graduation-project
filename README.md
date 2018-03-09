I think you can read nothing here ^_^

# Create out-of-tree module

## Command

1. create module directory:`gr_modtool newmod test`
2. add files for block:`gr_modtool add -t xxx test`
    * you can choose from sink,source,sync,decimator,interpolator,general,tagged_stream,hier,noblock for option -t
3. choose language and argument list according to the instruction
4. finish your code and test（python code in ./python and C++ code in ./lib）
5. Edit xml in ./grc


# module

## PHY

### recv_bit

* 前X(X=1000)bits不判决，第一个比特作为高、低电平门限，之后每遇到更大或更小的作平滑更新，高电平权重为（0.2、0.8），低电平权重为（0.5，0.5）
* 确定初始门限后，每收一个比特，判决完毕后，根据这个比特所属的电平，更新高、低电平门限，权重为（0.9、0.1）

### Conv Code

* g0=0133（1011011),g1=0171（1111001）
* 标准的卷积码编码、译码模块，软判决，窗长可调

# Debug suggestion

* 如果流程图有sink、source确定了采样率，就不要再用其他会影响采样率的模块
* usrp sink的采样过低，会产生不够平滑的插值

# Block tutorial

## USRP
* USRP sink/source会直接完成调制解调

