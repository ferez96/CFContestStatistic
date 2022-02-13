from models.member_codeforces_profile import MemberCodeforcesProfile


def test_create_new_instance():
    model = MemberCodeforcesProfile(
        handle="handle",
        rating=1500,
        rank="Specialist"
    )

    assert model.handle == "handle"
    assert model.rating == 1500
    assert model.rank == "Specialist"


def test_str():
    assert str(MemberCodeforcesProfile(
        handle="handle",
        rating=1500,
        rank="Specialist"
    )) == "<MemberCodeforcesProfile>(handle=handle,rank=Specialist,rating=1500)"


def test_eq():
    assert MemberCodeforcesProfile(
        handle="handle",
        rating=1500,
        rank="Specialist"
    ) == MemberCodeforcesProfile(
        handle="handle",
        rating=1500,
        rank="Specialist"
    )


def test_load():
    assert MemberCodeforcesProfile(
        handle="handle",
        rating=1500,
        rank="Specialist"
    ) == MemberCodeforcesProfile.load(
        {
            "handle": "handle",
            "rating": 1500,
            "rank": "Specialist"
        }
    )
