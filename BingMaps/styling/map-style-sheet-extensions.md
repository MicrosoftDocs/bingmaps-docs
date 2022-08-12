---
title: "Map Style Sheet Extensions | Microsoft Docs"
description: "This article provides guidelines on map style sheet extensions, which can be used to add custom entries and states to your map's styles and includes examples on how to create a custom entry, create a custom state, overriding transparency, swapping colors and changing background shapes."
ms.custom: ""
ms.date: "05/26/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8E33AAAE-5DC3-4B94-AD13-69B98402DF33
caps.latest.revision: 3
author: "dbuerer"
ms.author: "dbuerer"
manager: ""
ms.service: "bing-maps"
---
# Map Style Sheet Extensions

The extensions property at the root of a [map style sheet](map-style-sheets.md) can be used to add custom [entries](map-style-sheet-entries.md) and states to your map's styles. Entries and states can be set on your map elements in the various [Microsoft map controls](map-style-sheet-support.md) to define how they are styled.

## Create a Custom Entry

Creates a custom entry based on the foodPoint entry.  When a map element's style sheet entry is set to “myNamespace.myFoodPoint”, the icon used for the point will be the foodPoint’s icon, but scaled up twice as large.

```json
    { "version": "1.*",
      "extensions": {
        "myNamespace": {
          "myFoodPoint": {
            "parent": "foodPoint",
            "scale": 2
    } } } }
```

## Create a Custom State

In this example, when a map element's style sheet entry is set to “myNamespace.myCustomState”, the fillColor of the element will override the entry's fillColor with yellow.

```json
    { "version": "1.*",
      "extensions": {
        "myNamespace": {
          "myCustomState": {
            "fillColor": "#FFFF00"
    } } } }
```

When one or more states are applied to a map element, they are stacked on top of the element's entry and their properties override or interact with the properties of the entry.

States support the "parent" property to inherit from another state.  There are a few default states provided by the styling system including "disabled", "hover", and "selected", but these don't have to be used.

Setting the state of a map element to multiple states, usually represented as a semi-colon separated string like "hover;myNamespace.myState", means that each stat is stacked on top of each other and then stacked on the entry.

### Overriding Transparency

The "composition" property was added in style version [1.3].  In this example, two states that, when applied to a map element, will either blend a transparent green color with the underlying entry's fillColor or override the underlying entry's fillColor with a transparent green color.

```json
    { "version": "1.*",
      "extensions": {
        "myNamespace": {
          "myBlendedState": {
            "fillColor": { "value":"#AA008200", "composition": "blend" }
          },
          "myOverriddenState": {
            "fillColor": { "value":"#AA008200", "composition": "override" }
    } } } }
```

### Swapping Colors

The "property" pointer was added in style version [1.3].  This example shows a state that, when applied to a map element, will swap existing colors around.  This only works for color properties (not numeric or string properties), and it reads the property of the underlying entry (not of the state).

```json
    { "version": "1.*",
      "extensions": {
        "myNamespace": {
          "mySwappingState": {
            "fillColor": { "property": "iconColor" },
            "iconColor": { "property": "fillColor" },
            "strokeColor": { "property": "fillColor" }
    } } } }
```

### Changing Background Shape

The "shape" property was added in style version [1.4] and can also be applied to "elements".  This example shows a state that, when applied to a map icon, will change the background shape to a teardrop and the foreground to the beach icon.

```json
    { "version": "1.*",
      "extensions": {
        "myNamespace": {
          "myTeardropBeachState": {
            "shape": {
              "background": "teardrop",
              "icon": "beach"
    } } } } }
```

[1.0]: map-style-sheet-support.md
[1.1]: map-style-sheet-support.md
[1.2]: map-style-sheet-support.md
[1.3]: map-style-sheet-support.md
[1.4]: map-style-sheet-support.md
[1.5]: map-style-sheet-support.md
