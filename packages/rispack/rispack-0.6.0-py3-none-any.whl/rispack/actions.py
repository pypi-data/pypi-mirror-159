from rispack.stores import scoped_session

class BaseAction:
    @classmethod
    @scoped_session
    def call(cls, params):
        cls().call(params)
