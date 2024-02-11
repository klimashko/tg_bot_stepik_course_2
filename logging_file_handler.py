#Хэндлер для записи логов в файл.

import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('logs.log')

logger.addHandler(file_handler)

print(logger.handlers)

logger.warning('Это лог с предупреждением!')
#Выполнив этот код, получаем результат в консоли:
#[<FileHandler /<здесь_полный_путь_до_файла_с_логами>/logs.log (NOTSET)>]
#А в файле logs.txt: Это лог с предупреждением!