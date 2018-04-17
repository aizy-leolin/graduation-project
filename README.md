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

### CRC32

* CRC32参数有五部分：
    - 第一个是生成多项式，用它去除以原式，注意用异或代替减法即可
    - 第二个是初值，即初始的商
    - 第三个是最终异或值，即在输出前再和这个值异或
    - 第四个是输出是否反向，如果是则八位八位地反过来
    - 第五个是输出是否反向，如果是则输出的三十二位一起反过来
* 在实际实现中，为了高效，会八位八位的处理，八位的余数通过查表实现。再具体的原理不想管了
* 在PACK的时候用LSB来PACK

### Preamble

(0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0)

# 各种坑

* 如果流程图有sink、source确定了采样率，就不要再用其他会影响采样率的模块
* usrp sink的采样过低，会产生不够平滑的插值
* USRP Source的采样率要大于80k（不然会强行倍增到80k+）
* 当打开各种模块的property时，滑动鼠标滚轮时，如果鼠标正好指放在某一项可下拉的属性里并且你还没发现，那你就完了
* 如果没有符号同步，那么就等价于减少了信号能量，直接降低了信噪比，记得同步……
* tagged_stream的work最后面要return真实output长度，不是noutput_item

# Block tutorial

## USRP

* USRP sink/source会直接完成调制解调

## Packet

### Header/Payload Demux

* 输入：信息流、Trigger、Head message。输出：Header、Payload
* 当Trigger出现1时，开始截取header并输出。注意Trigger中的第一位1，对应着Header的第一位
* Trigger触发后，输出Header，然后根据header信息输出payload。有意思的是，输出完payload后，输入指针会指向payload的最后一位，而不是指向payload后的第一位，不知道为什么要这样设计。
* 没什么事就把Guard interval设成0就好了
