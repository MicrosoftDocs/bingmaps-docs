---
title: "SuggestionResult Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ddda2c99-fcb8-42b8-9f18-40d841b97dea
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# SuggestionResult Object
Represents the suggestion result from the Autosuggest manager.

## Properties

Name                    | Type          | Description
----------------------- | ------------- | ------------------------------------------
`address`               | [Address](Address%20Object.md) | A structured address object for the result.
`bestView`              | [LocationRect](LocationRect%20Class.md)  | A LocationRect that can be used to set the map view over the result.
`entityId`              | string        | Unique entity id to be used for searching the entity.
`entityType`            | string        | The type of the result; Address, Place
`entitySubType`         | string        | The sub type of result; Address, RoadBlock, PopulatedPlace, CountryRegion, etc.
`subtitle` | string | A secondary title that provides additional context to the title value of the suggestion.
`formattedSuggestion`   | string        | A nicely formatted suggestion string for the result based on market.
`location`              | [Location](Location%20Class.md)      | The coordinate of the result. This value is only returned for place (city, landmarks) results and not for addresses. Street addresses will need to be geocoded to get their location.
`title`                 | string        | The display title for the result (i.e. “Redmond”).
