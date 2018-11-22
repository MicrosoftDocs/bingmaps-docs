---
title: "Setting Map Control Parameters2 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 094936de-182f-439c-92de-c7733478bd1e
caps.latest.revision: 18
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Setting Map Control Parameters
When specifying the URL to the map control in a script reference, additional URL parameters can be added to configure how the map control functions.

## Setting Parameters

To add a parameter to the map control src URL, add a "?", the parameter, and set it "=" to one of the allowable values. Use "&" to separate parameters. 

The following example sets the map control URL such that it triggers a callback function called GetMap after the script has finished loading. It also loads the experimental branch of the map control in Italian.

```
<script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&branch=experimental&key=[YOUR_BING_MAPS_KEY]' async defer></script>
```

## Parameters

|   URL Parameter   |   Description   |
|-------------------|-----------------|
| `branch`    |	Specifies which branch of the SDK to load. Supported values:<br/><br/> • `release` (default)<br/> •   `experimental`<br /><br/>  See the [Map Control Branches](map-control-branches.md) section for more details. |
| `callback`  | The name of a callback function that should be called after the map control script has finished loading. |
| `key` | The Bing Maps Key used to authenticate the application. By specifying your Bing Maps key as a URL parameter in the map script reference, it will allow for live site issues reported to the Bing Maps Enterprise support team by licensed customers to be migrated faster.<br/><br/>**Tip**: if you need to get access to the Bing Maps key, it is available in the map options: `map.getOptions().credentials` |
| `setLang`         | Specifies the language to use for the map labels and navigation controls.<br/><br/>**Example:** en <br/><br/>The map automatically detects and sets this value based on the users location and device settings. It is not generally recommended to override this parameter unless testing. |
| `setMkt`          | This is a market parameter that provides insights into the users location. This is used to determine which features are available to the map in this area. For example, if the user is in an area where streetside imagery is not available, the map won’t list it as an option in the navigation bar. If the locale parameter is set to "en-US", an area where streetside imagery is available, this option will appear.<br/><br/>**Example:** en-US <br/><br/>The map automatically detects and sets this value based on the users location and device settings. It is not generally recommended to override this parameter unless testing.|
| `UR`              | A user region string that contains an [ISO 3166-1 alpha-2 country region code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). The user region value is used to ensure that disputed borders and location names, align with the views of the specified user region.<br/><br/>For a list of values, see the Region Localities section in the [Geospatial Endpoint Service](../articles/geospatial-endpoint-service.md) topic.<br/><br/> Due to the sensitivity of this feature, it is recommended to only use this when testing and to let the map automatically set this value in your production application.<br/><br/>**Example:** CN |

## Localizing the Map

The Bing Maps V8 Map Control automatically detects the users language and culture settings from their browser and uses this to localize the map control. However, it is possible to override the detected settings if desired by using the `setLang` and `setMkt` parameters. 

Here is an example of Bing Maps with the language parameter set to "fr" and the locale parameter set to "fr-FR".

```html
<script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&setMkt=fr-FR&setLang=fr' async defer></script>
```

The resulting map looks like this:

![French localized map](../v8-web-control/media/bmv8-franchlocalizedmap.PNG)

### Supported Languages

