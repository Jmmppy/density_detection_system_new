# 运行系统说明
#一、环境配置（终端进入环境后）
pip install -i https://pypi.douban.com/simple -r requirements.txt

如果使用工业相机则需要安装SDK，直接使用笔记本电脑的摄像头就不需要
下载链接：www.mindvision.com.cn/rjxz/list_12.aspx
软件为：迈德威视工业相机Windows系统SDK安装包V2.1.10.157(For Windows 10/7/8/8.1/Vista/XP)

1、开始需将Grad_design/yolodeepsort/deep_sort中的deep_sort.yaml文件中第二行的以下网络模型
ckpt.t7的路径改为相对路径

REID_CKPT: "C:\\Users\\hp\\Desktop\\s_dd\\detect_01\\Grad _design\\
yolodeepsort\\deep_sort\\deep_sort\\deep\\checkpoint\\ckpt.t7"

2、再将yolodeepsort/objtracker.py文件中的第八行改为deep_sort.yaml文件的相对路径
cfg.merge_from_file(r"C:\Users\hp\Desktop\s_dd\detect_01\Grad _design\yolodeepsort\deep_sort\deep_sort.yaml")

3、右键设置s_dd、Grad _design以及yolodeepsort文件，将目录标记为源根root

运行主程序为Grad _design中的main_Interface.py
由于时间有限，目前存在直接运行有问题，但选择调试则可以运行
所以通过点击调试可以查看系统运行效果

#二、报错解决方法：
1、若在终端无法进入环境的话，设置终端为相应的cmd.exe路径
C:\Windows\System32\cmd.exe
我们自己是使用的anaconda创建的虚拟环境

2、初次使用环境若报错...5md.dll文件（不记得具体叫什么了，但报错的话会弹出名称）
需要初始化一下：
就是在环境目录下搜索该名称的dll文件，删除这些文件即可

3、安装torch后，大概可能出现upsample的错误
可以直接百度搜索该错误，具体是只要删除一个参数即可
