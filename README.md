# PyAlias

This project aims to increase developer productivity by decreasing the use of
commands used to execute/invoke programs/interpreters, regardless of the
programming language.

### Install

```bash
$ git clone https://github.com/paulloclara/pyalias.git ~/.pyalias && python3 ~/.pyalias/install.py
$ source ~/.<you_bashrc>
```

### Run

```bash
$ pyalias <file_name or file_path> <args or void>
```

### Update

```bash
$ (cd ~/.pyalias && git pull)
```

### Dev

```bash
$ git clone https://github.com/paulloclara/pyalias.git
$ cd pyalias
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
$ nano ~/.<you_bashrc> | ex: $ nano ~/.bashrc
```

Add the code at the end of the file:

```sh
function pyalias-dev() {
  python3 -B /run/media/paullo/dev/python/pyalias/run.py $(pwd) FULL_FILE_PATH=$1 $* --pydev
}
```

```bash
$ source ~/.<you_bashrc>
$ pyalias-dev <file_name or file_path> <args or void>
```
