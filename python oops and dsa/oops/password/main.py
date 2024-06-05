from password import Authenticate
def main():
    p1 = Authenticate(password="swajith123", attempts=3)
    p1.authenticate()

main()