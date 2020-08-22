import os, shutil
import random

def get_random_files(path, type, count):
    all_f = os.listdir(path)
    all_f = list(filter(lambda x: x.endswith(str(type)), all_f))
    if all_f:
        rand_f = random.sample(all_f, count)
        return rand_f
    if not all_f:
        return []

def copy_and_paste(father_path, son_path, what):
    if not os.access(son_path, os.X_OK):
        os.mkdir(son_path)
    for i in what:
        shutil.copy(father_path + str(i), son_path + str(i))


