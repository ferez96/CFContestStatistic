from unittest import mock
from models import MemberCodeforcesProfile
from repositories.member_codeforces_profile import fetch_member_codeforces_profile


def _mock_send_request(method_name: str, params: dict):
    return [
        {
            "handle": "test_handler",
            "rating": 1500,
            "rank": "Specialist",
        },
    ]


@mock.patch("clients.codeforces.CodeforcesHttpClient.send_request", mock.Mock(side_effect=_mock_send_request))
def test_fetch_member_codeforces_profile():
    expected = MemberCodeforcesProfile(
        handle="test_handler",
        rating=1500,
        rank="Specialist",
    )
    profile = fetch_member_codeforces_profile("test_handler")
    assert profile == expected
