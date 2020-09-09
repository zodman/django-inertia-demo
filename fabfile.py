from fabric import task
from invoke import run
from patchwork.transfers import rsync

@task
def deploy(ctx):
    run("yarn install", echo=True)
    run("yarn run build", echo=True)
    run("python manage.py collectstatic --noinput", echo=True)
    run("find . -name '__pycache__' |xargs rm -rf ", echo=True)
    rsync(ctx, "static/", "apps/django-inertia-demo/")

    with ctx.prefix("source ~/.virtualenvs/inertia/bin/activate"):
        with ctx.cd("apps/django-inertia-demo"):
            ctx.run("git pull")
            ctx.run("pip install -r requirements.txt")
            ctx.run("python manage.py migrate")
            ctx.run("python populate.py")
            ctx.run("python manage.py collectstatic --noinput")
    ctx.run("sudo supervisorctl restart inertia")

