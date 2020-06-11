'''
    @ Date: 2020-06-11 19:27:59
    @ LastEditors: Qing Shuai
    @ LastEditTime: 2020-06-11 19:51:31
    @ Author: Qing Shuai
    @ Mail: s_q@zju.edu.cn
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--inp', type=str, default='expert/record.json')
parser.add_argument('--out', type=str, default='expert/data.js')
parser.add_argument('--debug', action='store_true')
args = parser.parse_args()  

import json
def readJson(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data

import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
from matplotlib import cm
import numpy as np
import random

cmap = 'gist_rainbow'

# max support 100 human
N = 100
cmaps = cm.get_cmap(cmap, N)
x = np.linspace(0.0, 1.0, N)
index = [i for i in range(N)]
random.seed(666)
random.shuffle(index)
rgb = cm.get_cmap(cmap)(x)[index, :]

if __name__ == "__main__":
    data = readJson(args.inp)
    humans = list(data.keys())
    width = 1
    # write colors:
    with open(args.out, 'w') as f:
        f.writelines('var color = {\n')
        for i, human in enumerate(humans):
            f.writelines("    '{}': \"{}\",\n".format(human, to_hex(rgb[i])))
        f.writelines("};\n")
        # write edges:
        f.writelines('var data = [\n')
        for i, human in enumerate(humans):
            for val in data[human]:
                f.writelines("    ['{}', \"{}\", {}],\n".format(human, val, width))
        f.writelines("];\n")
        