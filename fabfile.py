from fabric import task
from invoke import run
from patchwork.transfers import rsync

@task
def local(ctx):
    run('rm .cache demo/static/src/app.css -rf', echo=True)
    run("find . -name '__pycache__' |xargs rm -rf ", echo=True)
    run("yarn install", echo=True)
    run("yarn run build", echo=True)
    run("python manage.py collectstatic --noinput", echo=True)

@task(hosts=["zodman@go.opensrc.mx",])
def deploy(ctx):
    with ctx.prefix("source ~/.virtualenvs/inertia/bin/activate"):
        with ctx.cd("apps/django-inertia-demo"):
            ctx.run("git pull")
            ctx.run("pip install -r requirements.txt")
            ctx.run("python manage.py migrate")
            ctx.run("python populate.py")
            ctx.run("python manage.py collectstatic --noinput")
    rsync(ctx, "static/", "apps/django-inertia-demo/")
    ctx.run("sudo supervisorctl restart inertia")

