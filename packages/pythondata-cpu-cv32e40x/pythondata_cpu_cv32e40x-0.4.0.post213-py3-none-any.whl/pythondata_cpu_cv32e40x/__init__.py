import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.4.0.post213"
version_tuple = (0, 4, 0, 213)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post213")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post71"
data_version_tuple = (0, 4, 0, 71)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post71")
except ImportError:
    pass
data_git_hash = "adfd1a1fe57c919e1de0018b50b8e99a7c0a5edb"
data_git_describe = "0.4.0-71-gadfd1a1f"
data_git_msg = """\
commit adfd1a1fe57c919e1de0018b50b8e99a7c0a5edb
Merge: 2f19bac0 6fbbca6c
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Mon Jul 18 13:51:03 2022 +0200

    Merge pull request #622 from Silabs-ArjanB/ArjanB_mrv
    
    Added reset value for rvfi_mode

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn
