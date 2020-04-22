import os


if __name__ == '__main__':
    origin = "annotation"
    plus = "annotation_plus"
    for filename in os.listdir(plus):
        origin_path = os.path.join(origin, filename)
        plus_path = os.path.join(plus, filename)
        with open(origin_path, "a") as originfile:
            with open(plus_path, "r") as plusfile:
                for line in plusfile:
                    originfile.write(line)
    print("Merge complete!")