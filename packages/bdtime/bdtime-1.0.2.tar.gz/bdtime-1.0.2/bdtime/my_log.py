import logging
from .datetime_utils import common_date_time_formats

log_config_dc = {
    'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
    "datefmt": common_date_time_formats.s_dt,
    "level": logging.DEBUG,
}


log_level_types = list(logging._nameToLevel.keys())


def get_logger(name="logger", level="DEBUG"):
    _logger = logging.getLogger(name)
    if _logger:
        return _logger

    if level:
        logLevel = level.upper()
        assert hasattr(logging, logLevel), f'logLevel[{logLevel}]取值错误!'
        log_config_dc.update({"level": getattr(logging, logLevel)})
    logging.basicConfig(**log_config_dc)
    return _logger


def show_all_loggers():
    for name in logging.Logger.manager.loggerDict.keys():
        logger = logging.getLogger(name)
        print('name: [%s], logger: [%s]'%(name, logger))


if __name__ == '__main__':
    # log = logging.getLogger("dqn")
    # logging.basicConfig(**log_config_dc)
    # log.setLevel(logging.INFO)
    # logger = get_logger('info', 'test_logger')
    show_all_loggers()
