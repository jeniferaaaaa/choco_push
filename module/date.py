import logging
from datetime import datetime

#ログレベルセット
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

##ハンドラ取得
get_handler = logging.FileHandler('log/access.log')
logger.addHandler(get_handler)


def getNowDate():
    dt_now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    logger.info(dt_now)

    return dt_now