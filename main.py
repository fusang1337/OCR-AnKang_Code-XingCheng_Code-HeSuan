import os
from paddleocr import PaddleOCR
import re
import shutil

img_folder = r"C:\Users\THHICV\Downloads\附件下载_20220521三码收集（收集结果）\源文件"
save_path = r"C:\Users\THHICV\Downloads\附件下载_20220521三码收集（收集结果）\结果"
filename = r'C:\Users\THHICV\Downloads\附件下载_20220521三码收集（收集结果）\结果.txt'

print("要处理的目录为：",img_folder)
print("重命名的文件保存在：",save_path)
print("处理过程保存在：",filename)
if not os.path.exists(save_path):
    os.mkdir(save_path)
def match(reg, total):
    reg_re = re.search(reg, total, re.M | re.I)
    reg_ocr = ""
    if reg_re and len(reg_re.groups()) >= 1:
        reg_ocr = reg_re.group(1)
    return reg_ocr

ocr = PaddleOCR(lang='ch', det_db_box_thresh=0.5, use_gpu=False, det_model_dir=r'./model/det/ch/ch_PP-OCRv2_det_infer',
                rec_model_dir=r'./model/rec/ch/ch_PP-OCRv2_rec_infer',
                cls_model_dir=r'./model/cls/ch_ppocr_mobile_v2.0_cls_infer')
imgs = os.listdir(img_folder)
with open(filename,'w') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    pass

for img_path in imgs:
    # 遍历每一张图片
    # img = imgs[0]
    # paddleocr
    result_all = ocr.ocr(os.path.join(img_folder, img_path), cls=False)
    result_chin = [line[1][0] for line in result_all]
    result_str = str(result_chin)
    # print(result_str)
    print("--" * 88)
    name_file = match(r'(?<=收集结果-)(.+?)(?=-)', img_path)
    # print("文件名中的名字是：",name_file)
    # print(name_file)
    if '检测机构' in result_str:
        if '已过' in result_str:
            result_str = re.sub("'", "", result_str)
            result_str = re.sub(",", "", result_str)
            name_ocr = match(r'(?<=姓名 )(.+?)(?= 身份)', result_str)
            time_caiji = match(r'(?<=采集时间 )(.+?)(?= 检测)', result_str)
            nucleic_result_ocr = match(r'(\S性)', result_str)
            time_caiji = time_caiji[:10]
            print(name_file+"核酸检测报告"+"&"+img_path+"&"+name_ocr+"&"+time_caiji+"&"+nucleic_result_ocr)
            with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
                f.write(name_file+"&"+"核酸检测报告"+"&"+img_path+"&"+name_ocr+"&"+time_caiji+"&"+nucleic_result_ocr+"\n")
            shutil.copy(os.path.join(img_folder, img_path),os.path.join(save_path,name_file+"-"+"核酸检测报告"+".jpeg"))


        else:
            name_ocr = match(r'姓\s*名：\s*(\S*)', result_str)
            time_caiji = match(r'采集时间\s*(\S*)', result_str)
            nucleic_result_ocr = match(r'(\S性)', result_str)
            time_caiji = time_caiji[:11]
            print(name_file+"核酸检测报告"+"&"+img_path+"&"+name_ocr+"&"+time_caiji+"&"+nucleic_result_ocr)
            with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
                f.write(name_file+"&"+"核酸检测报告"+"&"+img_path+"&"+name_ocr+"&"+time_caiji+"&"+nucleic_result_ocr+"\n")
            shutil.copy(os.path.join(img_folder, img_path),
                        os.path.join(save_path, name_file + "-" + "核酸检测报告" + ".jpeg"))

    elif '康码' in result_str:
        result_str = re.sub("'", "", result_str)
        result_str = re.sub(",", "", result_str)
        name_ocr = match(r'(?<=办事 )(.+?)(?= 点)', result_str)
        time_jietu = match(r'(?<=天 )(.+?)(?=请点)', result_str)
        ma_result_ocr = match(r'(?<=二维码 )(.+?)(?= 核酸)', result_str)
        time_jietu = time_jietu[:10]
        print(name_file+"安康码"+"&"+img_path+"&"+name_ocr+"&"+time_jietu+"&"+ma_result_ocr)
        with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(name_file+"&"+"安康码"+"&"+img_path+"&"+name_ocr+"&"+time_jietu+"&"+ma_result_ocr+"\n")
        shutil.copy(os.path.join(img_folder, img_path), os.path.join(save_path, name_file + "-" + "安康码" + ".jpeg"))
    elif '区域核酸' in result_str:
        result_str = re.sub("'", "", result_str)
        result_str = re.sub(",", "", result_str)
        name_ocr = match(r'(?<=姓名 )(.+?)(?= 身份)', result_str)
        time_caiji = match(r'(?<=采集时间 )(.+?)(?= 检测)', result_str)
        nucleic_result_ocr = match(r'(\S性)', result_str)
        time_caiji = time_caiji[:10]
        print(name_file + "核酸检测报告" + "&" + img_path + "&" + name_ocr + "&" + time_caiji + "&" + nucleic_result_ocr)
        with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(
                name_file + "&" + "核酸检测报告" + "&" + img_path + "&" + name_ocr + "&" + time_caiji + "&" + nucleic_result_ocr + "\n")
        shutil.copy(os.path.join(img_folder, img_path), os.path.join(save_path, name_file + "-" + "核酸检测报告" + ".jpeg"))

    elif '行程卡' in result_str:
        result_str = re.sub("'", "", result_str)
        result_str = re.sub(",", "", result_str)
        name_ocr = match(r'(?<=绿色行程卡 )(.+?)(?=的动态行)', result_str)
        time_jietu = match(r'(?<=更新于：)(.+?)(?=您于前)', result_str)
        ma_result_ocr = match(r'(?<=或途经：)(.+?)(?=结果包)', result_str)
        time_jietu = time_jietu[:10]
        print(name_file+"行程卡"+"&"+img_path+"&"+name_ocr+"&"+time_jietu+"&"+ma_result_ocr)
        with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(name_file+"&"+"行程卡"+"&"+img_path+"&"+name_ocr+"&"+time_jietu+"&"+ma_result_ocr+"\n")
        shutil.copy(os.path.join(img_folder, img_path), os.path.join(save_path, name_file + "-" + "行程卡" + ".jpeg"))

    else:
        print(name_file+"判断出现错误"+"&"+img_path+"\n")
        with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(name_file+"&"+"异常"+"&"+img_path+"&"+name_ocr+"&"+time_jietu+"&"+ma_result_ocr+"\n")
        if not os.path.exists(os.path.join(save_path, "异常")):
            os.mkdir(os.path.join(save_path, "异常"))
        shutil.copy(os.path.join(img_folder, img_path), os.path.join(save_path, "异常",name_file + "-" + "行程卡" + ".jpeg"))
