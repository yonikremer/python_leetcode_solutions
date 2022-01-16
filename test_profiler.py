def long_function():
    _ = [i for i in range(2**16)]


def short_function():
    _ = [i for i in range(32)]


def main():
    long_function()
    short_function()


if __name__ == "__main__":
    main()
