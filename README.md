# PyAlias

### INSTALL

1. clone repository\
  `$ git clone https://github.com/paulloclara/pyalias.git ~/.pyalias`

2. access terminal settings\
  `$ sudo nano ~/.bashrc`

3. add code at end of file

```
function pyalias() {
  python3 -B ~/.pyalias/run.py $(pwd) $*
}
```

4. update terminal settings\
  `$ source ~/.bashrc`

### RUN

`$ pyalias file_name args`

### UPDATE

`$ (cd ~/.pyalias && git pull)`
