import logging
from marshmallow import Schema, fields

from clients.codeforces import CodeforcesHttpClient
import models

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
    pass
