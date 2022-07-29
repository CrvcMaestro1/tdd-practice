class Login:
  def login(self, username: str, password: str):
    if username == "" or password == "":
      raise ValueError("User and pass must not be empty")