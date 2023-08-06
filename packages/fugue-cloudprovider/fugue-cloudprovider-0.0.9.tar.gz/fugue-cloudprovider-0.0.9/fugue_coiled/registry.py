from typing import Any

from coiled import Cluster
from dask.distributed import Client, get_client
from fugue import parse_execution_engine
from fugue_dask import DaskExecutionEngine
from triad import assert_or_throw


# TODO: remove after Fugue is fully moved to conditional_dispatcher
def register() -> None:
    pass


@parse_execution_engine.candidate(
    matcher=lambda engine, conf, **kwargs: isinstance(engine, str)
    and (engine == "coiled" or engine.startswith("coiled:"))
)
def _parse_coiled(engine: str, conf: Any, **kwargs) -> DaskExecutionEngine:
    p = engine.split(":", 1)
    if len(p) == 1:
        client = get_client()
        assert_or_throw(
            isinstance(client.cluster, Cluster),
            ValueError("the current Dask client is not a Coiled client"),
        )
        return DaskExecutionEngine(conf=conf, dask_client=client)
    else:  # coiled:<clustername>
        cluster = Cluster(name=p[1])
        client = Client(cluster)
        return DaskExecutionEngine(conf=conf, dask_client=client)


@parse_execution_engine.candidate(
    matcher=lambda engine, conf, **kwargs: isinstance(engine, Cluster)
)
def _parse_coiled_cluster(engine: Cluster, conf: Any, **kwargs) -> DaskExecutionEngine:
    return DaskExecutionEngine(conf=conf, dask_client=Client(engine))
