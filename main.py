import logger_manager as Log


if __name__ == "__main__":
    import time
    from datetime import datetime

    logger_manager =  Log.LoggerManager(name="1")
    logger_manager.disable_internal_logging()
    logger_manager.enable_internal_logging()
    # Установим форматы для файлового логирования
    # logger_manager.set_file_format("%(asctime)s - !DEBUG!: %(message)s (%(filename)s:%(lineno)d)")
    # logger_manager.set_file_level_format('INFO',"%(asctime)s - !INFO!: %(message)s")
    # logger_manager.set_console_format("%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s") # Задать свой формат
    # logger_manager.set_console_level_format('INFO',"%(levelname)s") # Задать свой формат
    # logger_manager.set_console_color( 'DEBUG', 'blue')  # Задать цвет из доступных

    logger_manager.set_file_handler_params(max_bytes = 2048*1024, backup_count = 10) # Максимальный размер файла и количество ротируемых файлов
    logger_manager.enable_console_logging() # Включение логирования в консоль
    logger_manager.disable_console_logging() # Отключение логирования в консоль
    logger_manager.disable_logging()  # Отключение логирования
    logger_manager.enable_logging()   # Включение логирования
    #logger_manager.set_level('INFO')  # Установка уровня логирования на INFO
    logger_manager.set_filter_list(['DEBUG' ,'WARNING', 'ERROR' ]) # Установка списка фильтров для логирования
     # Установка списка фильтров для логирования
    # logger_manager.set_filter('INFO')  # Фильтрация сообщений только уровня INFO
    logger_manager.clear_filter()  # Очистка установленного фильтра
    #logger_manager.reset_level()  # Сброс уровня логирования до уровня DEBUG
    logger_manager.set_name("NewNameLogger")  # Установка нового имени логгера
    logger_manager.disable_file_logging()
    with logger_manager.time_execution():
        for i in range(2):
            # Включение и отключение логирования в файл
            logger_manager.enable_file_logging(f"{datetime.now().strftime('%Y-%m-%d %H-%M')}-{i}.log")
            logger_manager.set_file_filter_list(['DEBUG', 'WARNING', 'ERROR'])
            # logger_manager.disable_file_logging()

            # Логирование сообщений
            logger = logger_manager.logger
            logger.debug(f"debug message {i}")
            logger.info(f"info message {i}")
            logger.warning(f"warning message {i}")
            logger.error(f"error message {i}")
            logger.critical(f"critical message {i}")
            time.sleep(1)
