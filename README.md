<h1 align="center">Events Portal</h1>

<h4 align='center'> Repository for the Unicode 2020-2021 DJ Events Portal project.</h4>

## File Structure

```
.
├── README.md
├── website/
│   ├── api -> Django app for API
│   ├── client -> React frontend
│   ├── core -> Django app to render frontend
│   ├── website
│   └── manage.py
├── pyproject.toml -> Black settings
├── .flake8 -> Flake8 settings
├── .pre-commit-config.yaml -> Pre-commit hook settings
└── requirements.txt
```

## Technology Stack

#### Backend

- Django 3.1.5+ (Python 3.7+)

#### Frontend

- React 17.0+

## Team

#### Developers

1. Aryan Parekh
2. Yash Jhaveri
3. Nishant Kumar
4. Saloni Patel
5. Burhan Savliwala
6. Adithya Sanyal
7. Sumedh Vichare

#### Mentors

1. Aryan Chouhan
2. Kanishk Shah
3. Deep Nanda
4. Shrey Dedhia
5. Tejas Ghone
6. Nirali Parekh

## Build Instructions

#### Backend

```bash
  # Clone the repository, create a virtual environment and install pre-commit hooks
  git clone https://github.com/chouhanaryan/ep-test.git
  cd ep-test
  python -m venv venv
  .\venv\Scripts\activate
  pip3 install -r requirements.txt
  pre-commit install

  # Set up frontend
  cd website\client
  npm run build

  # Set up backend
  cd ..
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

#### Frontend

```bash
  # Clone the repository, create a virtual environment and install pre-commit hooks
  git clone https://github.com/chouhanaryan/ep-test.git
  cd ep-test
  python -m venv venv
  .\venv\Scripts\activate
  pip3 install -r requirements.txt
  pre-commit install

  # Start a local React server for development
  cd website\client
  npm install
  npm start

  # (If backend is required)
  npm run build
  cd ..
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

## Development Instructions

We have configured a [pre-commit hook](https://githooks.com/) that runs [Black](https://black.readthedocs.io/en/stable/) and [Prettier](https://prettier.io/) and checks against [Flake8](https://flake8.pycqa.org/en/latest/) to ensure consistent code formatting and styling for Python and JavaScript files.
In case a check fails, run `git add .` and commit the files again.

To manually run the hook, run `pre-commit run --all-files`.

## LICENSE

> MIT License
>
> Copyright (c) 2021 Unicode
>
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
