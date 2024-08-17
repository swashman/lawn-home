# LAWN HOME APP<a name="lawn-home-app"></a>

![License](https://img.shields.io/badge/license-GPLv3-green)
![python](https://img.shields.io/badge/python-3.10-informational)
![django](https://img.shields.io/badge/django-3.2-informational)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

_(These badges are examples, you can and should replace them with your own)_

______________________________________________________________________

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=1 -->

- [LAWN HOME APP](#lawn-home-app)
  - [How to Use It](#how-to-use-it)
    - [Cloning From Repo](#cloning-from-repo)
  - [Installing Into Your Dev AA](#installing-into-your-dev-aa)
  - [Installing Into Production AA](#installing-into-production-aa)

<!-- mdformat-toc end -->

______________________________________________________________________

## How to Use It<a name="how-to-use-it"></a>

### Cloning From Repo<a name="cloning-from-repo"></a>

For this app, we're assuming that you have all your AA projects, your virtual
environment, and your AA installation under one top folder (e.g. aa-dev).

This should look something like this:

```text
aa-dev
|- venv/
|- myauth/
|- lawn-home
|- (other AA projects ...)
```

```bash
git clone https://github.com/swashman/lawn-home.git lawn-home
cd lawn-home
pre-commit install
```

## Installing Into Your Dev AA<a name="installing-into-your-dev-aa"></a>

Once you've cloned or copied all files into place, you're ready to install it to your dev AA instance.

Make sure you're in your venv. Then install it with pip in editable mode:

```bash
pip install -e lawn-home
```

First add your app to the Django project by adding the name of your app to
INSTALLED_APPS in `settings/local.py`.

Make sure you are in aa-dev/myauth
Then migrate

```bash
python manage.py migrate
```

Finally, restart your AA server and that's it.

## Installing Into Production AA<a name="installing-into-production-aa"></a>

To install your plugin into a production AA, run this command within the virtual
Python environment of your AA installation:

```bash
pip install git+https://github.com/swashman/lawn-home
```

Then add your app to `INSTALLED_APPS` in `settings/local.py`, run migrations/collectstatic and
restart your allianceserver.
