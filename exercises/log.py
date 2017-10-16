import logging
# https://docs.python.org/3/howto/logging.html


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(fmt)

    logger.addHandler(handler)
    return logger


def test():
    l = get_logger(__name__)
    l.debug("debug msg")
    l.info("info msg")
    l.warn("warn msg")
    try:
        1/0
    except Exception as e:
        l.error(e, exc_info=True)
    l.info("Exitting...")


if __name__ == "__main__":
    test()
