from typing import List, Optional
from models import MemberProfile
from clients.mongodb_client import get_db


def get_member_profile_by_id(member_id) -> Optional[MemberProfile]:
    db = get_db()
    data = db["members"].find_one(member_id)
    if not data:
        return None
    return MemberProfile.load(data)


def get_list_member_id() -> List[int]:
    db = get_db()
    ids = db["members"].find().distinct("_id")
    return [int(x) for x in ids]


def update_member_by_id(member_id, new_profile):
    db = get_db()
    db["members"].find_one_and_replace({"_id": member_id},
                                       new_profile.as_dict())
