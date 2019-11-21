import subprocess
from sys import argv


class App:
    def __init__(self):
        self.current_path = argv[1]
        self.lang = argv[2].split('.')[-1]
        self.file_path = '.'.join(argv[2].split('.')[:-1])
        self.args = argv[3:]
        self.path = f'{self.current_path}/{self.file_path}.{self.lang}'

    def run(self):
        if self.lang in ['c']:
            self.run_c()

    def run_c(self):
        output_file_path = f'{self.current_path}/run'

        compile_command = ['gcc', self.path, '-o', output_file_path]
        run_output_file = [output_file_path]

        if self.args:
            for arg in self.args:
                run_output_file.append(arg)

        subprocess.run(compile_command)
        subprocess.run(run_output_file)


if __name__ == '__main__':
    app = App()
    app.run()
