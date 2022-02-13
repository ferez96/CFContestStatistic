from models.member_profile import MemberProfile


def test_create_new_instance():
    model = MemberProfile(
        name="Name",
    )

    assert model.name == "Name"
    assert model.codeforces is None


def test_str():
    assert str(MemberProfile(name="Name")) == "<MemberProfile>(name=Name,codeforces=None)"


def test_eq():
    assert MemberProfile(name="Name") == MemberProfile(name="Name")


def test_load():
    assert MemberProfile(name="Name") == MemberProfile.load({"name": "Name"})
