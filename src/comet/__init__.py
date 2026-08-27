# Ignore some warnings
import warnings
warnings.filterwarnings("ignore", message=r".*invalid escape sequence '\\<'", 
                        category=SyntaxWarning)
warnings.filterwarnings("ignore", message=r"invalid value encountered in divide",
                        category=RuntimeWarning, module=r".*bct\.algorithms\.centrality")
warnings.filterwarnings( "ignore", message=r'.*"is not" with \'tuple\' literal.*', 
                        category=SyntaxWarning)
warnings.filterwarnings("ignore", message=r"Starting a Matplotlib GUI outside of the main thread",
                        category=UserWarning)

# Lazy loading of submodule imports, deferred until first use (PEP 562)
import importlib
from typing import TYPE_CHECKING

__all__ = ["connectivity", "multiverse", "graph", "network", "utils", "cifti", "bids"]

if TYPE_CHECKING:
    # Import eagerly for type checkers and IDE completion
    from . import connectivity, multiverse, graph, network, utils, cifti, bids

def __getattr__(name):
    """Import a submodule on first access and cache it in the package namespace."""
    if name in __all__:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(set(globals()) | set(__all__))

# GUI launch function
def launch_gui(*args, **kwargs):
    from .gui import run
    return run(*args, **kwargs)
