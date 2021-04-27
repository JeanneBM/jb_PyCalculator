from src import *

import os
import shutil

import pytest
from flask import render_template, render_template_string, request
from jinja2.exceptions import TemplateNotFound
from jinja2.sandbox import SecurityError
from werkzeug.test import Client

from CTFd.config import TestingConfig
from CTFd.utils import get_config, set_config
from tests.helpers import create_ctfd, destroy_ctfd, gen_user, login_as_user


def test_themes_run_in_sandbox():
    app = create_ctfd()
    with app.app_context():
        try:
            app.jinja_env.from_string(
                "{{ ().__class__.__bases__[0].__subclasses__()[40]('./test_utils.py').read() }}"
            ).render()
        except SecurityError:
            pass
        except Exception as e:
            raise e
    destroy_ctfd(app)


def test_themes_cant_access_configpy_attributes():


## ... source file abbreviated to get to render_template examples ...


            except TemplateNotFound:
                pass
    destroy_ctfd(app)

    class ThemeFallbackConfig(TestingConfig):
        THEME_FALLBACK = True

    app = create_ctfd(config=ThemeFallbackConfig)
    with app.app_context():
        set_config("ctf_theme", "foo")
        assert app.config["THEME_FALLBACK"] == True
        with app.test_client() as client:
            r = client.get("/")
            assert r.status_code == 200
            r = client.get("/themes/foo/static/js/pages/main.dev.js")
            assert r.status_code == 200
    destroy_ctfd(app)

    os.rmdir(os.path.join(app.root_path, "themes", "foo"))


def test_theme_template_loading_by_prefix():
    app = create_ctfd()
    with app.test_request_context():
        tpl1 = render_template_string("{% extends 'core/page.html' %}", content="test")
        tpl2 = render_template("page.html", content="test")
        assert tpl1 == tpl2


def test_theme_template_disallow_loading_admin_templates():
    app = create_ctfd()
    with app.app_context():
        try:
            filename = os.path.join(
                app.root_path, "themes", "foo", "admin", "malicious.html"
            )
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                f.write("malicious")

            with pytest.raises(TemplateNotFound):
                render_template_string("{% include 'admin/malicious.html' %}")
        finally:
            shutil.rmtree(
                os.path.join(app.root_path, "themes", "foo"), ignore_errors=True
            )



## ... source file continues with no further render_template examples...
