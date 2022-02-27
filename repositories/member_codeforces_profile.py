from clients.codeforces import CodeforcesHttpClient
from models import MemberCodeforcesProfile


def fetch_member_codeforces_profile(codeforces_handle):
    client = CodeforcesHttpClient()
    profile = client.send_request("user.info", {"handles": codeforces_handle})
    if profile:
        return MemberCodeforcesProfile.load(profile[0])

    return None
