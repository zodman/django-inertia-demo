from fabric import task


@task
def deploy(ctx):
    with ctx.prefix("source ~/.virtualenvs/inertia/bin/activate"):
        with ctx.cd("apps/django-inertia-demo"):
            ctx.run("git pull")
            ctx.run("pip install -r requirements.txt")
            #ctx.run("npm i")
            ctx.run("npm run build")
            ctx.run("python manage.py collectstatic --noinput")
            ctx.sudo("supercvisorctl restart inertia")



