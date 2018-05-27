# 14-XJTU-ShaoNianXianFengDui
## MSRA学生项目作品--西安交通大学
![Image text](https://github.com/WALKMAN2000/14-XJTU-ShaoNianXianFengDui/blob/master/demo_img/demo_img1.JPG)
上图是我们的最终效果

## 说明
0.运行根目录下gui.py文件</br>
1.从摄像头检测行人：可以从摄像头检测行人，退出键盘键入q</br> 
2.从图像文件检测行人：可以从图像文件检测行人，文件放入test目录下，命名为test.jpg</br>
3.从视频文件检测行人：可以从视频文件检测行人，文件放入test目录下，命名为test.mp4</br>

## 识别效果展示
![Image text](https://github.com/WALKMAN2000/14-XJTU-ShaoNianXianFengDui/blob/master/demo_img/demo_img2.JPG)</br>
![Image text](https://github.com/WALKMAN2000/14-XJTU-ShaoNianXianFengDui/blob/master/demo_img/predictions.jpg)</br>

## 介绍
行人识别作为一种物体检测任务，是任何智能视频监控系统中的一项重要任务。最早的物体识别神经网络是通过一个 Sliding Window 在整幅输入图片上移动以确保扫描到所有位置，每一次扫描都计算一次卷积并且对该区域进行分类，这样计算过于缓慢。在深度神经网络之前，早期的 Object detection 方法是通过提取图像的一些 robust 的特征如（ Haar，SIFT，HOG ）等特征，使用 DPM 模型，用 Silding Window 的方式来预测具有较高 score 的 bounding box。这种方式非常耗时，而且精度又不怎么高。Selective Search的方法，相比于 Sliding window 这种穷举的方式，减少了大量的计算，同时在性能上也有很大的提高。</br>
利用 Selective Search 提出的 Region Proposals 结合卷积神经网络的R-CNN的方法提出后，Object detection 的性能有了一个质的飞越。基于 R-CNN 发展出来的 SPPnet、Fast R-CNN、Faster R-CNN 等方法，证明了 “Proposal + Classification” 的方法 在 Objection Detection 上的有效性。</br>
然而，使用Region Proposal的方法速度依然较慢，无法达到实时检测，几年前提出了一种更简单，更有效的物体检测方法YOLO。由于其在效率，准确性和便利性方面极大领先于先前的网络模型，我们选择YOLO来完成此次项目。</br>
## YOLO
YOLO is an approach of objection, in which the detection is treated as a regression problem. A single neural network predicts the bounding boxes and calss possibilities directly from the images in a single evaluation. Due to the simplicity of the detection process, YOLO runs at a surprisingly fast speed, 45 frames per second.</br>
The network structure of the YOLO network is shown in the figure below (Source: J. Redmon, S. Divvala, R. Girshick, A. Farhadi. You Only Look Once: Unified, Real-Time Object Detection [*arXiv:1506.02640v5*](https://arxiv.org/abs/1506.02640v5)).
![Image text](https://github.com/WALKMAN2000/14-XJTU-ShaoNianXianFengDui/blob/master/demo_img/YOLO_architecture.jpg)

## 项目依赖
Python：3.5</br>
Tensorflow：1.4 with gpu</br>
OS：Windows 10 or Ubuntu 16.04</br>

