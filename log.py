import logging


def setup_logger(name, log_file, formatter, console: bool, level=logging.DEBUG):
    handler = logging.FileHandler(log_file)
    handler_formatter = logging.Formatter(formatter)
    handler.setFormatter(handler_formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(log_format)

        logger.addHandler(console_handler)
    return logger


store = setup_logger('store', 'store.log', '%(asctime)s-%(name)-10s-%(levelname)-16s-%(message)s', False)
