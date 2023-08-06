import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.4.0.post209"
version_tuple = (0, 4, 0, 209)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post209")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post67"
data_version_tuple = (0, 4, 0, 67)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post67")
except ImportError:
    pass
data_git_hash = "86d27d7984f4075727b34177f6917bd76e6c8242"
data_git_describe = "0.4.0-67-g86d27d79"
data_git_msg = """\
commit 86d27d7984f4075727b34177f6917bd76e6c8242
Merge: fa22670c 83699c4a
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri Jul 15 08:15:04 2022 +0200

    Merge pull request #620 from Silabs-ArjanB/ArjanB_todofl
    
    Added todos related to recent PRs

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
