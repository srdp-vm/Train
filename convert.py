import os


if __name__ == '__main__':
    images = "images"
    annotation = "annotation"
    cwd = os.getcwd()
    images = os.path.normpath(os.path.join(cwd, images))
    annotation = os.path.normpath(os.path.join(cwd, annotation))
    print(images)
    print(annotation)
    shape = (416, 416)
    annotation_file = open("annotation.txt", "w")
    for filename in os.listdir(images):
        name, ext = os.path.splitext(filename)
        img_path = os.path.join(images, filename)
        anno_path = os.path.join(annotation, name + ".txt")
        print("JPG: {}, Annotation: {}".format(img_path, anno_path))
        try:
            with open(anno_path) as file:
                result = img_path
                for line in file:
                    cid, center_x, center_y, w, h = list(map(float, line.strip().split(" ")))
                    cid = int(cid)
                    center_x, center_y = center_x * shape[1], center_y * shape[0]
                    w, h = w * shape[1], h * shape[0]
                    x_min = round(center_x - w / 2)
                    x_max = round(center_x + w / 2)
                    y_min = round(center_y - h / 2)
                    y_max = round(center_y + h / 2)
                    result += " " + ",".join(str(i) for i in [x_min, y_min, x_max, y_max, cid])
                print(result)
            annotation_file.write(result + "\n")
        except IOError:
            print(anno_path + "文件不存在")
    annotation_file.close()

