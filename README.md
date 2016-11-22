# Cat_PiCam

这个程序的主要目的用于我们不在家的时候监视家里猫吃饭的状况。是一个运行在 Raspberry Pi 上的简易微信机器人。

## 硬件依赖

* Raspberry Pi： 任何能够支持相机模块的 Raspberry Pi 都可以。
* 相机模块： 理论上所有兼容的相机模块都可以使用。因为我希望能在晚上不开灯的情况下也能有好的图片效果，所以用了[类似这样的带光源的红外线相机模块](https://www.amazon.ca/Kuman-Raspberry-camera-Module-Supports/dp/B01ICKPGVW)。

## 软件依赖

* [ItChat](https://github.com/littlecodersh/ItChat)，一个功能强大的微信接口。可通过`pip install itchat` 安装。
* [MP4Box](https://gpac.wp.mines-telecom.fr/mp4box/)，用于将pycam拍摄的视频转换为mp4。可以通过`sudo apt install -y gpac` 安装。

## 使用
clone 代码至本地，在src目录下运行 `python main.py` 即可。 最好在一个 tmux/screen sessions 下或者后台运行。

目前支持的命令有四个。`Image`, `Video`, `ls`, `rm` 分别是用于拍摄图片，视频， 显示已拍摄的文件和删除所有已拍摄的文件。

