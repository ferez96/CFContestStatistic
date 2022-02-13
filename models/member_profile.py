from .base_model import Base
from .member_codeforces_profile import MemberCodeforcesProfile


class MemberProfile(Base):
    def __init__(self, name, codeforces=None):
        self.name = name
        self.codeforces = codeforces

    def __repr__(self):
        return f"<MemberProfile>(name={self.name},codeforces={self.codeforces})"

    def __eq__(self, other):
        if not isinstance(other, MemberProfile):
            return False

        if self.name != other.name:
            return False
        if self.codeforces != other.codeforces:
            return False

        return True

    @classmethod
    def load(cls, data):
        if not data:
            return None
        return cls(
            name=data.get("name"),
            codeforces=MemberCodeforcesProfile.load(data.get("codeforces")),
        )
