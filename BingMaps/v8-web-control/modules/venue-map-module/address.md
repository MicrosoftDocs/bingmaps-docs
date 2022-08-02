---
title: Venue address JSON class | Microsoft Docs
titleSuffix: Microsoft Bing Maps
description: Venue address JSON class represents an address of a venue map or entity within a venue map. Includes Properties and Example.
ms.custom: 
ms.date: 05/26/2020
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: 64878C5D-0F34-4229-BA8E-8351E7C5558B
caps.latest.revision: 3
author: DavidBuerer
ms.author: dbuerer
manager: 
ms.service: bing-maps
---

# Venue address JSON class

Represents an address of a [venue] map or [entity] within a venue map.

## Properties

| Property          | Type   | Description |
|-------------------|--------|-------------|
| addressLine       | string | The first line of the address that identifies the street location. |
| suite             | string | The suite identifier. |
| locality          | string | The populated for the address which may be the city, suburb, or neighborhood depending on the country. |
| adminDistrict     | string | The subdivision name in the country or region (may be state, province, etc.). |
| adminDistrict2    | string | The subdivision in the adminDistrict. |
| postalCode        | string | The post code, postal code, or ZIP code of the address. |
| countryRegionCode | string | The ISO 3166-1 Alpha-2 country code of the address. |

## Example

```json
{
  "addressLine": "One Microsoft Way",
  "locality": "Redmond",
  "adminDistrict": "WA",
  "postalCode": "98052",
  "countryRegionCode": "US"
}
```

[venue]: venue.md
[entity]: entity.md
