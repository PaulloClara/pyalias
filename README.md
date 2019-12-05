# PyAlias

### INSTALL

1. clone repository\
  `$ git clone https://github.com/paulloclara/pyalias.git ~/.pyalias && python3 ~/.pyalias/install.py`

2. update terminal settings\
  restart the terminal or `$ source ~/.<youbashrc>`

### RUN

`$ pyalias <file_name or file_path> <args or void>`

### UPDATE

`$ (cd ~/.pyalias && git pull)`

### DEV

`$ git clone https://github.com/paulloclara/pyalias.git`\
`$ cd pyalias`\
`$ python3 -m venv .env`\
`$ source .env/bin/activate`\
`$ pip install -r requirements.txt`\
`$ nano ~/.<youbashrc>` ex `$ nano ~/.bashrc`
```
function pyalias-dev() {
  python3 -B <full_project_path>/pyalias/run.py $(pwd) $*
}
```
`$ source ~/.<youbashrc>`\
use `$ pyalias-dev <file_name or file_path> <args or void>`
