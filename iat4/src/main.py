import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__,*[".."]*3)))
from ia import LogisticRegression
from ia.utils import download_and_extract_zip,parse_interval
from ia.tpi import humoments,fract_dim
import argparse
import matplotlib.pyplot as plt
import numpy as np
from utils import open_img_grey,sobel_l
from sys import argv

sigma=1
k=3
l=80

pic=open_img_grey(f"../dataset/train/cat/cat_{argv[1]}.png")
pic_l=sobel_l(pic,sigma,k,l)
# print(humoments(pic_l))
print(fract_dim(pic_l))
exit()
exit()

METHODS={
	"humoments",
	"fract_dim",
	"histogram",
	"pixels"
}
parser=argparse.ArgumentParser()
parser.add_argument("method",
	type=lambda s:s if all(m in METHODS for m in s.split(",")) else parser.error("invalid method"),
	help="/".join(METHODS)
)
parser.add_argument("-i","--interval",type=parse_interval)
parser.add_argument("-n","--no-it",type=int)
parser.add_argument("-d","--dataset",
	type=lambda s:s if os.path.isdir(s) else parser.error("path does not exist"),
	nargs="?",
	default=os.path.join("..","dataset"),
	help="path to dataset, defalt '../dataset/'"
)
args=parser.parse_args()

if (args.dataset==os.path.join("..","dataset")) and( not os.path.isdir(args.dataset)):
	url="https://llpinokio-ia.herokuapp.com/cats.zip"
	print("downloading dataset...")
	download_and_extract_zip(url,args.dataset)

