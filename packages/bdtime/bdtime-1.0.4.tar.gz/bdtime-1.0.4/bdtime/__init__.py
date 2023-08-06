name = "bdtime"

from .my_time import *
from .utils import *
from .my_log import log_config_dc, show_all_loggers, log


def version():
    """
    # 更新日志

    - 增加datetime和标准北京时间相关方法         # 1.0.0
    - 增加logger相关信息                        # 1.0.1
    - 更新了日期时间格式, 将分隔符'/'替换为'-'
    - 增加log_level_types                      # 1.0.2
    - 检查是否最新版本check_version
    - 修复check_version部分bug                 # 1.0.3
    - 做了部分优化                             # 1.0.4

    """
    ret = '1.0.4'
    return ret
