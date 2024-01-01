import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import locale

def get_juridical_decision_reference(ecli):
    base_url = "https://data.rechtspraak.nl/uitspraken/content"
    params = {'id': ecli}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Definieer de namespaces die gebruikt worden in de XML
        namespaces = {
            'dcterms': 'http://purl.org/dc/terms/',
            'rdfs': 'http://www.w3.org/2000/01/rdf-schema#'
        }

        root = ET.fromstring(response.content)

        # Zoek de rechterlijke instantie en vervang 'Rechtbank' met 'Rb.' en 'Gerechtshof Amsterdam' met 'OK'
        court_element = root.find(".//dcterms:creator[@rdfs:label='Instantie']", namespaces)
        if court_element is not None:
            court_name = court_element.text.replace("Rechtbank", "Rb.")
            court_name = court_name.replace("Gerechtshof Amsterdam", "OK")
            court_name = court_name.replace('Gerechtshof', 'Hof')
        else:
            court_name = 'Onbekend'

        # Zoek en formatteer de datum van de uitspraak
        date_element = root.find(".//dcterms:date[@rdfs:label='Uitspraakdatum']", namespaces)
        if date_element is not None:
            date_str = date_element.text
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')

            # Stel de locale in op Nederlands
            locale.setlocale(locale.LC_TIME, 'nl_NL')
            formatted_date = date_obj.strftime('%d %B %Y')
        else:
            formatted_date = 'Onbekende datum'

        # Formatteer de referentie
        return f"{court_name} {formatted_date}, {ecli}"
    else:
        return f"Error: {response.status_code}"

def main():
    while True:  # Start een oneindige loop
        # Vraag de gebruiker om ECLI-nummers, gescheiden door komma's
        ecli_input = input("Voer ECLI-nummers in, gescheiden door komma's (of type 'exit' om te stoppen): ")

        # Controleer of de gebruiker wil stoppen
        if ecli_input.lower() == 'exit':
            break

        ecli_list = ecli_input.split(',')

        # Verwerk elk ECLI-nummer en verzamel de referenties
        references = []
        for ecli in ecli_list:
            ecli = ecli.strip()  # Verwijder onnodige spaties
            reference = get_juridical_decision_reference(ecli)
            references.append(reference)

        # Combineer alle referenties in één string, gescheiden door komma's
        combined_references = ', '.join(references)
        print(combined_references)

# Voer het hoofdprogramma uit
main()
