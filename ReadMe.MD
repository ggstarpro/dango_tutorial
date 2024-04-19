# 概要
[Djangoクイックインストールガイドを実施した](https://docs.djangoproject.com/ja/3.2/intro/install/)

## 仮想環境作成
$ python3 -m venv venv
$ source venv/bin/activate

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
