---
title: Map Style Support | Microsoft Docs
description: Map styling can be applied to a variety of Microsoft map controls, including Bing Maps, Static, Windows, Android, or iOS.
ms.custom: 
ms.date: 05/26/2020
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: ED52C0B4-237D-46B0-8FCB-6D8E9CB8C80C
caps.latest.revision: 3
author: DavidBuerer
ms.author: dbuerer
manager: 
ms.service: bing-maps
---
# Map Style Support

Map styling can be applied to a variety of Microsoft map controls:
* The [Bing Maps web control](../v8-web-control/index.md) using the [customMapStyle option](../v8-web-control/map-control-api/mapoptions-object.md).
* The [Static web map control](../rest-services/imagery/get-a-static-map.md)
* The [Windows map control](/uwp/api/windows.ui.xaml.controls.maps.mapcontrol) using the [MapStyleSheet.ParseFromJson](/uwp/api/windows.ui.xaml.controls.maps.mapstylesheet.parsefromjson#Windows_UI_Xaml_Controls_Maps_MapStyleSheet_ParseFromJson_System_String_) method.
* The [Android or iOS map control](../sdk-native/index.md) using the [MapStyleSheet](../sdk-native/map-control-api/mapstylesheet-class.md) class.

The point at which a particular [entry] or [property] is supported on each map control can be tracked using the style version.  

Map style sheets can be created interactively using the [Map Style Sheet Editor application](https://www.microsoft.com/store/productId/9NBHTCJT72FT).  The editor will inform you of what is supported.

This table shows the minimum version of each control that supports each style version.

| Style Version | Android and iOS | Windows Release                            |
|---------------|-----------------|--------------------------------------------|
|  1.0          |  1.0.0          |  1703 - Creators Update (Build 15063)      |
|  1.1          |  1.0.0          |  1709 - Fall Creators Update (Build 16299) |
|  1.2          |  1.0.0          |  1803 - April 2018 Update (Build 17134)    |
|  1.3          |  1.0.0          |  1809 - October 2018 Update (Build 17763)  |
|  1.4          |  1.0.0          |  1903 - May 2019 Update (Build 18362)      |
|  1.5          |  1.0.0          |                                            |

[entry]: map-style-sheet-entries.md
[property]: map-style-sheet-entry-properties.md