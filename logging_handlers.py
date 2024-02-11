#Хэндлеры для вывода логов в stderr и stdout.

import logging
import sys

logger = logging.getLogger(__name__) #Создает объект логгера с именем текущего модуля (переданное имя __name__)

stderr_handler = logging.StreamHandler() #Создает хэндлер для вывода логов в стандартный поток ошибок (stderr)
stdout_handler = logging.StreamHandler(sys.stdout) #Создает хэндлер для вывода логов в стандартный поток вывода (stdout),
# явно указывая sys.stdout в качестве потока.

logger.addHandler(stderr_handler) #Добавляет stderr_handler в логгер. Теперь логи будут направляться и в стандартный поток ошибок
logger.addHandler(stdout_handler) #Добавляет stdout_handler в логгер. Теперь логи будут направляться и в стандартный поток вывода


print(logger.handlers) #Выводит список всех хэндлеров, прикрепленных к логгеру

logger.warning('Это лог с предупреждением!') #Выводит предупреждение, используя метод warning объекта логгера.
# Этот лог будет направлен как в stdout, так и в stderr

#Уровень хэндлеров по умолчанию NOTSET, а значит, они будут обрабатывать логи любого уровня.
# Если задать хэндлерам какой-то другой уровень, например, INFO, то обрабатывать они будут только логи,
# начиная с этого уровня (INFO, WARNING, ERROR и CRITICAL)

