import uuid


class OAuthStateStore:

    _states = {}

    @staticmethod
    def create(
        user_id: str
    ):

        state = str(
            uuid.uuid4()
        )

        OAuthStateStore._states[
            state
        ] = user_id

        return state

    @staticmethod
    def get_user(
        state: str
    ):

        return OAuthStateStore._states.pop(
            state,
            None
        )