# ECLI_Reference

**Overzicht**
Deze Python-script haalt rechterlijke uitspraken op en formatteert deze in een gestandaardiseerde referentievorm. Het script communiceert met de openbare API van data.rechtspraak.nl om informatie te verkrijgen op basis van het European Case Law Identifier (ECLI) nummer.

**Vereisten**
Python 3.x
requests library (installeren via pip install requests)

**Gebruik**
Start het script.
Voer ECLI-nummers in, gescheiden door komma's, wanneer daarom wordt gevraagd.
Om het programma te verlaten, typ exit.
Het script zal vervolgens de informatie voor elke ECLI opvragen, verwerken en de gestandaardiseerde referenties weergeven.

**Functies**
get_juridical_decision_reference(ecli)
Deze functie communiceert met de data.rechtspraak.nl API om gegevens over een rechterlijke uitspraak te verkrijgen op basis van een ECLI-nummer. Het verwerkt de XML-respons om de volgende informatie te extraheren en te formatteren:

Naam van de rechterlijke instantie (met specifieke afkortingen voor Nederlandse gerechtshoven)
Datum van de uitspraak, geformatteerd in het Nederlands
De ECLI-referentie zelf
main() 
Dit is de hoofdfunctie van het script. 
Het vraagt de gebruiker om ECLI-nummers.
Roept get_juridical_decision_reference aan voor elk ingevoerd ECLI-nummer.
Print de gecombineerde referenties.

**Foutafhandeling**
De get_juridical_decision_reference functie controleert de HTTP-statuscode van de API-respons. Als deze geen 200 (OK) is, retourneert de functie een foutmelding met de statuscode.

**Lokalisatie**
Het script gebruikt locale.setlocale(locale.LC_TIME, 'nl_NL') om datums in het Nederlands te formatteren. Dit vereist dat de Nederlandse locale geïnstalleerd is op het systeem waar het script wordt uitgevoerd.

**Beperkingen**
Het script is specifiek ontworpen voor de Nederlandse rechtspraak.
Het vereist een internetverbinding om met de API te communiceren.
Locale-instellingen zijn afhankelijk van het besturingssysteem.
