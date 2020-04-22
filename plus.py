import os
import shutil


if __name__ == '__main__':
    images = "images"
    annotation = "annotation"
    images_plus = "images_plus"
    annotation_plus = "annotation_plus"
    index = len(os.listdir(images))

    for filename in os.listdir(annotation_plus):
        if filename == "classes.txt":
            continue
        index += 1
        name, ext = os.path.splitext(filename)
        image_src = os.path.join(images_plus, name + ".jpg")
        label_src = os.path.join(annotation_plus, filename)
        image_dst = os.path.join(images, str(index) + ".jpg")
        label_dst = os.path.join(annotation, str(index) + ext)
        print("move \"{}\" to \"{}\"".format(image_src, image_dst))
        shutil.move(image_src, image_dst)
        print("move \"{}\" to \"{}\"".format(label_src, label_dst))
        shutil.move(label_src, label_dst)
    print("Plus complete!")

    # images = os.listdir(imagesPath)
    # for image in images:
    #     name, ext = os.path.splitext(image)
    #     imagePath = os.path.join(imagesPath, image)
    #     labelPath = os.path.join(labelsPath, name + ".txt")
    #     print(imagesPath, imagePath)
    #     if os.path.exists(labelPath):
    #         max += 1
    #         image_new = str(max) + ext
    #         label_new = str(max) + ".txt"
    #         print("rename:" + imagePath, image_new)
    #         print("rename:" + labelPath, label_new)
    #         os.rename(imagePath, os.path.join(imagesPath, image_new))
    #         os.rename(labelPath, os.path.join(labelsPath, label_new))