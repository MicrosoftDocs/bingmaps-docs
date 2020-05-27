---
title: "Map Style Sheet Reference in Maps | Microsoft Docs"
ms.custom: ""
ms.date: "05/26/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: C22745F9-7DD9-4348-8476-DC1AC0F7AC98
caps.latest.revision: 3
author: "dbuerer"
ms.author: ""
manager: ""
ms.service: "bing-maps"
---
# Map Style Sheet Reference in Maps

Microsoft mapping technologies use map style sheets to define the appearance of maps. A map style sheet is defined using JavaScript Object Notation (JSON) and can be used in:
* Web site's Map's [customMapStyle option](https://docs.microsoft.com/en-us/bingmaps/v8-web-control/map-control-api/mapoptions-object).
* A Windows Store application's [MapControl](https://docs.microsoft.com/uwp/api/windows.ui.xaml.controls.maps.mapcontrol) through the [MapStyleSheet.ParseFromJson](https://docs.microsoft.com/uwp/api/windows.ui.xaml.controls.maps.mapstylesheet.parsefromjson#Windows_UI_Xaml_Controls_Maps_MapStyleSheet_ParseFromJson_System_String_) method.
* An Android or iOS application's [MapStyleSheet](https://docs.microsoft.com/en-us/bingmaps/sdk-native/map-control-api/mapstylesheet-class).

Style sheets can be created interactively using the Map Style Sheet Editor application.

## JSON Format Overview

The following JSON can be used to make land appear white, water red, water labels green, and roads fill with blue:

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

Web Only URL Format
For simple style changes with the web control, compact versions of the style sheet can be used through URL parameters.  These can be done with the long form:

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

## Settings and Elements

The JSON entries that can be customized are represented in the following list.  They are represented as a tree structure where setting parent entry properties will override child entry properties.  The properties available to each entry can be found in the entry's property gorup.  This table uses ">" characters to represent levels in the entry hierarchy.

| Name               | Property Group | Web Arg | Windows Min | Android iOS Min | Description |
|--------------------|----------------|---------|-------------|-----------------|-------------|
| version            | Version        | version | 1703 | 1.0.0 | The style sheet version that you want to use. |
| settings           | Settings       | g       | 1703 | 1.0.0 | The settings that apply to the whole style sheet. |
| mapElement         | MapElement     | me      | 1703 | 1.0.0 | The parent entry to all map entries. |
| > baseMapElement   | MapElement     | bme     | 1703 | 1.0.0 | The parent entry to all non-user entries. |
| >> area            | MapElement     | ar      | 1703 | 1.0.0 | Areas describing land use. These should not to be confused with the physical buildings which are under the structure entry. |
| >>> airport        | MapElement     | ap      | 1703 | 1.0.0 | Areas that encompass airports. |
| >>> areaOfInterest | MapElement     | ai      | 1709 | 1.0.0 | Areas in which there are a high concentration of businesses or interesting points. |
| >>> cemetery       | MapElement     | cm      | 1703 | 1.0.0 | Areas that encompass cemeteries. |
| >>> continent      | MapElement     | ct      | 1703 | 1.0.0 | Continent area labels. |

## Property Groups

Each JSON entry has a set of properties that can be set on it.  These are listed in the property group for the entry.

### Version properties

| Property | Type | Web Type | Description |
|----------|------|----------|-------------|
| version | String | string | Targeted style sheet version. Used for applicability. "1.0" for default, "1.*" for additional minor features updates. |

### Settings properties
Web: ISettingStyle

| Name                    | Type    | Web Arg | Windows Min | Android iOS Min | Description |
|-------------------------|---------|---------|-------------|-----------------|-------------|
| atmosphereVisible	      | boolean |         | 1703        | 1.0.0           | A flag that indicates whether the atmosphere appears in the 3D control. |
| buildingTexturesVisible | boolean |         | 1803        | 1.0.0           | A flag that indicates whether or not to show textures on symbolic 3D buildings that have textures. |
| fogColor                | color   |         | 1703        | 1.0.0           | The ARGB color value of the distance fog that appears in the 3D control. |
| glowColor               | color   |         | 1703        | 1.0.0           | The ARGB color value that might be applied to label glow and icon glow. |
| imageFamily             | string  |         | 1703        | 1.0.0           | The name of image set to use for this style. Set this value to Default for signs that use fixed colors that are based on the real-world sign. Set this value to Palette for signs that use palette configurable colors. |
| landColor               | color   | lc      | 1703        | 1.0.0           | The ARGB color value of the land before anything is drawn on that land. |
| logosVisible            | color   |         | 1703        | 1.0.0           | A flag that indicates whether items that have an Organization property should draw the appropriate Logos or use a generic icon. |
| officialColorVisible    | boolean |         | 1703        | 1.0.0           | A flag that indicates whether items that have an official color property (such as transit lines in China) should draw that color. For example, turn this value off for a black and white map. |
| rasterRegionsVisible    | boolean |         | 1703        | 1.0.0           | A flag that indicates whether or not to draw raster regions where they have a better representation than vectors (Japan and Korea). |
| shadedReliefVisible     | boolean | shadedReliefVisible |  1703 | 1.0.0     | A flag that indicates whether or not to draw elevation shading on the map. |
| shadowColor             | color   |         | 1809        | 1.0.0           | The color of the shadow behind icons that use shadows. |
| spaceColor              | color   |         | 1703        | 1.0.0           | The color value for the area around the map. |
| terrainFlat             | boolean |         |             | 1.1.0 ?         | A flag that indicates whether the terrain should be flat (disabled) on the map. |
| useDefaultImageColors   | boolean |         | 1703        | 1.0.0           | A flag that indicates whether the original colors in the SVG should be used rather than looking up the palette entry for colors in an image. |

### MapElement properties
Web: IMapElementStyle

| Property          | Type    | Web Args | Windows Min | Android iOS Min | Description |
|-------------------|---------|----------|-------------|-----------------|-------------|
| backgroundScale   | number  |          | 1703        | 1.0.0           | Amount by which the background element of an icon should be scaled. For example, use 1 for default and 2 for twice as large. |
| fillColor         | color   | fc       | 1703        | 1.0.0           | The color that is used for filling polygons, the background of point icons, and for the center of lines if they have split. |
| fontFamily        | string  |          | 1703        | 1.0.0           | |
| fontWeight        | string  |          | 1903        | 1.0.0           | The density of a typeface, in terms of the lightness or heaviness of the strokes. "Light", "Normal", "SemiBold" and "Bold" can be set. |
| iconColor         | color   |          | 1703        | 1.0.0           | The color of the glyph shown in the middle of a point icon. |
| iconScale         | number  |          | 1709        | 1.0.0           | Amount by which the glyph of an icon should be scaled. For example, use 1 for default and 2 for twice as large. |
| labelColor        | color   | lbc      | 1703        | 1.0.0           | The color of a map label. |
| labelOutlineColor | color   | loc      | 1703        | 1.0.0           | The outline color of a map label. |
| labelScale        | number  |          | 1703        | 1.0.0           | The amount by which default label sizes are scaled. For example, use 1 for default and 2 for twice as large. |
| labelVisible      | boolean | lv       | 1703        | 1.0.0           | Species if a map label type is visible or not. |
| overwriteColor    | boolean |          | 1703        | 1.0.0           | Makes The alpha value of the FillColor overwrite the StrokeColor rather than blend with it. |
| scale             | number  |          | 1703        | 1.0.0           | The amount by which the whole point's size is scaled. For example, use 1 for default and 2 for twice as large. |
| strokeColor       | color   | sc       | 1703        | 1.0.0           | The color to use for the outline around polygons, the outline around point icons, and the color of lines. |
| strokeWidthScale  | number  |          | 1703        | 1.0.0           | The amount by which the stroke of lines are scaled. For example, use 1 for default and 2 for twice as large. |
| visible           | boolean | v        | 1703        | 1.0.0           | Specifies if the map element is visible or not. |

### BorderedMapElement properties
Web: IBorderedMapElementStyle

This property group extends the MapElement (web: IMapElementStyle) property group.

| Property           | Type    | Web Args | Windows Min | Android iOS Min | Description |
|--------------------|---------|----------|-------------|-----------------|-------------|
| borderOutlineColor | color   | boc      | 1703        | 1.0.0           | The secondary or casing line color of the border of a filled polygon. |
| borderStrokeColor  | color   | bsc      | 1703        | 1.0.0           | The primary line color of the border of a filled polygon. |
| borderVisible      | boolean | bv       | 1703        | 1.0.0           | Specifies if a border is visible or not. |
| borderWidthScale   | number  |          | 1703        | 1.0.0           | The amount by which the stroke of borders are scaled. For example, use 1 for default and 2 for twice as large. |

### PointStyle properties

This property group extends the MapElement (web: IMapElementStyle) property group.

| Property              | Type    | Web Args | Windows Min | Android iOS Min | Description |
|-----------------------|---------|----------|-------------|-----------------|-------------|
| shadowVisible         | boolean |          | 1903        | 1.0.0           | The flag that indicates whether the shadow of icon should be visible or not. |
| shape-Background      | string  |          | 1903        | 1.0.0           | Shape to use as the background of the icon--replacing any shape that exists there. |
| shape-Icon            | string  |          | 1903        | 1.0.0           | Shape to use as the foreground glyph of the icon--replacing any shape that exists there. |
| stemAnchorRadiusScale | number  |          | 1803        | 1.0.0           | Amount by which the anchor point of an icon stem should be scaled. For example, use 1 for default and 2 for twice as large. |
| stemColor             | color   |          | 1703        | 1.0.0           | The color of the stem coming out of the bottom of the icon in 3D mode. |
| stemHeightScale       | number  |          | 1803        | 1.0.0           | Amount by which the length of the stem of an icon should be scaled. For example, use 1 for default and 2 for twice as long. |
| stemOutlineColor      | color   |          | 1703        | 1.0.0           | The color of the outline around the stem coming out of the bottom of the icon in 3D mode. |
| stemWidthScale        | number  |          | 1703        | 1.0.0           | Amount by which the width of the stem of an icon should be scaled. For example, use 1 for default and 2 for twice as long. |

### MapElement3D properties

This property group extends the MapElement (web: IMapElementStyle) property group.

| Property              | Type    | Web Args | Windows Min | Android iOS Min | Description |
|-----------------------|---------|----------|-------------|-----------------|-------------|
| renderAsSurface       | boolean |          | 1803        |                 | A flag that indicates that a 3D model should be rendered like a building--without depth fading against the ground. |

