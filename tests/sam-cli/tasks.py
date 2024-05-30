"""Invoke tasks file"""

from invoke import task
from pathlib import Path


@task
def build(ctx):
    """Build and package the assets"""
    ctx.run("sam build --base-dir . --build-dir out --template template.yaml --no-beta-features --use-container")
    assert Path("out").exists()
    assert Path("out/template.yaml").exists()
    assert Path("out/exampleLambda").exists()
    assert Path("out/exampleLambda/boto3").exists()


@task
def build_without_dind(ctx):
    """Build and package the assets"""
    ctx.run("sam build --base-dir . --build-dir out --template template.yaml --no-beta-features")
    assert Path("out").exists()
    assert Path("out/template.yaml").exists()
    assert Path("out/exampleLambda").exists()
    assert Path("out/exampleLambda/boto3").exists()
