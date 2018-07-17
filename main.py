# Main.py
# 
__description__ = """\tChuong trinh thong ke ket qua thi Codeforces\n
		Cau lac bo ACM truong Dai hoc Bach Khoa TPHCM"""

import argparse

from api import API


def printResult(contest, user):
	ct = API.getContestInfo(contest)
	print("\tResult of contest", ct['name'],":")
	cr = API.getContestResult(contest, user)
	for r in cr.results:
		res = cr.results[r]
		for s in res:
			print(str(s['id'])+'\t'
				+r+'\t'
				+str(s['verdict'])+'\t'
				+str(s['passedTestCount'])+'\t'
				+str(s['timeConsumedMillis'])+'\t'
				+str(s['memoryConsumedBytes'])+'\t')


def main(args):
	if args.contests!=None and args.users!=None:
		for u in args.users:
			print('\t\t*** User:', u,'***')
			for c in args.contests:
				printResult(c,u)
			print()

parser = argparse.ArgumentParser(description=__description__)
parser.add_argument('-contests', metavar='contest_id', type=int, nargs='+', help='contest ID')
parser.add_argument('-users', metavar='user_handle', type=str, nargs='+', help='username')
args = parser.parse_args()
main(args)