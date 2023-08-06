import os
import logging

import h2o_experiment_tracking.tracking.client

logger = logging.getLogger(__name__)

# Build defaults
build_info = {
    "git_commit": "",
    "git_commit_timestamp": "",
    "git_describe": "",
    "build_os": "",
    "build_machine": "",
    "build_date": "",
    "build_user": "",
    "version": "0.0.0",
}

try:
    with open(
        os.path.join(
            os.path.dirname(h2o_experiment_tracking.__file__), "BUILD_INFO.txt"
        )
    ) as f:
        exec(f.read(), build_info)
except Exception as e:
    logger.debug(e)

__version__ = build_info["version"]
__build_info__ = build_info

init = h2o_experiment_tracking.tracking.client.init
start = h2o_experiment_tracking.tracking.client.start
end = h2o_experiment_tracking.tracking.client.end
log_param = h2o_experiment_tracking.tracking.client.log_param
log_params = h2o_experiment_tracking.tracking.client.log_params
log_metric = h2o_experiment_tracking.tracking.client.log_metric
log_metrics = h2o_experiment_tracking.tracking.client.log_metrics
log_artifact = h2o_experiment_tracking.tracking.client.log_artifact
log_artifacts = h2o_experiment_tracking.tracking.client.log_artifacts
get_iteration = h2o_experiment_tracking.tracking.client.get_iteration_by_id

__all__ = [
    "init",
    "start",
    "end",
    "log_param",
    "log_params",
    "log_metric",
    "log_metrics",
    "log_artifact",
    "log_artifacts",
    "__version__",
    "__build_info__",
]
