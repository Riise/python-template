def main():
    msg = get_message()
    print(msg)


def get_message() -> str:
    return "Hello, World! This is a Python app running in a dev container!"


if __name__ == "__main__":
    main()
