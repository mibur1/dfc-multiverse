"""
Pytest configuration for the comet test suite.

teneto (a test-only reference implementation used to cross-check comet's output) still imports
`from nilearn.input_data import NiftiLabelsMasker`. That module was deprecated in nilearn 0.11
and removed in 0.13+. When CI installs a fresh env against comet's `nilearn >= 0.12.1` pin, pip
resolves to nilearn 0.13/0.14 and teneto's import chain breaks at collection.

The shim below aliases `nilearn.input_data` to `nilearn.maskers` (where `NiftiLabelsMasker` now
lives) before teneto imports, so the cross-check tests keep running on any nilearn version.
Test-only; runtime is untouched.
"""
import sys

try:
    import nilearn.maskers
    sys.modules.setdefault("nilearn.input_data", nilearn.maskers)
except ImportError:
    pass
