"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from proyect_machine.pipelines import data_engineering as dp

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "data_engineering": dp.create_pipeline(),
        "__default__": dp.create_pipeline(),
    }
from proyect_machine.pipelines.data_science import pipeline as data_science

def register_pipelines():
    return {
        "data_science": data_science.create_pipeline(),
        "__default__": data_science.create_pipeline(),
    }
