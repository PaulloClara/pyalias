import subprocess
from sys import argv


class App:

    def __init__(self):
        self.args = argv[3:]
        self.lang = argv[2].split('.')[-1]
        self.current_path = argv[1]
        self.file_path = '.'.join(argv[2].split('.')[:-1])
        self.full_path = f'{self.current_path}/{self.file_path}.{self.lang}'

    def run(self):
        if self.lang in ['c']:
            self.run_c()
        elif self.lang in ['py']:
            self.run_python()
        else:
            print('\033[31mSorry, unsupported programming language...\033[0;0m')

    def run_c(self):
        output_file_path = f'{self.current_path}/run'

        compile_command = ['gcc', self.full_path, '-o', output_file_path]
        run_output_file = [output_file_path]

        if self.args:
            self._add_args(run_output_file)

        subprocess.run(compile_command)
        subprocess.run(run_output_file)

    def run_python(self):
        run_command = ['python3', self.full_path]

        if self.args:
            self._add_args(run_command)

        subprocess.run(run_command)

    def _add_args(self, command):
        for arg in self.args:
            command.append(arg)

        return command


if __name__ == '__main__':
    app = App()
    app.run()
