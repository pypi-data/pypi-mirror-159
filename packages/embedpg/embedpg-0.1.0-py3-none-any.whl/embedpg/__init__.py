from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
from embedpg.core import EmbedPg

__all__ = (
    "EmbedPg"
)
