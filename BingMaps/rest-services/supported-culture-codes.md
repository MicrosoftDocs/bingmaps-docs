---
title: "Supported Culture Codes | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d7b4109e-8bb5-4a2e-a4de-187e2d0b4b0b
caps.latest.revision: 17
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Supported Culture Codes
The following list shows the culture codes supported by the [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)] APIs.  
  
> [!NOTE]
>  For supported cultures, street names are localized to the local culture. For example, if you request a location in France, the street names are localized in French. For other localized data such as country names, the level of localization will vary for each culture. For example, there may not be a localized name for the "United States" for every culture code.  
  
|Culture|Language|Locations and Routes|Imagery|  
|-------------|--------------|--------------------------|-------------|  
|af|Afrikaans|X||  
|am|Amharic|X||  
|ar-sa|Arabic (Saudi Arabia)|X||  
|as|Assamese|X||  
|az-Latn|Azerbaijani (Latin)|X||  
|be|Belarusian|X||  
|bg|Bulgarian|X||  
|bn-BD|Bangla (Bangladesh)|X||  
|bn-IN|Bangla (India)|X||  
|bs|Bosnian (Latin)|X||  
|ca|Catalan Spanish|X||  
|ca-ES-valencia|Valencian|X||  
|cs|Czech|X||  
|cy|Welsh|X||  
|da|Danish|X||  
|de|German (Germany)|X||  
|de-de|German (Germany)|X|X**|  
|el|Greek|X||  
|en-GB|English (United Kingdom)|X||  
|en-US|English (United States)|X|X**|  
|es|Spanish (Spain)|X||  
|es-ES|Spanish (Spain)|X|X**|  
|es-US|Spanish (United States)|X|X<sup>1</sup>|  
|es-MX|Spanish (Mexico)|X|X<sup>1</sup>|  
|et|Estonian|X||  
|eu|Basque|X||  
|fa|Persian|X||  
|fi|Finnish|X||  
|fil-Latn|Filipino|X||  
|fr|French (France)|X||  
|fr-FR|French (France)|X|X**|  
|fr-CA|French (Canada)|X|X<sup>2</sup>|  
|ga|Irish|X||  
|gd-Latn|Scottish Gaelic|X||  
|gl|Galician|X||  
|gu|Gujarati|X||  
|ha-Latn|Hausa (Latin)|X||  
|he|Hebrew|X||  
|hi|Hindi|X||  
|hr|Croatian|X||  
|hu|Hungarian|X||  
|hy|Armenian|X||  
|id|Indonesian|X||  
|ig-Latn|Igbo|X||  
|is|Icelandic|X||  
|it|Italian (Italy)|X||  
|it-it|Italian (Italy)|X|X**|  
|ja|Japanese|X||  
|ka|Georgian|X||  
|kk|Kazakh|X||  
|km|Khmer|X||  
|kn|Kannada|X||  
|ko|Korean|X||  
|kok|Konkani|X||  
|ku-Arab|Central Kurdish|X||  
|ky-Cyrl|Kyrgyz|X||  
|lb|Luxembourgish|X||  
|lt|Lithuanian|X||  
|lv|Latvian|X||  
|mi-Latn|Maori|X||  
|mk|Macedonian|X||  
|ml|Malayalam|X||  
|mn-Cyrl|Mongolian (Cyrillic)|X||  
|mr|Marathi|X||  
|ms|Malay (Malaysia)|X||  
|mt|Maltese|X||  
|nb|Norwegian (Bokmål)|X||  
|ne|Nepali (Nepal)|X||  
|nl|Dutch (Netherlands)|X||  
|nl-BE|Dutch (Netherlands)|X|X**|  
|nn|Norwegian (Nynorsk)|X||  
|nso|Sesotho sa Leboa|X||  
|or|Odia|X||  
|pa|Punjabi (Gurmukhi)|X||  
|pa-Arab|Punjabi (Arabic)|X||  
|pl|Polish|X||  
|prs-Arab|Dari|X||  
|pt-BR|Portuguese (Brazil)|X||  
|pt-PT|Portuguese (Portugal)|X||  
|qut-Latn|K’iche’|X||  
|quz|Quechua (Peru)|X||  
|ro|Romanian (Romania)|X||  
|ru|Russian|X||  
|rw|Kinyarwanda|X||  
|sd-Arab|Sindhi (Arabic)|X||  
|si|Sinhala|X||  
|sk|Slovak|X||  
|sl|Slovenian|X||  
|sq|Albanian|X||  
|sr-Cyrl-BA|Serbian (Cyrillic, Bosnia and Herzegovina)|X||  
|sr-Cyrl-RS|Serbian (Cyrillic, Serbia)|X||  
|sr-Latn-RS|Serbian (Latin, Serbia)|X||  
|sv|Swedish (Sweden)|X||  
|sw|Kiswahili|X||  
|ta|Tamil|X||  
|te|Telugu|X||  
|tg-Cyrl|Tajik (Cyrillic)|X||  
|th|Thai|X||  
|ti|Tigrinya|X||  
|tk-Latn|Turkmen (Latin)|X||  
|tn|Setswana|X||  
|tr|Turkish|X||  
|tt-Cyrl|Tatar (Cyrillic)|X||  
|ug-Arab|Uyghur|X||  
|uk|Ukrainian|X||  
|ur|Urdu|X||  
|uz-Latn|Uzbek (Latin)|X||  
|vi|Vietnamese|X||  
|wo|Wolof|X||  
|xh|isiXhosa|X||  
|yo-Latn|Yoruba|X||  
|zh-Hans|Chinese (Simplified)|X||  
|zh-Hant|Chinese (Traditional)|X||  
|zu|isiZulu|X||  
  
 **The Imagery API renders tiles in United States English (en-US) for all locations on the Earth at all zoom levels. The following languages are rendered for all locations on the Earth at zoom levels 1-9, and for Europe locations at all zoom levels (1-21): fr-FR, de-DE, it-IT, es-ES, nl-BE.  
  
 <sup>1</sup> When you specify es-MX or es-US in the request, the culture is converted to es-ES.  
  
 <sup>2</sup> When you specify fr-CA in the request, the culture is converted to fr-FR.