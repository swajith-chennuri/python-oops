from AbstractPassword import AbstractPassword
class Authenticate(AbstractPassword):
    def authenticate(self):
        while self.attempts > 0:
            user_input = input("Enter the password: ")
            if user_input == self.password:
                print("Welcome")
                break
            else:
                self.attempts -= 1
                if self.attempts > 0:
                    print(f"Wrong password! You have {self.attempts} attempts left.")
                else:
                    print("Your account is blocked.")
                    break