from invoke import task
from sys import platform

@task
def server(ctx):
    print('Running wsgi platform')
    print('http://localhost:8000')
    if platform == 'linux' or platform == 'linux2':
        ctx.run('gunicorn --bind 0.0.0.0:8000  src:app', pty=True)
    if platform == 'win32':
        ctx.run('waitress-serve --host=0.0.0.0 --port=8000 src:app', pty=True)

@task
def cleanup(ctx):
    print('Clean up *.pyc files')
    ctx.run()
