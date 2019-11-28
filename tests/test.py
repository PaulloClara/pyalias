from sys import argv


def main():
    try:
        print(f'\n\t{argv[1]}\n\n')
    except Exception as e:
        print('\n\tHello World\n\n')


if __name__ == '__main__':
    main()
