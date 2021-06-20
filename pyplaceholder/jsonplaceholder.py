"""
Free fake API routes from https://jsonplaceholder.typicode.com/

"""
import pyplaceholder


class PyPlaceholderException(Exception):

    def __init__(self, error, response):
        self.error = error
        self.response = response
        self.headers = response.headers

    def __str__(self):
        return self.error

    def __eq__(self, other):
        if isinstance(other, "".__class__):
            return self.error == other
        elif isinstance(other, self.__class__):
            return self.error == other.error and self.headers == other.headers
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return super(PyPlaceholderException).__hash__()


def raise_status(response):
    """Raise an exception if the request did not return a status code of 200 or 201.

    :param response: Request response body
    """

    if response.status_code not in [200, 201]:
        try:
            response_json = response.json()
        except ValueError:
            response_json = {'error': response.content}

        try:
            failure = response_json['error']
        except (KeyError, IndexError, TypeError):
            failure = str(response_json)

        if response.status_code == 401:
            raise PyPlaceholderException('401, Unauthorized. ' + failure, response)
        elif response.status_code == 403:
            raise PyPlaceholderException('403, Forbidden. ' + failure, response)
        elif response.status_code == 404:
            raise PyPlaceholderException('404, Not Found. ' + failure, response)
        elif response.status_code == 400:
            raise PyPlaceholderException('400, Bad Request. ' + failure, response)
        elif response.status_code == 410:
            raise PyPlaceholderException('410, Gone. ' + failure, response)
        elif response.status_code == 429:
            raise PyPlaceholderException('429, Client Error. ' + failure, response)
        elif response.status_code == 500:
            raise PyPlaceholderException('500, Server Error. ' + failure, response)
        else:
            response.raise_for_status()


class JSONPlaceholder(object):

    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'

    def _get_response(self, endpoint):
        url = f'{self.base_url}/{endpoint}'

        response = pyplaceholder.request(
            'get',
            url
        )

        return response.json()

    def get_albums(self):
        """ Get albums.

        Example:

            print(ph.get_albums())

        :return: JSON response as dict.
        """
        return self._get_response('albums')

    def get_comments(self):
        """ Get comments.

        Example:

            print(ph.get_comments())

        :return: JSON response as dict.
        """
        return self._get_response('comments')

    def get_photos(self):
        """ Get photos.

        Example:

            print(ph.get_photos())

        :return: JSON response as dict.
        """
        return self._get_response('photos')

    def get_posts(self):
        """ Get posts.

        Example:

            print(ph.get_posts())

        :return: JSON response as dict.
        """
        return self._get_response('posts')

    def get_post(self, post_id):
        """ Get a post.

        Example:

            print(ph.get_post(1))

        :param post_id:
        :return: JSON response as dict.
        """
        return self._get_response(f'posts/{post_id}')

    def get_post_comments(self, post_id):
        """ Get a post's comments.

        Example:

            print(ph.get_post_comments(1))

        :param post_id:
        :return: JSON response as dict.
        """
        return self._get_response(f'posts/{post_id}/comments')

    def create_post(self, data):
        """ Create a post.

        Note: resource will not be really updated on the server but it will be faked as if.

        Example:

            data = {
                'title': 'test title',
                'body': 'test body',
                'userId': 1
            }

            print(ph.create_post(data))

        :param data:
        :return: JSON response as dict.
        """
        url = f'{self.base_url}/posts'

        response = pyplaceholder.request(
            'post',
            url,
            json=data
        )

        return response.json()

    def update_post(self, post_id, data):
        """ Create a post.

        Note: resource will not be really updated on the server but it will be faked as if.

        Example:

            data = {
                'title': 'update title',
                'body': 'update body',
                'userId': 1
            }

            print(ph.update_post(data))

        :param post_id:
        :param data:
        :return: JSON response as dict.
        """
        url = f'{self.base_url}/posts/{post_id}'

        response = pyplaceholder.request(
            'put',
            url,
            json=data
        )

        return response.json()

    def delete_post(self, post_id):
        """ Delete a post.

        Note: resource will not be really updated on the server but it will be faked as if.

        Example:

            print(ph.delete_post(1))

        :param post_id:
        :return: JSON response as dict.
        """
        url = f'{self.base_url}/posts/{post_id}'

        response = pyplaceholder.request(
            'delete',
            url
        )

        return response.json()

    def get_todos(self):
        """ Get todos.

        Example:

            print(ph.get_todos())

        :return: JSON response as dict.
        """
        return self._get_response('todos')

    def get_users(self):
        """ Get users.

        Example:

            print(ph.get_users())

        :return: JSON response as dict.
        """
        return self._get_response('users')
