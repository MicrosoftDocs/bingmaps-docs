---
title: "AmbientLightDetection Enumeration | Microsoft Docs"
description: "AmbientLightDetection Enumeration | Microsoft Docs"
ms.author: "krihenri"
ms.author: "krihenri"
---

# AmbientLightDetection Enumeration

Controls whether MapView will automatically monitor the ambient light sensor and toggle between light and dark map styles.

**Android**

>```java
> enum AmbientLightDetection
> {
>   DISABLED,
>   AUTOMATIC
> }
>```

**iOS**

Not available.

## Values

### Disabled

MapView will not monitor ambient light changes or change the map style.

### Automatic

MapView will automatically switch between light and dark map styles based on ambient light sensors.
