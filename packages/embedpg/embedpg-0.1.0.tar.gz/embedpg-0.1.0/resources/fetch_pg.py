import tempfile
import urllib.request
from os.path import dirname, realpath
from zipfile import ZipFile

DOWNLOAD_URL = "https://repo1.maven.org/maven2/io/zonky/test/postgres/embedded-postgres-binaries-{os}-{arch}/{version}/embedded-postgres-binaries-{os}-{arch}-{version}.jar"


def fetch_pg_binary_jar(os: str, arch: str, version: str) -> str:
    with tempfile.NamedTemporaryFile() as f:
        urllib.request.urlretrieve(
            DOWNLOAD_URL.format(os=os, arch=arch, version=version),
            f.name,
        )
        with ZipFile(f.file) as z:
            z.extractall(
                dirname(realpath(__file__)),
                [name for name in z.namelist() if name.endswith(".txz")],
            )


if __name__ == "__main__":
    fetch_pg_binary_jar("darwin", "arm64v8", "14.4.0")
    fetch_pg_binary_jar("linux", "amd64", "14.4.0")
