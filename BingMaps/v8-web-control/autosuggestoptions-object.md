---
title: "AutosuggestOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ca9b9601-ecae-4168-9a41-98b758b016bd
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bingmaps"
---
# AutosuggestOptions Object
The following Autosuggest option properties can be used to customize how suggestions are retrieved. 

Name                   | Type               | Description
---------------------- | ------------------ | --------------------------------------------------
`addressSuggestions`   | boolean            | Specifies if street address suggestions should be returned. Default: **true**
`autoDetectLocation`   | boolean            | Specifies if the user’s location should be auto detected using their IP address, if no location information is provided in the `userLocation` property. Default: **true**
`bounds`               | LocationRect       | A bounding box that is used to help influence the results such that locations that are in or near this bounding box are given more weight than they would normally. 
`countryCode` | string | A string specifying the [ISO 3166-1 alpha-2 country region code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) which is used to limit suggests to a single country. 
`map`                  | Map                | A reference to a map instance. If the `useMapView` property is set to true, the bounding box of the map view will be used to influence the weight of suggestions.
`maxResults`           | number             | The maximum number of results to return. Can be any value between 1 and 10. Default: **5**
`placeSuggestions`     | boolean            | Specifies if place suggestions (city, landmark, etc.) should be returned. Default: **true**
`useMapView`           | boolean            | Indicates if the maps bounding box should be used to influence the suggested results. Ignored if the bounds property is set. Default: **true**
`userLocation`         | Location           | A coordinate indicating where the user is located. This will influence the results to be more relevant to the user. 
