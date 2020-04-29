import os
import csv


if __name__ == '__main__':
    images_dir = "images"
    annotation_dir = "annotation"
    cwd = os.getcwd()
    images_dir = os.path.normpath(os.path.join(cwd, images_dir))
    annotation_dir = os.path.normpath(os.path.join(cwd, annotation_dir))
    print(images_dir)
    print(annotation_dir)

    class_dict = {0 : "NF"}
    shape = (416, 416)

    #生成声明文件
    annotation_file = open("annotation.csv", "w", newline="")
    anno_csv = csv.writer(annotation_file)
    for filename in os.listdir(images_dir):
        name, ext = os.path.splitext(filename)
        img_file = os.path.join(images_dir, filename)
        anno_file = os.path.join(annotation_dir, name + ".txt")
        print("JPG: {}, Annotation: {}".format(img_file, anno_file))
        try:
            with open(anno_file) as file:
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
                    anno_csv.writerow(result)
        except IOError:
            print(anno_file + "文件不存在")
    annotation_file.close()

    #生成classes.csv映射文件
    with open("classes.csv", "w", newline="") as cls:
        cls_csv = csv.writer(cls)
        for k, v in class_dict.items():
            cls_csv.writerow([v, k])