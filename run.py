import subprocess
from sys import argv


args = argv[3:]
lang = argv[2].split('.')[-1]
current_path = argv[1]
file_path = '.'.join(argv[2].split('.')[:-1])
full_path = f'{current_path}/{file_path}.{lang}'


def main():
    if lang in ['c']:
        run_c()
    elif lang in ['py']:
        run_python()
    else:
        show_error('unsupported programming language')


def run_c():
    output_file_path = f'{current_path}/run'

    compile_command = ['gcc', full_path, '-o', output_file_path]
    execution_command = [output_file_path]

    if args:
        add_args(execution_command)

    subprocess.run(compile_command)
    subprocess.run(execution_command)


def run_python():
    execution_command = ['python3', '-B', full_path]

    if args:
        add_args(execution_command)

    subprocess.run(execution_command)


def add_args(command):
    for arg in args:
        command.append(arg)

    return command


def show_error(error):
    print('\n')
    raise Exception(f'\033[31m"{error}"\033[0;0m\n\n')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        show_error('sorry, unexpected error')
