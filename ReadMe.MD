# 概要
[Djangoクイックインストールガイドを実施した](https://docs.djangoproject.com/ja/3.2/intro/install/)

## pyenv(複数のPythonのバージョンを作成・管理)インストール
```
$ brew install pyenv
$ pyenv -v
pyenv 2.3.23

# インストール可能なPythonのバージョン一覧を表示できます。
pyenv install --list
pyenv install 3.12.0b4

# インストール済みのバージョンを確認する。
pyenv versions

# バージョンの切り替え
pyenv global 3.12.0b4

# インストール済みのバージョンを確認する。
pyenv versions
```

## venv(仮想環境作成・管理)
```
# 仮想環境の作成(-mはモジュール名指定)
$ python3 -m venv venv

# 有効化
$ source venv/bin/activate

# 終了
(.venv) $ deactivate
```

## Djangoをインストール
```
$ pip install Django==
$ pip install Django or pip install Django==3.2.13
$ python -m django --version
5.0.4
```

## プロジェクトを作成する
```
$ django-admin startproject mysite
```

## 開発用サーバー
```
$ cd mysite
$ python manage.py runserver
```

## アプリケーションを作成
```
$ python manage.py startapp polls
```

## 管理ユーザを作成
```
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
python manage.py runserver
```

## Database の設定
```
$ python manage.py migrate
```

## モデルを有効にする
```
// これらの変更のためのマイグレーションを作成するために python manage.py makemigrations を実行します。
python manage.py makemigrations polls
// データベースにこれらの変更を適用するために python manage.py migrate を実行します。
python manage.py migrate
```

## API　で遊んでみる
```
python manage.py shell
```

## テスト
```
python manage.py test polls/
```

## Djangoのソースファイル検索
```
$ python -c "import django; print(django.__path__)"
```

## その他ライブラリ
```
pip install django-debug-toolbar
```
