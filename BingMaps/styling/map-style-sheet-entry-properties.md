---
title: "Map Style Sheet Entry Properites | Microsoft Docs"
ms.custom: ""
ms.date: "05/26/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 9C7DD543-050F-4179-914F-E0097A03491F
caps.latest.revision: 3
author: "dbuerer"
ms.author: ""
manager: ""
ms.service: "bing-maps"
---
# Map Style Sheet Entry Properties

The properties that are grouped and listed below can be set on [entries](map-style-sheet-entries.md) in a [map style sheet](map-style-sheets.md) to customize the appearance of a map in various [Microsoft map controls](map-style-sheet-support.md).

Map style sheets can be created interactively using the [Map Style Sheet Editor application](https://www.microsoft.com/store/productId/9NBHTCJT72FT).

In this simple JSON style sheet, the "water" entry is a MapElement, so it can set the "fillColor" property.

```json
{"version":"1.*", "elements":{"water":{"fillColor":"#FF0000"}}}
```

All color values are specified as a hex **\#RRGGBB** or **\#AARRGGBB** string.

> **Tip:** Ensure that all colors have 6 or 8 characters. If there is any other number of characters, the style will be considered invalid.

## Version properties

| Property | Type   | Description |
|----------|--------|-------------|
| version  | string | Targeted style sheet version. Used for applicability. "1.0" for default, "1.*" for additional minor features updates. |

## Settings properties

Web: ISettingStyle

| Name                    | Type    | Web     | Style | Description |
|-------------------------|---------|---------|-------|-------------|
| atmosphereVisible	      | boolean |         | [1.0] | A flag that indicates whether the atmosphere appears in the 3D control. |
| buildingTexturesVisible | boolean |         | [1.2] | A flag that indicates whether or not to show textures on symbolic 3D buildings that have textures. |
| fogColor                | color   |         | [1.0] | The ARGB color value of the distance fog that appears in the 3D control. |
| glowColor               | color   |         | [1.0] | The ARGB color value that might be applied to label glow and icon glow. |
| imageFamily             | string  |         | [1.0] | The name of image set to use for this style. Set this value to Default for signs that use fixed colors that are based on the real-world sign. Set this value to Palette for signs that use palette configurable colors. |
| landColor               | color   | lc      | [1.0] | The ARGB color value of the land before anything is drawn on that land. |
| logosVisible            | color   |         | [1.0] | A flag that indicates whether items that have an Organization property should draw the appropriate Logos or use a generic icon. |
| officialColorVisible    | boolean |         | [1.0] | A flag that indicates whether items that have an official color property (such as transit lines in China) should draw that color. For example, turn this value off for a black and white map. |
| rasterRegionsVisible    | boolean |         | [1.0] | A flag that indicates whether or not to draw raster regions where they have a better representation than vectors (Japan and Korea). |
| shadedReliefVisible     | boolean | shadedReliefVisible | [1.0] | A flag that indicates whether or not to draw elevation shading on the map. |
| shadowColor             | color   |         | [1.3] | The color of the shadow behind icons that use shadows. |
| spaceColor              | color   |         | [1.0] | The color value for the area around the map. |
| terrainFlat             | boolean |         | [1.5] | A flag that indicates whether the terrain should be flat (disabled) on the map. |
| useDefaultImageColors   | boolean |         | [1.0] | A flag that indicates whether the original colors in the SVG should be used rather than looking up the palette entry for colors in an image. |

## BaseMapStyle

The baseMapStyle root property specifies which base map style sheet your style sheet is derived from.  It is supported starting at style version [1.4].

In this example, the base map style is set to vibrantLight (the Bing Maps style) and all point features are turned off.

```json
{
  "version":"1.*",
  "baseMapStyle":"vibrantLight",
  "elements": {
    "point": {
      "labelVisible": false,
      "visible": false
    }
  }
}
```

| baseMapStyle          | Description |
|-----------------------|-------------|
| canvasDark            | Dark canvas style |
| canvasGray            | Gray canvas style |
| canvasLight           | Light canvas style |
| roadHighContrastDark  | High contrast dark symbolic style |
| roadHighContrastLight | High contrast light symbolic style |
| aerialWithOverlay     | Photo-real style with labels and icons |
| roadLight             | Light symbolic style |
| roadDark              | Dark symbolic style |
| vibrantLight          | Light vibrant symbolic style (Bing Maps style) |

## MapElement properties

Web: IMapElementStyle

| Property          | Type    | Web      | Style | Description |
|-------------------|---------|----------|-------|-------------|
| backgroundScale   | number  |          | [1.0] | Amount by which the background element of an icon should be scaled. For example, use 1 for default and 2 for twice as large. |
| fillColor         | color   | fc       | [1.0] | The color that is used for filling polygons, the background of point icons, and for the center of lines if they have split. |
| fontFamily        | string  |          | [1.0] |  |
| fontWeight        | string  |          | [1.4] | The density of a typeface, in terms of the lightness or heaviness of the strokes. "Light", "Normal", "SemiBold" and "Bold" can be set. |
| iconColor         | color   |          | [1.0] | The color of the glyph shown in the middle of a point icon. |
| iconScale         | number  |          | [1.1] | Amount by which the glyph of an icon should be scaled. For example, use 1 for default and 2 for twice as large. |
| labelColor        | color   | lbc      | [1.0] | The color of a map label. |
| labelOutlineColor | color   | loc      | [1.0] | The outline color of a map label. |
| labelScale        | number  |          | [1.0] | The amount by which default label sizes are scaled. For example, use 1 for default and 2 for twice as large. |
| labelVisible      | boolean | lv       | [1.0] | Species if a map label type is visible or not. |
| overwriteColor    | boolean |          | [1.0] | Makes The alpha value of the FillColor overwrite the StrokeColor rather than blend with it. |
| scale             | number  |          | [1.0] | The amount by which the whole point's size is scaled. For example, use 1 for default and 2 for twice as large. |
| strokeColor       | color   | sc       | [1.0] | The color to use for the outline around polygons, the outline around point icons, and the color of lines. |
| strokeWidthScale  | number  |          | [1.0] | The amount by which the stroke of lines are scaled. For example, use 1 for default and 2 for twice as large. |
| visible           | boolean | v        | [1.0] | Specifies if the map element is visible or not. |

## BorderedMapElement properties

Web: IBorderedMapElementStyle

This property group extends the MapElement (web: IMapElementStyle) property group.

| Property           | Type    | Web      | Style | Description |
|--------------------|---------|----------|-------|-------------|
| borderOutlineColor | color   | boc      | [1.0] | The secondary or casing line color of the border of a filled polygon. |
| borderStrokeColor  | color   | bsc      | [1.0] | The primary line color of the border of a filled polygon. |
| borderVisible      | boolean | bv       | [1.0] | Specifies if a border is visible or not. |
| borderWidthScale   | number  |          | [1.0] | The amount by which the stroke of borders are scaled. For example, use 1 for default and 2 for twice as large. |

## PointStyle properties

This property group extends the MapElement (web: IMapElementStyle) property group.

| Property              | Type    | Web      | Style | Description |
|-----------------------|---------|----------|-------|-------------|
| shadowVisible         | boolean |          | [1.4] | The flag that indicates whether the shadow of icon should be visible or not. |
| shape-Background      | string  |          | [1.4] | Shape to use as the background of the icon--replacing any shape that exists there. |
| shape-Icon            | string  |          | [1.4] | Shape to use as the foreground glyph of the icon--replacing any shape that exists there. |
| stemAnchorRadiusScale | number  |          | [1.2] | Amount by which the anchor point of an icon stem should be scaled. For example, use 1 for default and 2 for twice as large. |
| stemColor             | color   |          | [1.0] | The color of the stem coming out of the bottom of the icon in 3D mode. |
| stemHeightScale       | number  |          | [1.2] | Amount by which the length of the stem of an icon should be scaled. For example, use 1 for default and 2 for twice as long. |
| stemOutlineColor      | color   |          | [1.0] | The color of the outline around the stem coming out of the bottom of the icon in 3D mode. |
| stemWidthScale        | number  |          | [1.0] | Amount by which the width of the stem of an icon should be scaled. For example, use 1 for default and 2 for twice as long. |

## MapElement3D properties

This property group extends the MapElement (web: IMapElementStyle) property group.

| Property              | Type    | Web      | Style | Description |
|-----------------------|---------|----------|-------|-------------|
| renderAsSurface       | boolean |          | [1.2] | A flag that indicates that a 3D model should be rendered like a building--without depth fading against the ground. |

[1.0]: map-style-sheet-support.md
[1.1]: map-style-sheet-support.md
[1.2]: map-style-sheet-support.md
[1.3]: map-style-sheet-support.md
[1.4]: map-style-sheet-support.md
[1.5]: map-style-sheet-support.md