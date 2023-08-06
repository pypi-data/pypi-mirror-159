import datetime


BAD_END_DATE = datetime.datetime(1970, 1, 1)


def is_relevant(request: dict) -> bool:
    """
    Функция для проверки запроса от регулирующей организации.

    Проверяются следующие критерии:
    1) Дата окончания запроса отличается от 01.01.1970;
    2) Статус запроса отличается от "Отменен" (CNCL).

    :param request: Запрос от регулирующей организации, который  необходимо проверить;
    :return: True значит этот запрос соответствует критериям, False - нет.
    """
    end_date = request['enddate']
    status = request['request_status']

    print('test')

    return end_date and end_date > BAD_END_DATE and status != 'CNCL'
