---
title: "Address Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f8f39bf0-4bc3-486d-929c-00cb9fc23827
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Address Object
Represents a structured address.

Name               | Type       | Description
------------------ | ---------- | --------------------------------
`addressLine`        | string     | The street line of an address. The addressLine property is the most precise, official line for an address relative to the postal agency servicing the area specified by the locality or postalCode properties.
`adminDistrict`      | string	    | The subdivision name within the country or region for an address. This element is also commonly treated as the first order administrative subdivision. An example is a US state, such as “Oregon”.
`countryRegion`      | string     | The country or region name of the address.
`countryRegionISO2`  | string     | A string specifying the [two-letter ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
`district`           | string     | The second, third, or fourth order subdivision within a country, dependency, or region. An example is a US county, such as “King”.
`formattedAddress` | string | A nicely formatted address string.
`locality`           | string     | The locality, such as the primary city, that corresponds to an address. An example is “Seattle”.
`postalCode`         | string     | The post code, postal code, or ZIP code of an address. An example is a US ZIP code, such as “98152”.
