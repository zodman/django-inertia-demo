from fabric import task


@task
def deploy(ctx):
    with ctx.prefix("source ~/.virtualenvs/inertia/bin/activate"):
        with ctx.cd("apps/django-inertia-demo"):
            ctx.run("git pull")
            ctx.run("pip install -r requirements.txt")
            ctx.run("python manage.py migrate")
            ctx.run("python populate.py")
            ctx.run("python manage.py collectstatic --noinput")
    ctx.run("sudo supervisorctl restart inertia")



