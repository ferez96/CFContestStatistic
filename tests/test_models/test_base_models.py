from models.base_model import Base


def test_inherited_class():
    class NewModel(Base):
        pass

    model = NewModel()
