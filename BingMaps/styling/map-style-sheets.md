---
title: Map Style Sheet Reference in Maps
description: A map style sheet defines the appearance of a map in various Microsoft map controls and consists primarily of entries and properties.
ms.custom: 
ms.date: 05/26/2020
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: 966B4D77-FEAC-41FB-8FBB-7D4AFBA86651
caps.latest.revision: 3
author: DavidBuerer
ms.author: dbuerer
manager: 
ms.service: bing-maps
---
# Map Style Sheet Reference in Maps

A map style sheet defines the appearance of a map in various [Microsoft map controls](map-style-sheet-support.md).  A map style sheet consists primarily of [entries](map-style-sheet-entries.md) and [properties](map-style-sheet-entry-properties.md) on those entries that you can override to customize the appearance.

> [!TIP]
> Map style sheets can be created interactively using the [Map Style Sheet Editor application](https://www.microsoft.com/store/productId/9NBHTCJT72FT).

## JSON Style Sheet Format

The primary way to represent a map style sheet is using JavaScript Object Notation (JSON).  There are four root properties to a style sheet:

1. **version** - Defines the version that the style sheet targets, which effects which entries and properties are valid.  Wildcard characters are supported.
2. **settings** - A set of properties that apply to the map as a whole rather than a specific element of the map.
3. **elements** - Settings for specific elements of the map.
4. **extensions** - Settings for custom elements.  See [Map Style Sheet Extensions](map-style-sheet-extensions.md)

The following JSON can be used to make land appear white, water red, water labels green, and roads fill with blue:

```json
{
    "version":"1.*",
    "settings":{"landColor":"#FFFFFF"},
    "elements":{
        "water":{"fillColor":"#FF0000","labelColor":"#00FF00"}, 
        "road":{"fillColor":"#0000FF"}}
}
```

![Style Sample](media/style_sample.png)

This JSON can be used to remove all labels and points from a map.

```json
{
    "version":"1.*", 
    "elements":{"mapElement":{"labelVisible":false},"point":{"visible":false}}
}
```

Sometimes the value of a property is transformed to produce the final result. For example, vegetation fillColor has slightly different shades depending on type of the entity being displayed. This behavior can be turned off, thereby using the precise provided value, by using the ignoreTransform property.

```json
{
    "version":"1.*",
    "settings":{"shadedReliefVisible":false},
    "elements":{"vegetation":{"fillColor":{"value":"#999999","ignoreTransform":true}}}
}
```

## Web Only URL Style Sheet Format

For simple style changes with the [static map control](../rest-services/imagery/get-a-static-map.md), compact versions of the style sheet can be used through URL parameters.  These can be done with the long form:

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

Here is the image this request would return:

![Red Blue Map Style](media/bmv8-redbluemapstyle.jpg)

If the style is too long for a URL, when using the REST imagery service, the style can be passed in using a POST request. The POST data object format is: `style=[Your custom style]`
