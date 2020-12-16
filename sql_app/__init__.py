# this is just an empty file, but it tells Python Python that sql_app with all its modules (Python files) is a package.
# if you want to work with virtualenv, you need to initially follow the steps outlined in
# https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
# to create a virtualenv, navigate to the project directory and put "python3 -m venv env" in cmd,
# effectively creating a folder "env" containing the environment that can be activated using
# "source env/bin/activate", you can "pip install" packages into that. "pip freeze > requirements.txt"
# creates and stores a list of all packages and their dependencies into the project folder.
# "uvicorn main:app" starts up the server, specifically looking for file named "main" and object "app"
# in it. It can be reached under "http://127.0.0.1:8000" and its OpenAPI description under "/docs".