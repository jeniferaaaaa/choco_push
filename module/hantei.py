import logging
import datetime

#判定モジュール

#変数セット
a_shift_start = '08:30:00'
a_shift_end = '08:59:00'
b_shift_start = '09:30:00'
b_shift_end = '09:59:00'

#ログレベルセット
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

##ハンドラ取得
get_handler = logging.FileHandler('log/error.log')
logger.addHandler(get_handler)


def judgeTime(nowDate):
    #日付と時刻に分解
    new_date, new_time = nowDate.split()
    #「8:30~8:59」「09:30~9:59」の間であるかどうか判定
    if not (a_shift_start <= new_time <= a_shift_end or b_shift_start <= new_time <= b_shift_end):
        aa = '起動時間外です。起動時刻：'
        logger.info(aa + new_date + new_time)
        return False

    return True