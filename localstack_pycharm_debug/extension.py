import logging
import os

from localstack.extensions.api import Extension

LOG = logging.getLogger(__name__)


class PycharmDebugExtension(Extension):
    name = "localstack-extension-pycharm-debug"

    def on_platform_start(self):
        LOG.setLevel(level=logging.INFO)

        import pydevd_pycharm

        try:
            # localstack <2.3 compat
            from localstack.config import DOCKER_HOST_FROM_CONTAINER
            host = DOCKER_HOST_FROM_CONTAINER
        except ImportError:
            from localstack.utils.net import get_docker_host_from_container
            host = get_docker_host_from_container()

        port = int(os.getenv("PYDEVD_PYCHARM_PORT", "12345"))

        LOG.info("pydevd_pycharm.settrace('%s', %s)", host, port)
        pydevd_pycharm.settrace(
            host,
            port=port,
            stdoutToServer=True,
            stderrToServer=True,
        )
