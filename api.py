# File chua code xu ly
# 
import http.client
import json


class ContestResult:
    def __init__(self, contestID, userHandle):
        self.contestID = contestID
        self.userHandle = userHandle
        submissions = API.getContestSubmissions(contestID, userHandle)
        results = dict()
        if submissions != None:
            for submission in submissions:
                probID = submission['problem']['index']
                if submission['verdict'] == 'OK':
                    submission['point'] = 1
                else:
                    submission['point'] = 0
                if results.get(probID) == None:
                    results[probID] = [submission]
                else:
                    results[probID].append(submission)
        self.results = results


class API:
    def crawl(request):
        conn = http.client.HTTPConnection('codeforces.com')
        conn.request('GET', request)
        resp = conn.getresponse()
        raw_data = resp.read()
        data = json.loads(raw_data.decode('utf-8'))
        return data.get('result')

    def getContestInfo(contestID):
        request = '/api/contest.standings?contestId=' + str(contestID) + '&from=1&count=1'
        raw = API.crawl(request)
        contest = raw['contest']
        contest['problems'] = raw['problems']
        return contest

    def getContestSubmissions(contestID, userHandle):
        request = '/api/contest.status?contestId=' + str(contestID) + '&handle=' + str(userHandle)
        submissions = API.crawl(request)
        return submissions

    def getContestResult(contestID, userHandle):
        submission = API.getContestSubmissions(contestID, userHandle)
        cr = ContestResult(contestID, userHandle)
        return cr
