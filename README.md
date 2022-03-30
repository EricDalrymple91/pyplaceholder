# PyPlaceholder

A simple python (3.6+) wrapper for [JSON Placeholder free fake API](https://jsonplaceholder.typicode.com/).

# Table of contents

+ [Installation](#installation)
+ [Usage](#usage)
+ [Tests](#tests)  
+ [Changelog](#changelog)

# Installation

1. go [here](https://github.com/EricDalrymple91/pyplaceholder) and clone the repo
2. Install [Poetry](https://python-poetry.org/docs/)
3. Run the following:

    poetry install

# Usage

```python
import pyplaceholder

pyplaceholder.logger.setLevel('INFO')

ph = pyplaceholder.JSONPlaceholder()

# Get albums
for album in ph.get_albums():
    pyplaceholder.logger.info(album)

# Get Comments
for comment in ph.get_comments():
    pyplaceholder.logger.info(comment)

# Get photos
for photo in ph.get_photos():
    pyplaceholder.logger.info(photo)

# Get posts
for post in ph.get_posts():
    pyplaceholder.logger.info(post)

# Get a specific post
pyplaceholder.logger.info(ph.get_post(1))

# Get a specific post's comments
pyplaceholder.logger.info(ph.get_post_comments(1))

# Create a post
data = {
    'title': 'test title',
    'body': 'test body',
    'userId': 1
}
pyplaceholder.logger.info(ph.create_post(data))

# Update a post
data = {
    'title': 'update title',
    'body': 'update body',
    'userId': 1
}
pyplaceholder.logger.info(ph.update_post(1, data))

# Delete a post
pyplaceholder.logger.info(ph.delete_post(1))

# # Get todos
for todo in ph.get_todos():
    pyplaceholder.logger.info(todo)

# Get users
for user in ph.get_users():
    pyplaceholder.logger.info(user)
```

# Tests

Run test:

```
poetry shell
pytest
```

# Changelog

### 0.2 (2/2/22)

- Added tests.
- General cleanup.

### 0.1 (6/20/21)

- Initial release.

[Back to top](#pyplaceholder)