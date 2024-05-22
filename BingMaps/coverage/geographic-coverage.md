---
title: Bing Maps Geographic Coverage
titleSuffix: Microsoft Bing Maps
description: Description of Bing Maps Geographic Coverage
ms.date: 02/03/2022
ms.topic: article
ms.assetid: 1b4ad52b-0b4a-42ba-9a37-d43cca4854d0
author: eriklindeman
ms.author: eriklind
ms.service: bing-maps
---

# Bing Maps Geographic Coverage

[!INCLUDE [bing-maps-enterprise-service-retirement](../includes/bing-maps-enterprise-service-retirement.md)]

Bing Maps contains different levels of geographic coverage for every country/region in the world. The following table contains details about coverage for

- Road Data / Routing (Driving and Walking)
- Traffic
- Truck Routing
- Geocoding
  
## Road Data / Routing (Driving and Walking)  
  
- **Good** - The country/region has detailed road data available in most populated centers and most of these have been verified for accuracy.  Coverage is updated frequently. Remote areas may lack some road information.  
  
- **Fair** - At a minimum, the country/region has major road data available as well as some detailed road data. Most often, these roads have not been verified for accuracy. Coverage is updated over time. Please visit the map to assess if the current version meets the needs of your application.  
  
- **Major Roads Only** - At a minimum, the country/region coverage includes major roads.  These roads have not been verified for accuracy. Coverage is updated over time. Please visit the map to assess if the current version meets the needs of your application.  

## Traffic

Bing Maps APIs provide traffic coverage for the countries/regions indicated in the coverage table. Traffic flow can be illustrated by lines of color representing different levels of traffic congestion that display on a Bing map. Traffic flow is can also used by the routing APIs. Traffic incidents are reports of traffic issues, such as the report of an accident. Traffic incidents are provided by APIs such as the [Bing Maps Traffic API](../rest-services/traffic/index.md) and [Bing Maps V8 Web Control Traffic Module](../v8-web-control/modules/traffic-module/index.md). Traffic incident text is provided in the primary language of the country/region where the incident occurs.  

## Truck Routing

The Bing Maps Truck Routing API provides travel routes which take truck attributes such as size, weight and type of cargo. This is important as not all trucks can travel the same routes as other vehicles. Here are some examples:

- Bridges have heights and weight limits.
- Tunnels often have restrictions on flammable or hazardous materials.
- Longer trucks have difficulty making tight turns.
- Highways often have a separate speed limit for trucks.
- Certain trucks may want to avoid roads that have steep gradients.

Bing Maps supports truck routing in the countries/regions indicated in the table below.

> [!NOTE]
> Not all truck restrictions may be supported or apply to all countries/regions.

## Geocoding  
  
- **Rooftop** – Most addresses are resolved to the latitude/longitude coordinate at the center of the address parcel (property boundary). Rooftop has the highest level of accuracy support. Its coverage varies by country/region.  
  
- **Address** – Addresses are interpolated to a latitude/longitude coordinate on the street.  
  
- **Street Name** – Addresses are resolved to the latitude/longitude coordinate of the street that contains the address. The address number is not processed.  
  
- **Basic** - Geocoding support is limited and primarily only accurate to the city level. If an address is valid, Bing Maps attempts to resolve it, but a result is not guaranteed.  
  
> [!NOTE]
> The ability to geocode in a country/region is dependent upon the road data coverage and the geocoding precision of the geocoding service. For example, a country/region may have 'Address' geocoding precision, but if there is 'Fair' road data coverage, you can only geocode addresses on the available streets and roads. Typically, geocoding precision also applies to reverse-geocoding.  

## Country/Region Coverage Table

