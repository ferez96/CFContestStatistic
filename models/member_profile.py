from .base_model import Base
from .member_codeforces_profile import MemberCodeforcesProfile


class MemberProfile(Base):
    def __init__(self, name, codeforce_handle="", codeforces=None):
        self.name = name
        self.codeforces_handle = codeforce_handle
        self.codeforces = codeforces

    def __repr__(self):
        return f"<MemberProfile>(name={self.name},codeforces={self.codeforces},codeforces_handle={self.codeforces_handle})"

    def __eq__(self, other):
        if not isinstance(other, MemberProfile):
            return False

        if self.name != other.name:
            return False
        if self.codeforces_handle != other.codeforces_handle:
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
            codeforce_handle=data.get("codeforces_handle", ""),
            codeforces=MemberCodeforcesProfile.load(data.get("codeforces")),
        )

    def as_dict(self):
        return {
            "name": self.name,
            "codeforces_handle": self.codeforces_handle,
            "codeforces": self.codeforces.as_dict(),
        }
