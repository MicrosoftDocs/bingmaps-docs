---
title: "Address Object2 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: db835fd0-e2d1-4cd9-b465-e81be7e4a262
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Address Object
Represents a structured address.

## Properties

Name                   | Type              | Description
---------------------- | ----------------- | ---------------------------------
`addressLine`          | string            | The street line of an address. The addressLine property is the most precise, official line for an address relative to the postal agency servicing the area specified by the locality or postalCode properties.
`adminDistrict`        | string            | The subdivision name within the country or region for an address. This element is also commonly treated as the first order administrative subdivision. An example is a US state, such as “Oregon”.
`countryRegion`        | string            | The country or region name of the address.
`countryRegionISO2`    | string            | A string specifying the [two-letter ISO country code](http://www.iso.org/iso/country_codes.htm).
`district`             | string            | The second, third, or fourth order subdivision within a country, dependency, or region.
`formattedAddress`     | string            | The complete, unparsed address.
`locality`             | string            | The locality, such as the primary city, that corresponds to an address. An example is “Seattle”.
`postalCode`           | string            | The post code, postal code, or ZIP code of an address. An example is a US ZIP code, such as “98152”.

