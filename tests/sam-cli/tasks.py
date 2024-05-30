"""Invoke tasks file"""

import re
from invoke import task
from pathlib import Path


def update_runtime_in_template(file_path: Path, new_runtime: str):
    with file_path.open(mode="r", encoding="utf-8") as file:
        content = file.read()

    # Use regex to replace the Runtime line
    updated_content = re.sub(r"Runtime:\s*python[0-9\.]+", f"Runtime: {new_runtime}", content)

    with file_path.open(mode="w", encoding="utf-8") as file:
        file.write(updated_content)


@task
def build(ctx, runtime):
    """Build and package the assets"""
    template_path = Path("template.yaml")
    update_runtime_in_template(template_path, f"python{runtime}")
    ctx.run("sam build --base-dir . --build-dir out --template template.yaml --no-beta-features --use-container")
    assert Path("out").exists()
    assert Path("out/template.yaml").exists()
    assert Path("out/exampleLambda").exists()
    assert not Path("out/exampleLambda/boto3").exists()
    # This fails because aws-sam-cli cannot build docker in docker, so the boto3 package is not present
    # We should not use the --use-container flag with this image


@task
def build_without_dind(ctx, runtime):
    """Build and package the assets"""
    template_path = Path("template.yaml")
    update_runtime_in_template(template_path, f"python{runtime}")
    ctx.run("sam build --base-dir . --build-dir out --template template.yaml --no-beta-features")
    assert Path("out").exists()
    assert Path("out/template.yaml").exists()
    assert Path("out/exampleLambda").exists()
    assert Path("out/exampleLambda/boto3").exists()
