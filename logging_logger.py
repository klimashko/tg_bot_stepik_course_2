import logging


logger = logging.getLogger(__name__)

logger.warning('Предупреждение!')
logger.debug('Отладочная информация')

print(logger)