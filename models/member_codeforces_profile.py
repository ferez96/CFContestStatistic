from .base_model import Base


class MemberCodeforcesProfile(Base):
    def __init__(self, handle, rank, rating):
        self.handle = handle
        self.rank = rank
        self.rating = rating

    def __repr__(self):
        return f"<MemberCodeforcesProfile>(handle={self.handle},rank={self.rank},rating={self.rating})"

    def __eq__(self, other):
        if not isinstance(other, MemberCodeforcesProfile):
            return False

        if self.handle != other.handle:
            return False
        if self.rank != other.rank:
            return False
        if self.rating != other.rating:
            return False

        return True

    @classmethod
    def load(cls, data):
        if not data:
            return None

        return cls(
            handle=data.get("handle"),
            rank=data.get("rank"),
            rating=data.get("rating"),
        )
