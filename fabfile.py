from fabric import task


@task
def deploy(ctx):
    with ctx.prefix("source ~/.virtualenvs/inertia/bin/bash") and \
            ctx.cd("apps/django-inertia-demo"):
        ctx.run("pip install -r requirements.txt")
        ctx.run("git pull")



