from os import path

PYALIAS = '\nfunction pyalias() {\n\
  python3 -B ~/.pyalias/run.py $(pwd) $*\n\
}\n'


def main():
    installed = False
    bash_file_path = path.expanduser('~/.zshrc')

    try:
        bash_file = open(bash_file_path, 'r')
    except FileNotFoundError as e:
        bash_file_path = path.expanduser('~/.bashrc')
        bash_file = open(bash_file_path, 'r')

    bash_file_content = bash_file.readlines()
    bash_file.close()

    for line in bash_file_content:
        if 'pyalias' in line:
            installed = True
            break

    if not installed:
        bash_file_content.append(PYALIAS)

        try:
            bash_file = open(bash_file_path, 'w')
            bash_file.writelines(bash_file_content)
        except Exception as e:
            raise
        finally:
            bash_file.close()

    print('\n\n\tPyAlias installed\n\tRestart the terminal\n\n')


if __name__ == '__main__':
    main()
