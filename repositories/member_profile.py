from typing import List, Optional
from models import MemberProfile
from clients.mongodb_client import get_db


def get_member_profile_by_id(member_id) -> Optional[MemberProfile]:
    db = get_db()
    data = db["members"].find_one(member_id)
    if not data:
        return None
    return MemberProfile.load(data)
