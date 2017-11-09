# -*- coding:utf-8 -*-
__author__ = 'IanChen'

import logging

logging.basicConfig(filename="test.log",level=logging.INFO)

logger=logging.getLogger("test.log")
logger.setLevel(logging.ERROR)
# logging.warning("bitch")
# logging.info("hha")
# logging.error("see")
# logging.critical("hello")

