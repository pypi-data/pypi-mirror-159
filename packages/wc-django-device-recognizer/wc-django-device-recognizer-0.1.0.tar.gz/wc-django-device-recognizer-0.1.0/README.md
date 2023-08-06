# WebCase device recognizing utility

## Installation

```sh
pip install wc-django-device-recognizer
```

It depends on `django-user-agents`, so check out [it's documentation](https://pypi.org/project/django-user-agents/) about additional installation instructions.

In `settings.py`:

```python
INSTALLED_APPS += [
  'wcd_device_recognizer',
]
```

## Usage

To get all possible information from request:

```python
from wcd_device_recognizer.services import request_resolver

interlocutor = request_resolver.resolve(request)

assert interlocutor.device.bitness == '64'
assert interlocutor.os.family == 'Linux'
assert interlocutor.os.arch == 'x86'
assert interlocutor.app.family == 'Chrome'
assert interlocutor.app.version == (101, 0, 0)
assert interlocutor.device.dpr == 1
```

And then you may save interlocutor's data to database:

```python
from wcd_device_recognizer.services import registry

# You may pass any amount of interlocutors to register here.
registry.register_interlocutors((interlocutor,))
```