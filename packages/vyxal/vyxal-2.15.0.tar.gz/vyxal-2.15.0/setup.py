# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vyxal']

package_data = \
{'': ['*']}

install_requires = \
['num2words>=0.5.10,<0.6.0', 'sympy>=1.9,<2.0']

entry_points = \
{'console_scripts': ['vyxal = vyxal.main:cli']}

setup_kwargs = {
    'name': 'vyxal',
    'version': '2.15.0',
    'description': 'A golfing language that has aspects of traditional programming languages.',
    'long_description': '# Vyxal\n\n![Vyxal Logo](./documents/logo/vylogo.png)\n\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Vyxal/Vyxal.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Vyxal/Vyxal/context:python) ![Test status](https://github.com/Vyxal/Vyxal/actions/workflows/run-tests.yaml/badge.svg)\n\n**Vyxal** is a golfing language that takes the idea that conciseness comes at the cost of practicality and throws it out the window. That\'s right - where other golflangs throw you into the deep-end of keyboard mashing, Vyxal eases you into the concept of elegantly crafting built-ins into a functioning program.\n\nAnd yes, this design goal really _does_ warrant adding another golfing language into the already densely populated mix of golflangs. If you go and take a look at the current state of the art of golfing languages, you\'ll find that 99% of languages are either a) powerful and concise, but not easy to pick up or b) easy to learn, but not that useful for anything non-trivial (I say this as someone who\'s made and contributed to both kinds of languages). Vyxal aims to bridge the gap between simplicity and "golfability".\n\n## Installation\n\nYou can also use the [online interpreter](https://vyxal.pythonanywhere.com) with no need to install!\n\nIf you only want to run Vyxal, all you need to run is this:\n\n```\npip install vyxal\n```\n\nIf you are working on Vyxal, install [Poetry](https://python-poetry.org), and then you can clone this repo and run:\n\n```\npoetry install\n```\n\n## Usage\n\nTo run using the script:\n\n```\nvyxal <file> <flags (single string of flags)> <input(s)>\n```\n\nIf you\'re using Poetry:\n\n```\npoetry run vyxal <file> <flags (single string of flags)> <input(s)>\n```\n\nTo run tests, install pytest and simply run `pytest tests`.\n\n## Why Vyxal?\n\nVyxal is designed to be easy to use coming from practical programming languages like Python and C, and borrows many concepts from those, such as [variables], [functions], [conditionals and loops], comments and more. Despite this, it\'s also heavily optimised for golfing, with a large library of powerful [builtins](https://github.com/Vyxal/Vyxal/blob/main/documents/knowledge/elements.md) that can easily be chained to complete the task at hand. For more information, see the [tutorial](https://vyxapedia.hyper-neutrino.xyz/beginners).\n\n[variables]: https://vyxal.pythonanywhere.com/#WyIiLCIiLCIjIFZhcmlhYmxlcyBhcmUgZGVub3RlZCB3aXRoIHRoZSBzeW1ib2xzIOKGkiBhbmQg4oaQIGZvbGxvd2VkIGJ5IGFueSBudW1iZXIgb2YgYWxwaGFiZXRpYyBjaGFyYWN0ZXJzLlxuXG4jIOKGkiBzZXRzIGEgdmFyaWFibGUgdG8gdGhlIHZhbHVlIHBvcHBlZCBmcm9tIHRoZSBzdGFjay5cbmBIZWxsb2Ag4oaSZ3JlZXRpbmdcbiMgVGhlIHZhbHVlIFwiSGVsbG9cIiBpcyBub3cgc3RvcmVkIGluIHRoZSB2YXJpYWJsZSBncmVldGluZy5cblxuIyDihpAgcHVzaGVzIHRoZSB2YWx1ZSBvZiBhIHZhcmlhYmxlIHRvIHRoZSBzdGFjay5cblxu4oaQZ3JlZXRpbmciLCIiLCIiXQ==\n[functions]: https://vyxal.pythonanywhere.com/#WyIiLCIiLCJAZmlib25hY2NpOk58ICAgICAgICAgICAgICAgICMgZGVmIGZpYm9uYWNjaShOKTpcbiAg4oaQTiAwID0gWyAwIHwgICAgICAgICAgICAgICAjICAgaWYgTiA9PSAwOiByZXR1cm4gMFxuICAgIOKGkE4gMSA9IFsgMSB8ICAgICAgICAgICAgICMgICBlbGlmIE4gPT0gMTogcmV0dXJuIDFcbiAgICAgIOKGkE4gMiAtIEBmaWJvbmFjY2k7ICAgICAjICAgZWxzZTogcmV0dXJuIGZpYm9uYWNpaShOIC0gMikgKyBmaWJvbmFjaWkoTiAtIDEpXG4gICAgICDihpBOIDEgLSBAZmlib25hY2NpOyArXG4gICAgXVxuICBdXG47XG5cbjEwIEBmaWJvbmFjY2k7IiwiIiwiIl0=\n[conditionals and loops]: https://vyxal.pythonanywhere.com/#WyIiLCIiLCIjIElmIHN0YXRlbWVudHMgc3RhcnQgd2l0aCBbIGFuZCBlbmQgd2l0aCBdXG5cblxuMSAyICsgMyA9IFsgIyBJZiAxICsgMiA9IDMuLi5cbiAgICAgICAgICAgICMgRG8gc3R1ZmYgaGVyZVxuIFxuICAgfCAgICAgICAgIyB8IGluc2lkZSBhbiBpZiBzdGF0ZW1lbnQgZnVuY3Rpb25zIGFzIGFuIGVsc2UgY2xhdXNlXG4gICAgICAgICAgICAjIERvIHN0dWZmIGhlcmUgaWYgMSArIDIg4omgIDNcbl1cblxuIyBGb3IgbG9vcHMgbG9vcCBvdmVyIGVhY2ggZWxlbWVudCBvZiBhIHN0cmluZy9hcnJheVxuIyBvciBsb29wIGEgZ2l2ZW4gbnVtYmVyIG9mIHRpbWVzXG4jIFRoZXkncmUgbWFya2VkIHdpdGggKClcblxuYFN0YXJ0aW5nIGZvciBsb29wYCxcblxuYEhlbGxvYFxuXG4oYXwgICAgICAgIyB8IGluc2lkZSBhIGZvciBsb29wIG1hcmtzIHRoZSBiaXQgYmVmb3JlIGFzIGEgdmFyaWFibGVcbiAgICAgICAgICAjIEVhY2ggdmFsdWUgaXRlcmF0aW5nIG92ZXIgdGhlIGxvb3Agd2lsbCBiZSBzdG9yZWQgaW4gdGhpcyB2YXJpYWJsZVxuICAgICAgICAgIFxuICDihpBhICwgICAgIyBXZSBjYW4gZ2V0IHRoZSBjdXJyZW50IHZhbHVlIG9mIGEgYW5kIHByaW50IGl0LlxuICBuLCAgICAgICMgV2UgY2FuIGFsc28gdXNlIG4sIHdoaWNoIGlzIHRoZSBjdXJyZW50IGxvb3AgdmFsdWUgYW1vbmcgb3RoZXIgdGhpbmdzLlxuKVxuXG5cbiMgV2hpbGUgbG9vcHMgbG9vcCB3aGlsZSBhIGNlcnRhaW4gY29uZGl0aW9uIGlzIHRydWVcbiMgKE9yIGZvcmV2ZXIsIGlmIG5vIGNvbmRpdGlvbiBpcyBzcGVjaWZpZWQpXG4jIFRoZXkncmUgbWFya2VkIHdpdGgge31cblxuXG41ICAgICAgICAgICMgV2UgcHVzaCA1XG5cbnsgMSAtIDogfCAgIyBBbmQgY29udGludWFsbHkgZGVjcmVtZW50IGl0IHVudGlsIGl0IGlzIGZhbHN5XG4gIDogLCAgICAgICMgUHJpbnRpbmcgaXQgYXMgd2UgZ28uXG59IiwiIiwiIl0=\n\n\n## Links\n\n- [Repository](https://github.com/Vyxal/Vyxal)\n- [Online Interpreter](http://vyxal.pythonanywhere.com)\n- [Tutorial](https://vyxapedia.hyper-neutrino.xyz/beginners)\n- [Main Chat Room (SE Chat)](https://chat.stackexchange.com/rooms/106764/vyxal)\n- [Vycord (Discord)](https://discord.gg/hER4Avd6fz)\n- [Elements](https://github.com/Vyxal/Vyxal/blob/main/documents/knowledge/elements.md)\n- [Vyxapedia](https://vyxapedia.hyper-neutrino.xyz/)\n',
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://vyxal.pythonanywhere.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
