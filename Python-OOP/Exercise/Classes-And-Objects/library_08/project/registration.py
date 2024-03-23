from project.user import User
from project.library import Library


class Registration:

    def add_user(self, user: User, library: Library) -> str or None:
        if user not in library.user_records:
            library.user_records.append(user)
            return None

        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library) -> str or None:
        if user in library.user_records:
            library.user_records.remove(user)
            return None

        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            old_user = next(filter(lambda u: u.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if old_user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"

        if library.rented_books.get(old_user):
            library.rented_books[new_username] = library.rented_books.pop(old_user.username)

        old_user.username = new_username

        return f"Username successfully changed to: {new_username} for user id: {user_id}"
