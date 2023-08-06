import logging
import os
import tarfile
import tempfile
from os.path import dirname, realpath
from subprocess import Popen

logger = logging.getLogger("embedpg")

OS = "linux"
match os.uname().sysname:
    case "Darwin":
        OS = "darwin"
logger.debug("OS: %s", OS)

ARCH = "x86_64"
match os.uname().machine:
    case "arm64":
        ARCH = "arm_64"
logger.debug("ARCH: %s", ARCH)


class EmbedPg(object):
    def __init__(self, user: str = "postgres", port: int = 5432):
        self.user = user
        self.port = port

        self.pghome = tempfile.mkdtemp(prefix="embedpg-")
        with tarfile.open(
                os.path.join(
                    dirname(realpath(__file__)),
                    "resources",
                    "postgres-{os}-{arch}.txz".format(os=OS, arch=ARCH)
                ), "r:xz") as tf:
            tf.extractall(path=self.pghome)
        logger.info("Postgres home: %s", self.pghome)

        self.datadir = tempfile.mkdtemp(prefix="embedpg-datadir-")
        os.system(" ".join([
            os.path.join(self.pghome, "bin", "initdb"),
            "-D", self.datadir,
            "-U", self.user,
        ]))
        logger.info("Postgres data dir: %s", self.datadir)

        self.pgproc = Popen([
            os.path.join(self.pghome, "bin", "postgres"),
            "-D", self.datadir,
            "-p", str(self.port),
        ])
        logger.info("Postgres listen on port %s", self.port)

    def shutdown(self):
        try:
            self.pgproc.kill()
            os.waitpid(self.pgproc.pid, 0)
            logger.info("Postgres process shutdown gracefully")
        finally:
            pass

    def __enter__(self):
        return self

    def __exit__(self):
        self.shutdown()
