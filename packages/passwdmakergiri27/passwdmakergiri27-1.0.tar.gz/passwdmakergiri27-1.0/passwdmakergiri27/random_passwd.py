def random_passwd():
    import sys
    if len(sys.argv) == 1:
        print("Password is required to execute script: ")
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == "gowda":
            print("successfully validated")
            import random
            import string
            letter = "".join(random.choices(string.ascii_letters, k=2))
            number = "".join(random.choices(string.digits, k=2))
            print(f"The new paswword is : {letter+number}")
        else:
            print("invalid passwd")
    else:
        print("Expected only one argument")

random_passwd()
