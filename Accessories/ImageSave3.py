# 方法一：图片存储——根据OK或ng存到OK文件夹和ng文件夹。
# 输入参数（图片地址，字符串‘OK’ or ‘ng’）。黄璐那里每识别判断一个，直接调用我的函数进行存储。
# 拍下的图片都全放在同一个文件夹datafile文件夹里面。
# 问题：还需要改进，把类中的方法函数分细一些，不要每次都要经历创建文件夹

import os
import shutil
# 输入参数（图片地址，字符串‘OK’ or ‘ng’）
class ImageSave33:
    def __init__(self, src):
        self.src = src
    def deal_file(self, check_string):
        # 再存储全部图片的上一层创建文件夹
        # ok文件存储位置
        dst1_ok = os.path.join(self.src, '..', 'ok_file')
        if not os.path.exists(dst1_ok):
            os.makedirs(dst1_ok)
        # ng文件存储位置
        dst2_ng = os.path.join(self.src, '..', 'ng_file')
        if not os.path.exists(dst2_ng):
            os.makedirs(dst2_ng)

        # 创建目标文件夹
        if not os.path.isdir(dst1_ok):
            os.mkdir(dst1_ok)
        if not os.path.isdir(dst2_ng):
            os.mkdir(dst2_ng)

        # 拷贝该图片到目标文件夹
        if check_string == 'ok':
            shutil.copy(self.src, dst1_ok)
        if check_string == 'ng':
            shutil.copy(self.src, dst2_ng)

if __name__ == "__main__":

    # 类测试
    img1 = ImageSave33("F:/app/data/图片2.png")
    img1.deal_file('ng')

    img2 = ImageSave33("F:/app/data/图片5.png")
    img2.deal_file('ng')

    img3 = ImageSave33("F:/app/data/图片6.png")
    img3.deal_file('ok')