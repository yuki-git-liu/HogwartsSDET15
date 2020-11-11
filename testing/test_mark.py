# coding = utf-8
import pytest


@pytest.mark.login
def test_login1():
    print('登录用例')


@pytest.mark.search
def test_search():
    print('搜索用例')
