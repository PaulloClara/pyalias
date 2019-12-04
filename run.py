from sys import argv
from subprocess import run as run_command


ARGS = argv[3:]
LANG = argv[2].split('.')[-1]
FILE_PATH = '.'.join(argv[2].split('.')[:-1])
FILE_NAME = FILE_PATH.split('/')[-1]
CURRENT_PATH = argv[1]
FULL_PATH = f'{CURRENT_PATH}/{FILE_PATH}.{LANG}'
TEMP_PATH = f'{"/".join(argv[0].split("/")[:-1])}/temp'


def main():
    if len(argv) < 3:
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
        execution_command = f'(cd {TEMP_PATH} && java {FILE_NAME})'

    print(compile_command)
    print(execution_command)
    run_command(compile_command, shell=True)
    run_command(execution_command, shell=True)


def run_python():
    execution_command = ['python3', '-B', FULL_PATH]

    if ARGS:
        add_args(command=execution_command, ARGS=ARGS)

    run_command(execution_command)


def add_args(command, ARGS):
    for arg in ARGS:
        command.append(arg)

    return command


def show_error(error, stop_exec=True):
    error = f'\033[31m"{error}"\033[0;0m\n\n'

    print('\n')
    if stop_exec:
        raise Exception(error)
    else:
        print(error)


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        if type(err.ARGS[0]) == str and '\n\n' in err.ARGS[0]:
            raise
        show_error(error='sorry, unexpected error', stop_exec=False)
