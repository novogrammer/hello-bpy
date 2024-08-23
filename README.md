# Hello bpy

PythonとしてBlenderを実行できるようになったそうなので試す。

## 前提
+ python3
+ venv


## 導入

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.lock
$ deactivate
```

## venvに入る
```
$ source .venv/bin/activate
```

## venvから出る
```
$ deactivate
```

## 実行

venvに入った状態で

```
$ python ./hello.py
```


