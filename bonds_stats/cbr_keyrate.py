import zeep
from setup_logging import setup_logging

log = setup_logging()

# URL веб-сервиса
url = 'https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?WSDL'

def get_currency_data():
    try:
        # Создаем клиент SOAP
        client = zeep.Client(url)

        # Вызываем метод веб-сервиса (например, GetCursOnDate)
        #response = client.service.GetCursOnDate('2024-11-10')
        response = client.service.KeyRate('2024-10-09','2024-10-10')
         
        # Логируем успешное получение данных
        log.info("SOAP response received successfully")

        # Выводим ответ (в зависимости от структуры данных)
        log.info(f"Response: {response}")

        return response

    except Exception as e:
        log.error(f"Error occurred while fetching SOAP data: {e}")
        return None

def main():
    currency_data = get_currency_data()

    if currency_data:
        log.info("Currency data retrieved successfully.")
        # Обработка и вывод данных
        for item in currency_data:
            print(item)
            #log.info(f"Currency: {item} Data: {currency_data[item]}")
    else:
        log.error("Failed to retrieve currency data.")

if __name__ == "__main__":
    main()