import logging

logger = logging.getLogger(__name__)

try:
    print(4 / 2)
    print(2 / 0)
except ZeroDivisionError:
    logger.error('Тут было исключение', exc_info=True)#Способ 1:
    # Лог вместе с трейсбэком ошибки через передачу методу логгера аргумента exc_info=True.
    logger.exception('Тут было исключение') #Способ 2:
    # Лог вместе с трейсбэком ошибки через вызов метода exception у логгера.