## 基因片段功能检测
 - 给出一段未知功能的基因片段，获得该基因片段的功能，主要是通过计算机模拟的方法。

---
1. 流程
 - 获取基因序列
 - 获取待检测基因片段
 - DNA -> RNA -> 蛋白质
	- DNA -> RNA -> 氨基酸序列：这个过程已经实现 Expasy
	- 氨基酸序列 -> 蛋白质结构：[SWISS-MODEL](https://blog.csdn.net/qq_29300341/article/details/69651060) + VMD(可视化)
	- 氨基酸层次：DeepView
 - 分析蛋白质结构及功能
	- chemdraw 蛋白质结构转 pdb
	- gaussview 画分子
 - 推断基因片段功能
2. 实现方式
 - 计算模拟
 - Python C C++
 - 可视化
3. 实验
 - 找一个已经确定功能的基因片段进行转录
4. 基因数据
 - [NCBI](https://www.ncbi.nlm.nih.gov/)
 
## 配置
 - config/config.txt 配置文件
 - pyfunc Python函数
 - kownledge 知识数据
 - python3.5(pandas, numpy, matplotlib)
 - gromacs(模拟)
 
---
### 进度
 - 20180627	DNA 到氨基酸序列的实现，并验证结果
 - 20180629 氨基酸序列到蛋白质结构的实现方法
 - 20180701 CesA protein CesA 基因族控制纤维素合成酶的合成
	- [拟南芥数据库TAIR](http://www.arabidopsis.org/)
	- [水稻数据库Rice Genome](http://rice.plantbiology.msu.edu/index.shtml)
	- [在线基因结构显示系统GSDS](http://gsds.cbi.pku.edu.cn)
	- [蛋白质结构分析SMART](http://smart.emblheidelberg.de/)
 - 20180706 纤维素合成酶的gromacs 计算模拟结束，用时3天
	- [gromacs 可以做的分析](http://blog.sciencenet.cn/blog-504446-746761.html)
 - 20180707（勿忘国耻） 生成回旋半径随时间变化图
	- ![回旋半径](https://github.com/xuleichao/GeneFuncDetect/blob/master/datasets/images/%E7%BA%A4%E7%BB%B4%E7%B4%A0%E5%90%88%E6%88%90%E9%85%B6Rg.png)