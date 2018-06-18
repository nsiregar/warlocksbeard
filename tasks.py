from invoke import task
from sys import platform

@task
def server(ctx):
    print('Running wsgi platform')
    print('http://localhost:8000')
    ctx.run('waitress-serve --host=0.0.0.0 --port=8000 src:app')
