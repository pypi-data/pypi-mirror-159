import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.4.0.post217"
version_tuple = (0, 4, 0, 217)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post217")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post75"
data_version_tuple = (0, 4, 0, 75)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post75")
except ImportError:
    pass
data_git_hash = "d542e41ced10c83c4389d5ae14ffc7f955dfb190"
data_git_describe = "0.4.0-75-gd542e41c"
data_git_msg = """\
commit d542e41ced10c83c4389d5ae14ffc7f955dfb190
Merge: 9ff0705c a5fa4b54
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Jul 19 08:03:29 2022 +0200

    Merge pull request #624 from Silabs-ArjanB/ArjanB_obr
    
    Removed obsolete RTL signal

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
