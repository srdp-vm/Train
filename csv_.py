import os
import csv
import random

if __name__ == '__main__':
    images_dir = "images"
    annotation_dir = "annotation"
    cwd = os.getcwd()
    images_dir = os.path.normpath(os.path.join(cwd, images_dir))
    annotation_dir = os.path.normpath(os.path.join(cwd, annotation_dir))
    
    total_xml = os.listdir(images_dir)   #返回指定路径下的文件和文件夹列表
    num = len(total_xml)
    list_ = range(num)
    
    train_percent = 0.85
    tr = int(num * train_percent)
    train = random.sample(list_, tr)

    class_dict = {0:"NF"}
    shape = (416, 416)

    #生成声明文件
    annotation_train_file = open("annotations_train.csv", "w", newline="")
    annotation_val_file = open("annotations_val.csv", "w", newline="")
    train_csv = csv.writer(annotation_train_file, delimiter=',')
    val_csv = csv.writer(annotation_val_file, delimiter=',')
    
    for i in list_:
        filename = total_xml[i]
        name, ext = os.path.splitext(filename)
        img_file = os.path.join(images_dir, filename)
        train_file = os.path.join(annotation_dir, name + ".txt")
        val_file = os.path.join(annotation_dir, name + ".txt")
        if i in train:
            try:
               with open(train_file) as file:
                    for line in file:
                       cid, center_x, center_y, w, h = list(map(float, line.strip().split(" ")))
                       cid = int(cid)
                       center_x, center_y = center_x * shape[1], center_y * shape[0]
                       w, h = w * shape[1], h * shape[0]
                       x_min = round(center_x - w / 2)
                       x_max = round(center_x + w / 2)
                       y_min = round(center_y - h / 2)
                       y_max = round(center_y + h / 2)
                       result = [img_file, x_min, y_min, x_max, y_max, class_dict[cid]]

                       train_csv.writerow(result)
            except IOError:
                print(train_file + "文件不存在")      
        else:
           try:
               with open(val_file) as file:
                    for line in file:
                       cid, center_x, center_y, w, h = list(map(float, line.strip().split(" ")))
                       cid = int(cid)
                       center_x, center_y = center_x * shape[1], center_y * shape[0]
                       w, h = w * shape[1], h * shape[0]
                       x_min = round(center_x - w / 2)
                       x_max = round(center_x + w / 2)
                       y_min = round(center_y - h / 2)
                       y_max = round(center_y + h / 2)
                       # result += " " + ",".join(str(i) for i in [x_min, y_min, x_max, y_max, cid])
                       result = [img_file, x_min, y_min, x_max, y_max, class_dict[cid]]
                       val_csv.writerow(result)
           except IOError:
                print(val_file + "文件不存在")    
                
    annotation_train_file.close()
    annotation_val_file.close()    
            
    #生成classes.csv映射文件
    with open("class_mappings.csv", "w", newline="") as cls:
        cls_csv = csv.writer(cls)
        for k, v in class_dict.items():
            cls_csv.writerow([v, k])