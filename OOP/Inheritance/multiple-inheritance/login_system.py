class Database:
    def connect(self):
        print(f"Database connected")

class Logger:
    def write_log(self):
        print(f"Log written")

class Application(Database,Logger):
    def login(self):
        self.connect()
        self.write_log()
        print(f"Login successful")

app = Application()
app.login()