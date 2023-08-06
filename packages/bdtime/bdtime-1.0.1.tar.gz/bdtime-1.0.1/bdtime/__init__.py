name = "bdtime"


from .my_time import *
from .utils import *
from .my_log import log_config_dc, get_logger, show_all_loggers


def version():
    """
    # 更新日志

    - 增加datetime和标准北京时间相关方法         # 1.0.0
    - 增加logger相关信息                        # 1.0.1
    - 更新了日期时间格式, 将分隔符'/'替换为'-'
    """
    ret = '1.0.1'
    return ret
