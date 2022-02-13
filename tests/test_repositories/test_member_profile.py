import pytest
from unittest import mock
from models import MemberProfile, MemberCodeforcesProfile
from repositories.member_profile import get_member_profile_by_id


def test_get_member_profile_by_id_happy(mongodb_with_members):
    with mock.patch("clients.mongodb_client._get_db") as _get_db:
        _get_db.return_value = mongodb_with_members
        expected = MemberProfile(
            name="Duong Thai Minh",
            codeforces=MemberCodeforcesProfile(
                handle="I_UsedTo_Love_You",
                rank=None,
                rating=1500
            )
        )
        member = get_member_profile_by_id(1)
        assert member == expected


@mock.patch("clients.mongodb_client._get_db")
def test_get_member_profile_by_id_not_existed(_get_db, mongodb_with_members):
    _get_db.return_value = mongodb_with_members
    expected = None
    member = get_member_profile_by_id(9999)
    assert member == expected
