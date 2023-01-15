import datetime
from modules import goodDayFlag, goodDayUptime

def sayOnTime(object, gntime, gmtime):
        
        # from modules import goodDayFlag, goodDayUptime
        
        global goodDayFlag, goodDayUptime
        
        date_time = datetime.datetime.now().time().strftime('%H%M')
        # print(date_time)
        if date_time == gntime and goodDayFlag:
            object.answer(550581505, 'Спокойной ночи, хозяин')
            goodDayUptime = int(date_time) + 1
            goodDayFlag = not goodDayFlag
            
        if date_time == gmtime and goodDayFlag:
            object.answer(550581505, 'Доброе утро, хозяин. Нас ждёт чудесный день!')
            goodDayUptime = int(date_time) + 1
            goodDayFlag = not goodDayFlag
            
        if goodDayUptime % 100 == 60:
                goodDayUptime = (goodDayUptime // 100 + 1) * 100
            
        if int(date_time) == goodDayUptime:
            goodDayFlag = not goodDayFlag
            
        # modules.goodDayFlag = goodDayFlag
        # modules.goodDayUptime = goodDayUptime
