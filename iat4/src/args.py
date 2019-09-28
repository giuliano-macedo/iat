import argparse
from ia.utils import parse_interval
from utils import FeatureExtractor
import os
def get_args():
	parser=argparse.ArgumentParser()
	parser.add_argument("method",
		type=FeatureExtractor,
		help="image extraction methods, it can be a combination of '%s'"%(
			'/'.join(list(FeatureExtractor.methods.keys()))
		)
	)
	parser.add_argument("-a","--alpha",
		type=float,
		help="alpha to use",
		required=True
	)
	parser.add_argument("-n","--no-it",
		type=int,
		help="max no of iterations on logistic regression",
		required=True
	)
	parser.add_argument("-d","--dataset",
		type=lambda s:s if os.path.isdir(s) else parser.error("path does not exist"),
		nargs="?",
		default=os.path.join("..","dataset"),
		help="path to dataset, defalt '../dataset/'"
	)
	parser.add_argument("-s","--sigma",
		type=int,
		nargs="?",
		default=1,
		help="standard deviation for gaussian blur"
	)
	parser.add_argument("-k","--kernel_size",
		type=int,
		nargs="?",
		default=3,
		help="kernel_size for gaussian blur"
	)
	parser.add_argument("-l","--threshold",
		type=int,
		nargs="?",
		default=80,
		help="threshold after sobel"
	)
	return parser.parse_args()