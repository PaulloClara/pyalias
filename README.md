# PyAlias

### Install

1. access terminal settings\
   `$ sudo nano ~/.zshrc` or `$ sudo nano ~/.bashrc`

2. add code at end of file

```
function pyalias() {
  python -B /run/media/paullo/dev/python/pyalias/run.py $(pwd) $\*
}
```

3. update terminal settings\
   `$ source ~/.zshrc` or `$ source ~/.bashrc`

### RUN

`$ pyalias file_name.file_lang args` ex: `$ pyalias run.c arg1 arg2 arg...`
