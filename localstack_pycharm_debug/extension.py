import logging
import os

from localstack.extensions.api import Extension

LOG = logging.getLogger(__name__)


class PycharmDebugExtension(Extension):
    name = "localstack-extension-pycharm-debug"

    def on_platform_start(self):
        LOG.setLevel(level=logging.INFO)

        import pydevd_pycharm
        from localstack.config import DOCKER_HOST_FROM_CONTAINER

        port = int(os.getenv("PYDEVD_PYCHARM_PORT", "12345"))

        LOG.info("pydevd_pycharm.settrace('%s', %s)", DOCKER_HOST_FROM_CONTAINER, port)
        pydevd_pycharm.settrace(
            DOCKER_HOST_FROM_CONTAINER,
            port=port,
            stdoutToServer=True,
            stderrToServer=True,
        )
