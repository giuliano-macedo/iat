import argparse
from .  import parse_interval
def common_argparse_alphas(need_normalize=True):
	parser=argparse.ArgumentParser()
	parser.add_argument("--no_it","-n",type=int,required=True)
	parser.add_argument("--interval","-i",type=parse_interval,required=True)
	if need_normalize:
		parser.add_argument("--normalize",action="store_true")
	args=parser.parse_args()

	GRAPH_TITLE=""
	if args.interval.type=="range":
		a,b,c=args.interval.ans;
		GRAPH_TITLE=rf'Gráfico de $J(\theta)$ para diferentes alphas que variam ${a:g}$ e ${b:g}$, passo {c:g}'
	elif args.interval.type=="list":
		GRAPH_TITLE=rf'Gráfico de $J(\theta)$ para os alphas {args.interval.ans}'
	return GRAPH_TITLE,args