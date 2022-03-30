import pytest
from requests_mock import Mocker

from pyplaceholder.jsonplaceholder import JSONPlaceholder


class TestJSONPlaceholder(object):
    @Mocker(kw="http_mocker")
    def test_get_albums(self, **kwargs):
        kwargs["http_mocker"].get(
            "https://jsonplaceholder.typicode.com/albums", json=[{"id": 1}]
        )
        resp = JSONPlaceholder().get_albums()

        assert resp == [{"id": 1}]

    @Mocker(kw="http_mocker")
    def test_get_comments(self, **kwargs):
        kwargs["http_mocker"].get(
            "https://jsonplaceholder.typicode.com/comments", json=[{"id": 1}]
        )
        resp = JSONPlaceholder().get_comments()

        assert resp == [{"id": 1}]

    @Mocker(kw="http_mocker")
    def test_get_photos(self, **kwargs):
        kwargs["http_mocker"].get(
            "https://jsonplaceholder.typicode.com/comments", json=[{"id": 1}]
        )
        resp = JSONPlaceholder().get_comments()

        assert resp == [{"id": 1}]

    @pytest.mark.posts
    @Mocker(kw="http_mocker")
    def test_get_posts(self, **kwargs):
        kwargs["http_mocker"].get(
            "https://jsonplaceholder.typicode.com/posts", json=[{"id": 1}]
        )
        resp = JSONPlaceholder().get_posts()

        assert resp == [{"id": 1}]

    @pytest.mark.posts
    @Mocker(kw="http_mocker")
    def test_get_post(self, **kwargs):
        kwargs["http_mocker"].get(
            "https://jsonplaceholder.typicode.com/posts/1", json={"id": 1}
        )
        resp = JSONPlaceholder().get_post(1)

        assert resp == {"id": 1}

    @pytest.mark.posts
    @Mocker(kw="http_mocker")
    def test_get_post_comments(self, **kwargs):
        kwargs["http_mocker"].get(
            "https://jsonplaceholder.typicode.com/posts/1/comments", json={"id": 1}
        )
        resp = JSONPlaceholder().get_post_comments(1)

        assert resp == {"id": 1}

    @pytest.mark.posts
    @Mocker(kw="http_mocker")
    def test_create_post(self, **kwargs):
        kwargs["http_mocker"].post(
            "https://jsonplaceholder.typicode.com/posts", json={"id": 1}
        )
        resp = JSONPlaceholder().create_post({"id": 1})

        assert resp == {"id": 1}

    @pytest.mark.posts
    @Mocker(kw="http_mocker")
    def test_update_post(self, **kwargs):
        kwargs["http_mocker"].put(
            "https://jsonplaceholder.typicode.com/posts/1", json={"id": 1}
        )
        resp = JSONPlaceholder().update_post(1, {"user_id": 1})

        assert resp == {"id": 1}

    @pytest.mark.posts
    @Mocker(kw="http_mocker")
    def test_delete_post(self, **kwargs):
        kwargs["http_mocker"].delete(
            "https://jsonplaceholder.typicode.com/posts/1", json={"id": 1}
        )
        resp = JSONPlaceholder().delete_post(1)

        assert resp == {"id": 1}

    @Mocker(kw="http_mocker")
    def test_get_todos(self, **kwargs):
        kwargs["http_mocker"].get(
            "https://jsonplaceholder.typicode.com/todos", json=[{"id": 1}]
        )
        resp = JSONPlaceholder().get_todos()

        assert resp == [{"id": 1}]

    @Mocker(kw="http_mocker")
    def test_get_users(self, **kwargs):
        kwargs["http_mocker"].get(
            "https://jsonplaceholder.typicode.com/users", json=[{"id": 1}]
        )
        resp = JSONPlaceholder().get_users()

        assert resp == [{"id": 1}]
