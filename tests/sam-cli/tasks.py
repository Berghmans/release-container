"""Invoke tasks file"""

from invoke import task
from pathlib import Path


@task
def build(ctx):
    """Build and package the assets"""
    ctx.run("sam build --config-file samconfig.toml")
    assert Path("out").exists()
    assert Path("out/template.yaml").exists()
    assert Path("out/exampleLambda").exists()
    assert Path("out/exampleLambda/boto3").exists()
