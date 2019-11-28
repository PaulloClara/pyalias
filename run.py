import subprocess
from sys import argv


def show_error(error, stop_exec=True):
    error = f'\033[31m"{error}"\033[0;0m\n\n'

    print('\n')
    if stop_exec:
        raise Exception(error)
    else:
        print(error)


if len(argv) < 3:
    show_error('file not found')

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
        show_error(error='unsupported programming language')


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


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        if '\n\n' in err.args[0]:
            raise
        show_error(error='sorry, unexpected error', stop_exec=False)
