---
title: "Color Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7d5d713d-3595-42aa-8181-38889cc0e4cb
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Color Class

Creating an instance of the Color class can be done in one of two ways. The first is to specify values for all the properties in the constructor. The second is to use the static method fromHex which parses a string Hex color value into a Bing Maps Color. The following code shows how these two methods can be used to create a Location objects.

**Note:** In addition to using the Color class to specify the color of a shape in Bing Maps, [CSS3 color strings](../map-control-concepts/colors.md) can also be used. 
 
## Constructor

>  `Color(a: number, r:number, g:number, b:number)`


## Properties

The Color class has four properties; a (alpha), r (red), g (green), b (blue) and are defined as follows. 

Name         | Type             | Description
------------ | ---------------- | ----------------------
`a`           | number           | The opacity of the color. The range of valid values is a decimal value between 0 and 1. If a value between 1 and 255 is specified, as was done in Bing Maps V7, it will be divided by 255.
`r`           | number           | The red value of the color. The range of valid values is 0 to 255.
`g`           | number           | The green value of the color. The range of valid values is 0 to 255.
`b`           | number           | The blue value of the color. The range of valid values is 0 to 255.

## Methods

The Color class has the following methods available.

Name             | Return Type	| Description
---------------- | -------------- | ---------------------
`clone()`        | Color          | Returns a copy of the Color object.
`getOpacity()`   | number         | Returns the opacity of the Color as a value between 0 (a=0) and 1 (a=255).
`toHex()`        | string         | Converts the Color into a 6-digit hex string. Opacity is ignored. For example, a Color with values (255,0,0,0) is returned as hex string #000000.
`toRgba()`       | string         | Converts the Color into a RGBA color string. For example: rgba(0, 255, 0, 0.5) 

## Static Methods

The Color class has the following static methods available.

Name                       | Return Type    | Description
-------------------------- | -------------- | ------------------------------------
`clone(color: Color)`      | Color          | Creates a copy of the Color object.
`fromHex(hex:string)`      | Color          | Converts the specified hex string to a Color.

## Example

```javascript
var color = new Microsoft.Maps.Color(150, 0, 255, 0);
```

```javascript
//From a string Hex color
var color = Microsoft.Maps.Color.fromHex('#00FF00');
```