# 14-XJTU-ShaoNianXianFengDui
MSRA学生项目作品--西安交通大学
![](https://github.com/WALKMAN2000/14-XJTU-ShaoNianXianFengDui/demo_img1.JPG)
上图是我们的最终效果


## Introduction
Pedestrian recognition, as a kind of object detection task, is an essential and significant task in any intellegent video surveillance system. It provides a basic understanding of a frame from a video, which could be used for more complecated purposes, pose estimation for example.</br>
Many object detection systems alter classifiers for detection purposes. These kind of detectors ususlly consist evaluation of the classifier at various locations and scales in an image. Such detectors usually has terribly low efficiency due to enormous work amount. Approaches like R-CNN use region proposal methods which speeds up the process a little by generating potential bounding boxes in an image before running the classifier.</br>
However, a simpler and more efficient approach os object detection, YOLO, is proposed a couple years ago. It is selected in our group due to its supriority in efficiency, accuracy, and convinience.</br>

## YOLO
YOLO is an approach of objection, in which the detection is treated as a regression problem. A single neural network predicts the bounding boxes and calss possibilities directly from the images in a single evaluation. Due to the simplicity of the detection process, YOLO runs at a surprisingly fast speed, 45 frames per second.</br>
The network structure of the YOLO network is shown in the figure below (Source: J. Redmon, S. Divvala, R. Girshick, A. Farhadi. You Only Look Once: Unified, Real-Time Object Detection [*arXiv:1506.02640v5*](https://arxiv.org/abs/1506.02640v5)).
![](https://github.com/Anannf/14-XJTU-ShaoNianXianFengDui/blob/master/YOLO/YOLO_architecture.jpg)
We constructed the YOLO network using TensorFlow, an open source deep learning framework.</br>
## YOLOv3
YOLOv3 is a recently improved version of the YOLO approach which has demonstrated extraordinary performance in training and detection speed, as shown in the figure below (Source: J. Redmon, A. Farhadi. YOLOv3: An Incremental Improvement [*arXiv:1804.02767v1*](https://arxiv.org/abs/1804.02767v1)).
![](https://github.com/Anannf/14-XJTU-ShaoNianXianFengDui/blob/master/YOLOv3/resource/YOLOv3.jpeg)
YOLOv3 is released in March 2018. The new network for feature extraction has a 53 layer structure as the following figure shows (Source: J. Redmon, A. Farhadi. YOLOv3: An Incremental Improvement [*arXiv:1804.02767v1*](https://arxiv.org/abs/1804.02767v1)).
![](https://github.com/Anannf/14-XJTU-ShaoNianXianFengDui/blob/master/YOLOv3/resource/YOLOv3_architecture.jpg)
Comparing to the precious version YOLOv2, the accuracy of detection has significantly improved, while the speed has not changed a lot. It is approximatly 4 times faster than RetinaNet, but it provides similar accuracy.</br>
This model has satisfying performance on platforms with limited computational ability, thus it is perfect for industrial utilization, such as surveillance cameras, self-drived automobiles, or outdoor inspections.</br>
In our project, the YOLOv3 network is trained for pedestrain detection. A demo of the result is shown in the pictures below. The first picture is a photography of a few persons and the result of the detection is shown below it.
![](https://github.com/Anannf/14-XJTU-ShaoNianXianFengDui/blob/master/YOLOv3/resource/people.jpg)
![](https://github.com/Anannf/14-XJTU-ShaoNianXianFengDui/blob/master/YOLOv3/resource/predictions.jpg)
