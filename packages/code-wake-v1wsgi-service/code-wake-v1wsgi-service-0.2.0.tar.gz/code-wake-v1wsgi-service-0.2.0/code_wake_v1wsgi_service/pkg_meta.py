"""Package meta data."""

import sys
from typing import Any, Dict

name = "code-wake-v1wsgi-service"
version = "0.2.0"
author = "Michael Wright"
author_email = "mjw@methodanalysis.com"
description = "Code Wake V1 WSGI Werkzeug middleware"
url = "https://github.com/mwri/pycodewake-v1wsgi-service"

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

entry_points: Dict[str, Any] = {
    "console_scripts": [],
}

python_requires = ">=3.6"
install_requires = [
    "bencode.py~=4.0.0",
    "code-wake~=0.2.0",
    "werkzeug~=2.1.2",
]

extras_require = {
    "dev": [
        "pytest==7.0.1",
        "coverage==6.2",
        "black==22.3.0",
        "isort==5.10.1",
        "mypy==0.961",
        "types-requests==2.28.0",
        "code-wake-sql14-store==0.2.0",
        "code-wake-v1rest-store==0.2.0",
        "flask==2.1.2",
    ],
}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        attr_names = sys.argv[1:]
        attr_val = getattr(sys.modules[__name__], attr_names.pop(0))

        def display_val(val):
            if type(attr_val) == str:
                print(val)
            elif type(val) == list:
                for sub_val in val:
                    print(sub_val)
            elif type(val) == dict:
                print(repr(val))

        if type(attr_val) in (str, list):
            display_val(attr_val)
        elif type(attr_val) == dict:
            while len(attr_names) > 0 and type(attr_val) == dict:
                attr_val = attr_val[attr_names.pop(0)]
            display_val(attr_val)
