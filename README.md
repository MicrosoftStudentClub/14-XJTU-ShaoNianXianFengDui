# 14-XJTU-ShaoNianXianFengDui
## MSRA学生项目作品--西安交通大学
![Image text](https://github.com/WALKMAN2000/14-XJTU-ShaoNianXianFengDui/blob/master/demo_img/demo_img1.JPG)
上图是我们的最终效果

## 说明
0.运行根目录下gui.py文件
1.从摄像头检测行人：可以从摄像头检测行人，退出键盘键入
2.从图像文件检测行人：可以从图像文件检测行人，文件放入test目录下，命名为test.jpg
3.从视频文件检测行人：可以从视频文件检测行人，文件放入test目录下，命名为test.mp4

## 识别效果展示
![Image text](https://github.com/WALKMAN2000/14-XJTU-ShaoNianXianFengDui/blob/master/demo_img/demo_img2.JPG)
![Image text](https://github.com/WALKMAN2000/14-XJTU-ShaoNianXianFengDui/blob/master/demo_img/predictions.jpg)

## 介绍
行人识别作为一种物体检测任务，是任何智能视频监控系统中的一项重要任务。最早的物体识别神经网络是通过一个滑窗在整幅输入图片上移动以确保扫描到所有位置，每一次扫描都计算一次卷积并且对该区域进行分类，这样计算过于缓慢，例如在一张500*500大小的图片上用一个40*40的滑窗进行扫描，步长为2的话，需要移动53361次并完成53361此前向传播的过程，这种方法不仅计算缓慢并且对于过大和过小的物体几乎无法检测。后来的Faster RCNN等网络使用Region Proposal方案生成若干个可能包含物体的框，使用分类器去对这些框打分，并且对框的位置进行微调，然而这种方式仍然检测很慢，并且由于这些环节并不是同时训练，优化较为困难。
然而，几年前提出了一种更简单，更有效的物体检测方法YOLO。由于其在效率，准确性和便利性方面极大领先于先前的网络模型，选择YOLO来完成此次项目。

## YOLO
YOLO is an approach of objection, in which the detection is treated as a regression problem. A single neural network predicts the bounding boxes and calss possibilities directly from the images in a single evaluation. Due to the simplicity of the detection process, YOLO runs at a surprisingly fast speed, 45 frames per second.</br>
The network structure of the YOLO network is shown in the figure below (Source: J. Redmon, S. Divvala, R. Girshick, A. Farhadi. You Only Look Once: Unified, Real-Time Object Detection [*arXiv:1506.02640v5*](https://arxiv.org/abs/1506.02640v5)).
![Image text](https://github.com/WALKMAN2000/14-XJTU-ShaoNianXianFengDui/blob/master/demo_img/YOLO_architecture.jpg)

## 项目依赖
Python：3.5
Tensorflow：1.4 with gpu
OS：Windows 10 or Ubuntu 16.04

