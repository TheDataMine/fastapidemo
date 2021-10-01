# fastapidemo

## Getting started

### Running on Brown

TBD

### Running on your local machine

1. Install poetry: https://python-poetry.org/docs/#installation

2. Clone repo:

```bash
git clone git@github.com:TheDataMine/fastapidemo.git
```

3. Navigate into the project directory and install dependencies.

```bash
cd $HOME/fastapidemo
poetry install
```

4. Run the program:

```bash
poetry run uvicorn app.main:app --reload
```

5. In a browser navigate to localhost:8000 or localhost:8000/downloader