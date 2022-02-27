import pytest
from unittest import mock
from models import MemberProfile, MemberCodeforcesProfile
from repositories.member_profile import (
    get_member_profile_by_id,
    get_list_member_id
)

_GET_DB_PATCH_PATH_ = "clients.mongodb_client._get_db"


def test_get_member_profile_by_id_happy(mongodb_with_members):
    with mock.patch(_GET_DB_PATCH_PATH_) as _get_db:
        _get_db.return_value = mongodb_with_members
        expected = MemberProfile(
            name="Duong Thai Minh",
            codeforce_handle="I_UsedTo_Love_You",
            codeforces=MemberCodeforcesProfile(
                handle="I_UsedTo_Love_You",
                rank=None,
                rating=1500
            )
        )
        member = get_member_profile_by_id(1)
        assert member == expected


def test_get_member_profile_by_id_missing_codeforces_profile(mongodb_with_members):
    with mock.patch(_GET_DB_PATCH_PATH_) as _get_db:
        _get_db.return_value = mongodb_with_members
        expected = MemberProfile(
            name="Truong Cong Thanh",
            codeforce_handle="TYT",
            codeforces=None
        )
        member = get_member_profile_by_id(2)
        assert member == expected


def test_get_member_profile_by_id_not_existed(mongodb_with_members):
    with mock.patch(_GET_DB_PATCH_PATH_) as _get_db:
        _get_db.return_value = mongodb_with_members
        expected = None
        member = get_member_profile_by_id(9999)
        assert member == expected


def test_get_list_member_id(mongodb_with_members):
    with mock.patch(_GET_DB_PATCH_PATH_) as _get_db:
        _get_db.return_value = mongodb_with_members
        expected = [1, 2]
        ids = get_list_member_id()
        assert ids == expected
