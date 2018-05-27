import os
import cv2
import argparse
import numpy as np
import tensorflow as tf
import yolo.config as cfg
from yolo.yolo_net import YOLONet
from utils.timer import Timer
import tkinter as tk
import test
from tkinter import messagebox  # import this to fix messagebox error
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('--weights', default="YOLO_small.ckpt", type=str)
parser.add_argument('--weight_dir', default='weights', type=str)
parser.add_argument('--data_dir', default="data", type=str)
parser.add_argument('--gpu', default='', type=str)
args = parser.parse_args()

os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu

yolo = YOLONet(False)
weight_file = os.path.join(args.data_dir, args.weight_dir, args.weights)
detector = test.Detector(yolo, weight_file)

def detect_from_the_camera():
    # 从摄像头检测
    cap = cv2.VideoCapture(0)
    detector.camera_detector(cap)

def detect_from_the_picture():
    # 从图片检测
    imname = 'test/test.jpg'
    detector.image_detector(imname)

def detect_from_the_video():
    videoname = 'test/test.mp4'
    video = cv2.VideoCapture(videoname)
    detector.video_detector(video)

def read_me():
    r = messagebox.askokcancel('README', '1.从摄像头检测行人：可以从摄像头检测行人，退出键盘键入q\n'
                                         '2.从图像文件检测行人：可以从图像文件检测行人，文件放入test目录下，命名为test.jpg\n'
                                         '3.从视频文件检测行人：可以从视频文件检测行人，文件放入test目录下，命名为test.mp4\n\n'
                                         '**版权所有：西安交通大学--XWL**\n')

def exit_system():
    window.destroy()

window = tk.Tk()
window.title('行人检测系统--XWL')
window.geometry('300x420')

# welcome images
canvas = tk.Canvas(window, height=100, width=300)
image_file = tk.PhotoImage(file='data/sources/xjtu_show.png')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.place(x=10, y=20)

b1 = tk.Button(window,
    text='从摄像头检测行人',
    width=25, height=2,
    font=("黑体", 12),
    command=detect_from_the_camera)
b1.place(x=50,y=120)


b2 = tk.Button(window,
    text='从图像文件检测行人',
    width=25, height=2,
    font=("黑体", 12),
    command=detect_from_the_picture)
b2.place(x=50, y=175)

b3 = tk.Button(window,
    text='从视频文件检测行人',
    width=25, height=2,
    font=("黑体", 12),
    command=detect_from_the_video)
b3.place(x=50, y=230)

b4 = tk.Button(window,
    text='【  R E A D M E  】',
    width=25, height=2,
    font=("黑体", 12),
    command=read_me)
b4.place(x=50, y=285)

b4 = tk.Button(window,
    text='退出行人检测系统',
    width=25, height=2,
    font=("黑体", 12),
    command=exit_system)
b4.place(x=50, y=340)


def main():
    window.mainloop()


if __name__ == '__main__':
    main()