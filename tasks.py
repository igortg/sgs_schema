from invoke import tasks
import fdb



@tasks
def install(ctx):
    ctx.run("isql")
