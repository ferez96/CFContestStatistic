from main import getResult

# Educational Codeforces Round xx
CONTEST_0 = {'A': 2, 'B': 2, 'C': 2, 'D': 2, 'E': 4, 'F': 4, 'G': 8}
# Codeforces Round #xxx Div. 1
CONTEST_1 = {'A': 4, 'B': 4, 'C': 4, 'D': 16, 'E': 32}
# Codeforces Round #xxx Div. 2
CONTEST_2 = {'A': 2, 'B': 2, 'C': 2, 'D': 4, 'E': 8}
# Codeforces Round #xxx Div. 3
CONTEST_3 = {'A': 1, 'B': 1, 'C': 1, 'D': 2, 'E': 4}
# Contest
CONTEST = [CONTEST_0, CONTEST_1, CONTEST_2, CONTEST_3]


def ctype(contest_name):
    if contest_name.find("Educational") != -1:
        return 0
    if contest_name.find("Div. 1") != -1:
        return 1
    if contest_name.find("Div. 2") != -1:
        return 2
    if contest_name.find("Div. 3") != -1:
        return 3
    return 4


def score(contest_name, succ_problem):
    contestName = contest_name
    contestType = ctype(contestName)
    succProblem = succ_problem
    totalScore = 0

    for problem in succProblem:
        if problem in CONTEST[contestType].keys():
            totalScore += CONTEST[contestType][problem]

    return totalScore


f = open("data/z_ContestId.txt", 'r')
contestId = []
for contest_id in f:
    contestId.append(contest_id.strip())
f.close()

g = open("data/z_User.txt", 'r')
userName = []
for user_name in g:
    userName.append(user_name.strip())
g.close()

for user_name in userName:
    h = open("data/acc_" + user_name + ".txt", 'w')
    print("Doing on " + user_name)
    for contest_id in contestId:
        result = getResult(contest_id, user_name)
        contestName = result[0]
        succProblem = result[1:]
        totalScore = score(contestName, succProblem)

        h.write("\tResult of contest " + contestName + ":\n")
        h.write("Success Problem: " + ' '.join(succProblem) + "\n")
        h.write("Total score: " + str(totalScore) + "\n\n")
    h.close()