| Country/Region                             | Road Data / Routing | Traffic | Truck Routing | Geocoding   |
|--------------------------------------------|---------------------|---------|---------------|-------------|
| Afghanistan                                | Major Roads Only    |         |               | Street Name |
| Albania                                    | Good                |         |       x       | Street Name |
| Algeria                                    | Good                |         |               | Street Name |
| American Samoa                             | Good                |         |               | Street Name |
| Andorra                                    | Good                |    x    |       x       | Rooftop     |
| Angola                                     | Good                |         |               | Street Name |
| Anguilla                                   | Good                |         |               | Basic       |
| Antarctica                                 | Major Roads Only    |         |               | Basic       |
| Antigua & Barbuda                          | Good                |         |               | Street Name |
| Argentina                                  | Good                |    x    |       x       | Rooftop     |
| Armenia                                    | Good                |         |               | Rooftop     |
| Aruba                                      | Good                |         |               | Street Name |
| Australia                                  | Good                |    x    |       x       | Rooftop     |
| Austria                                    | Good                |    x    |       x       | Rooftop     |
| Azerbaijan                                 | Good                |         |               | Rooftop     |
| Bahamas                                    | Good                |         |               | Street Name |
| Bahrain                                    | Good                |    x    |               | Rooftop     |
| Bangladesh                                 | Major Roads Only    |         |               | Street Name |
| Barbados                                   | Good                |         |               | Street Name |
| Belarus                                    | Good                |         |               | Rooftop     |
| Belgium                                    | Good                |    x    |       x       | Rooftop     |
| Belize                                     | Good                |         |               | Basic       |
| Benin                                      | Fair                |         |               | Street Name |
| Bermuda                                    | Good                |         |               | Street Name |
| Bhutan                                     | Major Roads Only    |         |               | Basic       |
| Bolivia                                    | Good                |         |               | Street Name |
| Bonaire                                    | Good                |         |               | Street Name |
| Bosnia & Herzegovina                       | Good                |         |       x       | Rooftop     |
| Botswana                                   | Good                |         |               | Street Name |
| Bouvet Island                              | Major Roads Only    |         |               | Basic       |
| Brazil                                     | Good                |    x    |       x       | Rooftop     |
| British Indian Ocean Territory             | Major Roads Only    |         |               | Basic       |
| British Virgin Islands                     | Good                |         |               | Basic       |
| Brunei                                     | Good                |    x    |               | Rooftop     |
| Bulgaria                                   | Good                |    x    |       x       | Rooftop     |
| Burkina Faso                               | Fair                |         |               | Street Name |
| Burundi                                    | Good                |         |               | Street Name |
| Cabo Verde                                 | Good                |         |               | Street Name |
| Cambodia                                   | Good                |         |               | Street Name |
| Cameroon                                   | Fair                |         |               | Street Name |
| Canada                                     | Good                |    x    |       x       | Rooftop     |
| Cayman Islands                             | Good                |         |               | Street Name |
| Central African Republic                   | Major Roads Only    |         |               | Street Name |
| Chad                                       | Major Roads Only    |         |               | Street Name |
| Chile                                      | Good                |    x    |               | Rooftop     |
| China                                      | Good                |    x    |               | Address     |
| Christmas Island                           | Good                |         |               | Rooftop     |
| Cocos (Keeling) Islands                    | Major Roads Only    |         |               | Basic       |
| Colombia                                   | Good                |    x    |               | Rooftop     |
| Comoros                                    | Major Roads Only    |         |               | Street Name |
| Congo                                      | Fair                |         |               | Street Name |
| Congo (DRC)                                | Fair                |         |               | Street Name |
| Cook Islands                               | Major Roads Only    |         |               | Street Name |
| Costa Rica                                 | Good                |         |               | Street Name |
| Côte d’Ivoire                              | Fair                |         |               | Street Name |
| Croatia                                    | Good                |    x    |       x       | Rooftop     |
| Cuba                                       | Good                |         |               | Street Name |
| Curaçao                                    | Good                |         |               | Street Name |
| Cyprus                                     | Good                |         |       x       | Address     |
| Czech Republic                             | Good                |    x    |       x       | Rooftop     |
| Denmark                                    | Good                |    x    |       x       | Rooftop     |
| Djibouti                                   | Major Roads Only    |         |               | Street Name |
| Dominica                                   | Good                |         |               | Street Name |
| Dominican Republic                         | Good                |         |               | Street Name |
| Ecuador                                    | Good                |         |               | Street Name |
| Egypt                                      | Good                |    x    |               | Rooftop     |
| El Salvador                                | Good                |         |               | Street Name |
| Equatorial Guinea                          | Major Roads Only    |         |               | Basic       |
| Eritrea                                    | Major Roads Only    |         |               | Street Name |
| Estonia                                    | Good                |    x    |       x       | Rooftop     |
| Eswatini                                   | Good                |         |               | Street Name |
| Ethiopia                                   | Major Roads Only    |         |               | Street Name |
| Falkland Islands                           | Major Roads Only    |         |               | Street Name |
| Faroe Islands                              | Good                |         |               | Rooftop     |
| Fiji                                       | Good                |         |               | Basic       |
| Finland                                    | Good                |    x    |       x       | Rooftop     |
| France                                     | Good                |    x    |       x       | Rooftop     |
| French Guiana                              | Good                |         |               | Street Name |
| French Polynesia                           | Major Roads Only    |         |               | Street Name |
| French Southern Territories                | Major Roads Only    |         |               | Basic       |
| Gabon                                      | Fair                |         |               | Street Name |
| Gambia                                     | Fair                |         |               | Street Name |
| Georgia                                    | Good                |         |               | Rooftop     |
| Germany                                    | Good                |    x    |       x       | Rooftop     |
| Ghana                                      | Good                |         |               | Street Name |
| Gibraltar                                  | Good                |    x    |       x       | Address     |
| Greece                                     | Good                |    x    |       x       | Rooftop     |
| Greenland                                  | Major Roads Only    |         |               | Street Name |
| Grenada                                    | Good                |         |               | Street Name |
| Guadeloupe                                 | Good                |         |               | Address     |
| Guam                                       | Good                |         |               | Rooftop     |
| Guatemala                                  | Good                |         |               | Street Name |
| Guernsey                                   | Good                |    x    |               | Address     |
| Guinea                                     | Major Roads Only    |         |               | Street Name |
| Guinea-Bissau                              | Major Roads Only    |         |               | Street Name |
| Guyana                                     | Good                |         |               | Street Name |
| Haiti                                      | Good                |         |               | Street Name |
| Heard Island & McDonald Islands            | Major Roads Only    |         |               | Basic       |
| Honduras                                   | Good                |         |               | Street Name |
| Hong Kong SAR                              | Good                |    x    |               | Rooftop     |
| Hungary                                    | Good                |    x    |       x       | Rooftop     |
| Iceland                                    | Good                |    x    |               | Rooftop     |
| India                                      | Good                |    x    |               | Rooftop     |
| Indonesia                                  | Good                |    x    |       x       | Rooftop     |
| Iran                                       | Major Roads Only    |         |               | Basic       |
| Iraq                                       | Good                |         |               | Street Name |
| Ireland                                    | Good                |    x    |       x       | Rooftop     |
| Isle of Man                                | Good                |    x    |               | Address     |
| Israel                                     | Good                |         |       x       | Rooftop     |
| Italy                                      | Good                |    x    |       x       | Rooftop     |
| Jamaica                                    | Good                |         |               | Street Name |
| Jan Mayen                                  | Good                |         |               | Street Name |
| Japan                                      | Good                |    x    |               | Rooftop     |
| Jersey                                     | Good                |    x    |               | Address     |
| Jordan                                     | Good                |         |               | Rooftop     |
| Kazakhstan                                 | Good                |         |               | Rooftop     |
| Kenya                                      | Good                |    x    |               | Street Name |
| Kiribati                                   | Major Roads Only    |         |               | Street Name |
| Korea                                      | Good                |    x    |               | Address     |
| Kosovo                                     | Good                |         |               | Street Name |
| Kuwait                                     | Good                |    x    |               | Rooftop     |
| Kyrgyzstan                                 | Major Roads Only    |         |               | Street Name |
| Laos                                       | Good                |         |               | Basic       |
| Latvia                                     | Good                |    x    |       x       | Address     |
| Lebanon                                    | Good                |         |               | Rooftop     |
| Lesotho                                    | Good                |    x    |               | Street Name |
| Liberia                                    | Major Roads Only    |         |               | Street Name |
| Libya                                      | Major Roads Only    |         |               | Street Name |
| Liechtenstein                              | Good                |    x    |       x       | Rooftop     |
| Lithuania                                  | Good                |    x    |       x       | Rooftop     |
| Luxembourg                                 | Good                |    x    |       x       | Rooftop     |
| Macao SAR                                  | Good                |         |               | Rooftop     |
| Madagascar                                 | Major Roads Only    |         |               | Street Name |
| Malawi                                     | Good                |         |               | Street Name |
| Malaysia                                   | Good                |    x    |       x       | Rooftop     |
| Maldives                                   | Major Roads Only    |         |               | Basic       |
| Mali                                       | Fair                |         |               | Street Name |
| Malta                                      | Good                |    x    |       x       | Address     |
| Marshall Islands                           | Major Roads Only    |         |               | Basic       |
| Martinique                                 | Good                |         |               | Address     |
| Mauritania                                 | Fair                |         |               | Street Name |
| Mauritius                                  | Good                |         |               | Street Name |
| Mayotte                                    | Good                |         |               | Street Name |
| Mexico                                     | Good                |    x    |       x       | Rooftop     |
| Micronesia                                 | Major Roads Only    |         |               | Basic       |
| Moldova                                    | Good                |         |               | Rooftop     |
| Monaco                                     | Good                |    x    |       x       | Address     |
| Mongolia                                   | Major Roads Only    |         |               | Street Name |
| Montenegro                                 | Good                |         |       x       | Address     |
| Montserrat                                 | Good                |         |               | Basic       |
| Morocco                                    | Good                |    x    |               | Rooftop     |
| Mozambique                                 | Good                |    x    |               | Street Name |
| Myanmar                                    | Good                |         |               | Basic       |
| Namibia                                    | Good                |         |               | Address     |
| Nauru                                      | Major Roads Only    |         |               | Street Name |
| Nepal                                      | Major Roads Only    |         |               | Street Name |
| Netherlands                                | Good                |    x    |       x       | Rooftop     |
| New Caledonia                              | Major Roads Only    |         |               | Street Name |
| New Zealand                                | Good                |    x    |       x       | Rooftop     |
| Nicaragua                                  | Good                |         |               | Street Name |
| Niger                                      | Fair                |         |               | Street Name |
| Nigeria                                    | Good                |    x    |               | Address     |
| Niue                                       | Major Roads Only    |         |               | Basic       |
| Norfolk Island                             | Major Roads Only    |         |               | Street Name |
| North Korea                                | Major Roads Only    |         |               | Basic       |
| North Macedonia                            | Good                |         |               | Rooftop     |
| Northern Mariana Islands                   | Good                |         |               | Street Name |
| Norway                                     | Good                |    x    |       x       | Rooftop     |
| Oman                                       | Good                |    x    |               | Street Name |
| Pakistan                                   | Major Roads Only    |         |               | Street Name |
| Palau                                      | Major Roads Only    |         |               | Basic       |
| Palestinian Authority                      | Major Roads Only    |         |               | Basic       |
| Panama                                     | Good                |         |               | Street Name |
| Papua New Guinea                           | Major Roads Only    |         |               | Street Name |
| Paraguay                                   | Good                |         |               | Address     |
| Peru                                       | Good                |    x    |               | Address     |
| Philippines                                | Good                |    x    |       x       | Rooftop     |
| Pitcairn Islands                           | Major Roads Only    |         |               | Street Name |
| Poland                                     | Good                |    x    |       x       | Rooftop     |
| Portugal                                   | Good                |    x    |       x       | Rooftop     |
| Puerto Rico                                | Good                |    x    |               | Rooftop     |
| Qatar                                      | Good                |    x    |               | Rooftop     |
| Réunion                                    | Good                |         |               | Address     |
| Romania                                    | Good                |    x    |       x       | Address     |
| Russia                                     | Good                |         |       x       | Rooftop     |
| Rwanda                                     | Good                |         |               | Street Name |
| Saba                                       | Good                |         |               | Basic       |
| Saint Barthélemy                           | Good                |         |               | Street Name |
| Saint Kitts & Nevis                        | Good                |         |               | Street Name |
| Saint Lucia                                | Good                |         |               | Street Name |
| Saint Martin                               | Good                |         |               | Street Name |
| Saint Pierre & Miquelon                    | Good                |         |               | Street Name |
| Saint Vincent & the Grenadines             | Good                |         |               | Basic       |
| Samoa                                      | Major Roads Only    |         |               | Street Name |
| San Marino                                 | Good                |    x    |       x       | Rooftop     |
| São Tomé & Príncipe                        | Major Roads Only    |         |               | Basic       |
| Saudi Arabia                               | Good                |    x    |               | Address     |
| Senegal                                    | Good                |         |               | Street Name |
| Serbia                                     | Good                |         |       x       | Rooftop     |
| Seychelles                                 | Good                |         |               | Street Name |
| Sierra Leone                               | Major Roads Only    |         |               | Street Name |
| Singapore                                  | Good                |    x    |       x       | Rooftop     |
| Sint Eustatius                             | Good                |         |               | Basic       |
| Sint Maarten                               | Good                |         |               | Street Name |
| Slovakia                                   | Good                |    x    |       x       | Rooftop     |
| Slovenia                                   | Good                |    x    |       x       | Rooftop     |
| Solomon Islands                            | Major Roads Only    |         |               | Basic       |
| Somalia                                    | Major Roads Only    |         |               | Street Name |
| South Africa                               | Good                |    x    |       x       | Rooftop     |
| South Georgia & the South Sandwich Islands | Major Roads Only    |         |               | Basic       |
| South Sudan                                | Major Roads Only    |         |               | Street Name |
| Spain                                      | Good                |    x    |       x       | Rooftop     |
| Sri Lanka                                  | Major Roads Only    |         |               | Street Name |
| St Helena, Ascension, Tristan da Cunha     | Major Roads Only    |         |               | Street Name |
| Sudan                                      | Major Roads Only    |         |               | Street Name |
| Suriname                                   | Good                |         |               | Street Name |
| Svalbard                                   | Good                |         |               | Street Name |
| Sweden                                     | Good                |    x    |       x       | Address     |
| Switzerland                                | Good                |    x    |       x       | Rooftop     |
| Syria                                      | Major Roads Only    |         |               | Street Name |
| Taiwan                                     | Good                |    x    |       x       | Rooftop     |
| Tajikistan                                 | Major Roads Only    |         |               | Street Name |
| Tanzania                                   | Good                |         |               | Street Name |
| Thailand                                   | Good                |    x    |       x       | Rooftop     |
| Timor-Leste                                | Major Roads Only    |         |               | Basic       |
| Togo                                       | Fair                |         |               | Street Name |
| Tokelau                                    | Major Roads Only    |         |               | Basic       |
| Tonga                                      | Major Roads Only    |         |               | Street Name |
| Trinidad & Tobago                          | Good                |         |               | Street Name |
| Tunisia                                    | Good                |         |               | Rooftop     |
| Türkiye                                     | Good                |    x    |       x       | Rooftop     |
| Turkmenistan                               | Major Roads Only    |         |               | Street Name |
| Turks & Caicos Islands                     | Good                |         |               | Basic       |
| Tuvalu                                     | Major Roads Only    |         |               | Basic       |
| U.S. Outlying Islands                      | Major Roads Only    |         |               | Basic       |
| U.S. Virgin Islands                        | Good                |         |               | Rooftop     |
| Uganda                                     | Good                |         |               | Street Name |
| Ukraine                                    | Good                |         |               | Rooftop     |
| United Arab Emirates                       | Good                |    x    |               | Rooftop     |
| United Kingdom                             | Good                |    x    |       x       | Rooftop     |
| United States                              | Good                |    x    |       x       | Rooftop     |
| Uruguay                                    | Good                |    x    |       x       | Rooftop     |
| Uzbekistan                                 | Major Roads Only    |         |               | Basic       |
| Vanuatu                                    | Major Roads Only    |         |               | Basic       |
| Vatican City                               | Good                |    x    |       x       | Street Name |
| Venezuela                                  | Good                |         |               | Street Name |
| Vietnam                                    | Good                |    x    |       x       | Rooftop     |
| Wallis & Futuna                            | Major Roads Only    |         |               | Basic       |
| Yemen                                      | Good                |         |               | Street Name |
| Zambia                                     | Good                |         |               | Street Name |
| Zimbabwe                                   | Good                |         |               | Street Name |
