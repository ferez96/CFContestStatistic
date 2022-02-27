import logging
from marshmallow import Schema, fields

from clients.codeforces import CodeforcesHttpClient
import models
from repositories.member_profile import get_list_member_id, get_member_profile_by_id, update_member_by_id
from repositories.member_codeforces_profile import fetch_member_codeforces_profile

_logger = logging.getLogger(__name__)


def load_members_list(path_to_json_file):
    pass


def fetch_codeforces_profile_by_handle(codeforces_handle):
    """Fetch user profile from codeforces APIs

    Returns:
        updated profile
    """
    try:
        client = CodeforcesHttpClient()
        data = client.send_request("user.info", {"handles": codeforces_handle})
    except Exception as e:
        _logger.error(f"fail to fetch codeforces profile. Message: {e}", exc_info=True)
        return None

    if len(data) == 0:
        _logger.error(f"there is no user with handle: {codeforces_handle}")
        return None

    return models.MemberCodeforcesProfile(
        handle=codeforces_handle,
        rating=data[0].get("rating"),
        rank=data[0].get("rank")
    )


def update_member_profile_all():
    all_ids = get_list_member_id()
    for member_id in all_ids:
        update_member_profile_by_id(member_id)


def update_member_profile_by_id(member_id):
    print(f"update profile for member with id {member_id}")
    member_profile = get_member_profile_by_id(member_id)
    handle = member_profile.codeforces_handle
    member_profile.codeforces = fetch_member_codeforces_profile(handle)
    print(member_profile)
    update_member_by_id(member_id, member_profile)
