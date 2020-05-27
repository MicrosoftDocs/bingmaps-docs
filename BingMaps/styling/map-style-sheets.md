---
title: "Map Style Sheets | Microsoft Docs"
ms.custom: ""
ms.date: "05/26/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 966B4D77-FEAC-41FB-8FBB-7D4AFBA86651
caps.latest.revision: 3
author: "dbuerer"
ms.author: ""
manager: ""
ms.service: "bing-maps"
---
# Map Style Sheet Reference in Maps

Microsoft mapping technologies use map style sheets to define the appearance of maps. Map style sheets can be used in:
* The [Bing Maps web control](https://docs.microsoft.com/bingmaps/v8-web-control/?redirectedfrom=MSDN) using the [customMapStyle option](https://docs.microsoft.com/bingmaps/v8-web-control/map-control-api/mapoptions-object).
* The [Windows map control](https://docs.microsoft.com/uwp/api/windows.ui.xaml.controls.maps.mapcontrol) using the [MapStyleSheet.ParseFromJson](https://docs.microsoft.com/uwp/api/windows.ui.xaml.controls.maps.mapstylesheet.parsefromjson#Windows_UI_Xaml_Controls_Maps_MapStyleSheet_ParseFromJson_System_String_) method.
* The [Android or iOS map control](https://docs.microsoft.com/bingmaps/sdk-native/) using the [MapStyleSheet](https://docs.microsoft.com/bingmaps/sdk-native/map-control-api/mapstylesheet-class) class.

Map style sheets can be created interactively using the [Map Style Sheet Editor application](https://www.microsoft.com/store/productId/9NBHTCJT72FT).

A map style sheet consists primarily of [entries](map-style-sheet-entries.md) and [properties](map-style-sheet-entry-properties.md) on those entries that you can override to customize the appearance of your map.

## JSON Style Sheet Format 

The primary way to represent a map style sheet is using JavaScript Object Notation (JSON). The following JSON can be used to make land appear white, water red, water labels green, and roads fill with blue:

```json
{"version":"1.*",
    "settings":{"landColor":"#FFFFFF"},
    "elements":{"water":{"fillColor":"#FF0000","labelColor":"#00FF00"}, "road":{"fillColor":"#0000FF"}}
}
```

This JSON can be used to remove all labels and points from a map.

```json
{"version":"1.*", "elements":{"mapElement":{"labelVisible":false},"point":{"visible":false}}}
```

Sometimes the value of a property is transformed to produce the final result. For example, vegetation fillColor has slightly different shades depending on type of the entity being displayed. This behavior can be turned off, thereby using the precise provided value, by using the ignoreTransform property.

```json
{"version":"1.*",
    "settings":{"shadedReliefVisible":false},
    "elements":{"vegetation":{"fillColor":{"value":"#999999","ignoreTransform":true}}}
}
```

## Web Only URL Style Sheet Format

For simple style changes with the web map control, compact versions of the style sheet can be used through URL parameters.  These can be done with the long form:

```url
water|fillColor:FF0000;labelColor:00FF00_road|fillColor:0000FF_global|landColor:FFFFFF 
```

...or the short form:

```url
wt|fc:FF0000;lbc:00FF00_rd|fc:0000FF_g|landColor:FFFFFF
```

The URL style sheet can then be appended to a REST Static Image request or a tile URL. For example:

```url
http://dev.virtualearth.net/REST/V1/Imagery/Map/Road/Bellevue%20Washington?&key=[YOUR_BING_MAPS_KEY]&st=wt|fc:FF0000;lbc:00FF00_rd|fc:0000FF_g|landColor:FFFFFF
```