| Language - Country/Region | Culture | Map Labels | Navigation Control | Location & Directions | AutoSuggest |
|---------------------------|---------|------------|--------------------|-----------------------|-------------|
| Arabic - Saudi Arabia | ar-SA | x |  | x* | x |
| Basque | eu | x |  | x* | x |
| Bulgarian | bg | x |  | x* | x |
| Bulgarian - Bulgaria | bg-BG | x |  | x* | x |
| Catalan Spanish | ca | x | x | x | x |
| Central Kurdish | ku-Arab | x |  | x* | x |
| Chinese - China | zh-CN | x | x | x | x |
| Chinese - Hong Kong | zh-HK | x | x | x | x |
| Chinese - Simplified | zh-Hans | x | x | x | x |
| Chinese - Taiwan | zh-TW | x | x | x | x |
| Chinese - Traditional | zh-Hant | x | x | x | x |
| Czech | cs | x |  | x* | x |
| Czech - Czech Republic | cs-CZ | x |  | x* | x |
| Danish | da | x |  | x* | x |
| Danish - Denmark | da-DK | x |  | x* | x |
| Dutch - Belgium | nl-BE | x | x | x | x |
| Dutch - Netherlands | nl | x | x | x | x |
| Dutch - Netherlands | nl-NL | x | x | x | x |
| English - Australia | en-AU | x | x | x | x |
| English - Canada | en-CA | x | x | x | x |
| English - India | en-IN | x | x | x | x |
| English - United Kingdom | en-GB | x | x | x | x |
| English - United States | en-US | x | x | x | x |
| Finnish | fi | x |  | x* | x |
| Finnish - Finland | fi-FI | x |  | x* | x |
| French - Belgium | fr-BE | x | x | x | x |
| French - Canada | fr-CA | x | x | x | x |
| French - France | fr | x | x | x | x |
| French - France | fr-FR | x | x | x | x |
| French - Switzerland | fr-CH | x | x |  |  |
| Galician | gl | x |  | x* | x |
| German - Germany | de | x | x | x | x |
| German - Germany | de-DE | x | x | x | x |
| Greek | el | x |  | x* | x |
| Hebrew | he | x |  | x* | x |
| Hebrew - Israel | he-IL | x |  | x* | x |
| Hindi | hi | x |  | x* | x |
| Hindi - India | hi-IN | x |  | x* | x |
| Hungarian | hu | x |  | x* | x |
| Hungarian - Hungary | hu-HU | x |  | x* | x |
| Icelandic | is | x |  | x* | x |
| Icelandic - Iceland | is-IS | x |  | x* | x |
| Italian - Italy | it | x | x | x | x |
| Italian - Italy | it-IT | x | x | x | x |
| Japanese | ja | x | x | x | x |
| Japanese - Japan | ja-JP | x | x | x | x |
| Korean | ko | x |  | x* | x |
| Korean - Korea | Ko-KR | x |  | x* | x |
| Kyrgyz | ky-Cyrl | x | x | x | x |
| Latvian | lv | x |  | x* | x |
| Latvian - Latvia | lv-LV | x |  | x* | x |
| Lithuanian | lt | x |  | x* | x |
| Lithuanian - Lithuania | lt-LT | x |  | x* | x |
| Norwegian - Bokmål | nb | x | x | x | x |
| Norwegian - Bokmål - Norway | nb-NO | x | x | x | x |
| Norwegian - Nynorsk | nn | x |  | x* | x |
| Polish | pl | x | x | x | x |
| Polish - Poland | pl-PL | x | x | x | x |
| Portuguese - Brazil | pt-BR | x | x | x | x |
| Portuguese - Portugal | pt-PT | x | x | x | x |
| Russian | ru | x | x | x | x |
| Russian - Russia | ru-RU | x | x | x | x |
| Spanish - Mexico | es-MX | x | x | x | x |
| Spanish - Spain | es | x | x | x | x |
| Spanish - Spain | es-ES | x | x | x | x |
| Spanish - United States | es-US | x | x | x | x |
| Swedish - Sweden | sv | x | x | x | x |
| Swedish - Sweden | sv-SE | x | x | x | x |
| Tatar - Cyrillic | tt-Cyrl | x | x | x | x |
| Thai | th | x |  | x* | x |
| Thai - Thailand | th-TH | x |  | x* | x |
| Turkish | tr | x | x | x | x |
| Turkish - Turkey | tr-TR | x | x | x | x |
| Ukrainian | uk | x |  | x | x |
| Ukrainian - Ukraine | uk-UA | x |  | x | x |
| Uyghur | ug-Arab | x | x | x | x |
| Valencian | ca-ES-valencia | x | x | x | x |
| Vietnamese | vi | x |  | x* | x |
| Vietnamese - Vietnam | vi-VN | x |  | x* | x |

\* Directions input panel may not be localized. Some English words may appear in the route summary. The step by step instructions will be localized. 

### Localization of Error Messages

* Error messages are always displayed in English - United States.

### Why does Bing Maps use three parameters for localization?

Most mapping systems that support localization, only provide one or two parameters for localization, so you might be wondering why does Bing Maps provide three. Take for example this scenario; 
A user who is based in India visits a travel site. By default, the map would set the user region to "IN" and ensure that disputed borders are displayed to align with the views of the people of India, the language would be set to English ("en") or one of the many languages spoken in India depending on the customer's computer settings, and the locale parameter would be set to "en-IN" which would hide certain features that are no available in India, such as streetside. Being that this is a travel site and the user likely will be looking at areas outside of India, possibly a city in the USA, the user may be interested in displaying streetside imagery of their destination. The travel site can override the default locale parameter with a "en-US" value and this will enable this feature.

