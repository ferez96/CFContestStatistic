import main
from argparse import Namespace

# for submission in api.getContestSubmissions(1003,'minhphuoc1998'):
	# print(submission['id'])
# api.API.getContestResult(1003,'minhphuoc1998')
# print(api.API.getContestInfo(1003))

# This equal to :
# python main.py -contests 1003 1004 1005 -users ferez.96 minhphuoc1998
args = Namespace(contests=[1003,1004,1005],users=['ferez.96','minhphuoc1998'])
main.main(args)