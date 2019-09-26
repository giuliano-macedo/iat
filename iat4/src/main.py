import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__,*[".."]*3)))
from ia import download_and_extract_zip,LogisticRegression,parse_interval
import argparse
METHODS={
	"fft",
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

