import requests
import xml.etree.ElementTree as ET
from setup_logging import setup_logging

log = setup_logging()
xml_cache=None

def fetch_xml(url):
    try:
        log.info(f"Fetching XML data from {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос успешен
        log.info("XML data successfully fetched.")
        return response.content
    except requests.exceptions.RequestException as e:
        log.error(f"Error fetching XML data: {e}")
        return None


def parse_xml(xml_data):
    try:
        log.info("Parsing XML data...")
        root = ET.fromstring(xml_data)

        # Создаем список для хранения данных
        currencies = []

        # Проходим по каждому элементу <Valute>
        for valute in root.findall("Valute"):
            char_code = valute.find("CharCode").text
            name = valute.find("Name").text
            value = valute.find("Value").text
            nominal = valute.find("Nominal").text

            # Добавляем данные в список
            currencies.append({
                "CharCode": char_code,
                "Name": name,
                "Nominal": nominal,
                "Value": value
            })

        log.info(f"Successfully parsed {len(currencies)} currencies.")
        global xml_cache
        xml_cache=currencies
        return currencies
    except ET.ParseError as e:
        log.error(f"Error parsing XML data: {e}")
        return None


def get_currency_value(currency_code):

    log.debug(f"Displaying currency {currency_code} data:")
    if xml_cache:
        currencies= xml_cache
        for currency in currencies:
            if currency_code in currency["CharCode"]:
                return currency['Value']
                
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    xml_data = fetch_xml(url)

    if xml_data:
        currencies = parse_xml(xml_data)

        if currencies:
            for currency in currencies:
                if currency_code in currency["CharCode"]:
                    return currency['Value']
        else:
            log.warning("No currency data available.")
    else:
        log.error("Failed to retrieve or parse XML data.")


def main():
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    xml_data = fetch_xml(url)

    if xml_data:
        currencies = parse_xml(xml_data)

        if currencies:
            log.info("Displaying currency data:")
            for currency in currencies:
                log.info(f"{currency['Name']} ({currency['CharCode']}): {currency['Nominal']} шт. = {currency['Value']} руб.")
        else:
            log.warning("No currency data available.")
    else:
        log.error("Failed to retrieve or parse XML data.")
    

if __name__ == "__main__":
    main()
