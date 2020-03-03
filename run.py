from sys import argv
from subprocess import run as run_command


PYALIAS_PATH = argv[0]
CURRENT_PATH = argv[1]
FULL_FILE_PATH = argv[2].split('=')[1]

ARGS = list(filter(lambda arg: '--py' not in arg, argv[4:]))
ENV_ARGS = list(filter(lambda arg: '--py' in arg, argv[4:]))

DEV_MODE = '--pydev' in ENV_ARGS
LANG = FULL_FILE_PATH.split('.')[-1]

FILE_PATH = FULL_FILE_PATH.split('.')[0]
FULL_PATH = f'{CURRENT_PATH}/{FULL_FILE_PATH}'
TEMP_PATH = f'{"/".join(PYALIAS_PATH.split("/")[:-1])}/temp'

FILE_NAME = FILE_PATH.split('/')[-1]


def main():
    if not FULL_FILE_PATH:
        show_error('file not found')

    if LANG in ['c']:
        run_c()
    elif LANG in ['java']:
        run_java()
    elif LANG in ['py']:
        run_python()
    else:
        show_error(error='unsupported programming language')


def run_c():
    output_file_path = f'{TEMP_PATH}/run'

    compile_command = ['gcc', FULL_PATH, '-o', output_file_path]
    execution_command = [output_file_path]

    if ARGS:
        add_args(command=execution_command, ARGS=ARGS)

    show_log(f'compile: {compile_command}')
    show_log(f'execution: {execution_command}')

    run_command(compile_command)
    run_command(execution_command)


def run_java():
    package = FILE_PATH.split('/')

    if len(package) > 2:
        package = '/'.join(FILE_PATH.split('/')[-2:])
        other_path = FILE_PATH.replace(package, "")
        compile_command =\
            f'(cd {other_path} && javac {package}.{LANG} -d {TEMP_PATH})'
        execution_command = f'(cd {TEMP_PATH} && java {package})'
    else:
        compile_command = f'javac {FULL_PATH} -d {TEMP_PATH}'
        execution_command = f'(cd {TEMP_PATH} && java {FILE_PATH})'

    show_log(f'compile: {compile_command}')
    show_log(f'execution: {execution_command}')

    run_command(compile_command, shell=True)
    run_command(execution_command, shell=True)


def run_python():
    execution_command = ['python3', '-B', FULL_PATH]

    if ARGS:
        add_args(command=execution_command, ARGS=ARGS)

    show_log(f'execution: {execution_command}')
    run_command(execution_command)


def add_args(command, ARGS):
    for arg in ARGS:
        command.append(arg)

    return command


def show_log(msg):
    if DEV_MODE:
        print(f'\033[33m{msg.capitalize()}\033[0;0m')


def show_error(error, stop_exec=True):
    print(f'\n\033[31m"{error.capitalize()}"\033[0;0m\n')

    if stop_exec:
        exit(1)


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        show_error(error='sorry, unexpected error', stop_exec=not DEV_MODE)
        raise
