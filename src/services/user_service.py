class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_user(self, username, password):
        if self.user_repository.user_exists(username):
            raise ValueError("User already exists")
        hashed_password = self.hash_password(password)
        user = {"username": username, "password": hashed_password}
        self.user_repository.save_user(user)
        return user

    def authenticate_user(self, username, password):
        user = self.user_repository.get_user(username)
        if user and self.verify_password(password, user['password']):
            return user
        raise ValueError("Invalid username or password")

    def hash_password(self, password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password, hashed_password):
        return self.hash_password(password) == hashed_password

    def get_user_data(self, username):
        user = self.user_repository.get_user(username)
        if user:
            return {"username": user['username']}
        raise ValueError("User not found")