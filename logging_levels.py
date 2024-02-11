import logging


logging.basicConfig(level=logging.DEBUG) #параметр level отвечает за базовую настройку уровня логирования,
# указали DEBUG - значит начиная с него будут сохраняться логи, а по умолчанию с WARNING

logging.debug('Это лог уровня DEBUG')
logging.info('Это лог уровня INFO')
logging.warning('Это лог уровня WARNING')
logging.error('Это лог уровня ERROR')
logging.critical('Это лог уровня CRITICAL')

print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)

logger = logging.getLogger(__name__)

logger.warning('Предупреждение!')
logger.debug('Отладочная информация')

print(logger)