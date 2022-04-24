# OCR-AnKang_Code-XingCheng_Code-HeSuan
# 通过OCR解析安康码、行程码、核酸截图中的姓名、时间、关键信息，并自动重命名
## 功能
##### 1、读取和代码同级'./截图'目录的图片
##### 2、解析文件名中的姓名，自动OCR并判断是行程卡或者安康码或者核酸，判断图中的名字，判断图中的核酸时间、安康码时间、行程码省市。 
##### 3、将文件拷贝重命名为'./重命名/姓名-啥码.jpeg'
##### 4、打印所有检测到的信息到'./结果.txt'
## 食用姿势
##### 1、在腾讯文档（https://docs.qq.com/）创建收集表（姓名、健康码、行程码、核酸）并督促填写
##### 2、导出全部图片放到截图目录下
##### 3、安装环境
git clone https://github.com/fusang1337/OCR-AnKang_Code-XingCheng_Code-HeSuan.git

conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda activate paddle_env

pip install paddleocr

python main.py

### 本代码参考了 https://github.com/fuxuemingzhu/NucleicAcidCheck
