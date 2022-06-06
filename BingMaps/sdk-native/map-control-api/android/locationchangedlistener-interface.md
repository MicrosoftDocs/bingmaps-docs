---
title: LocationChangedListener Interface | Microsoft Docs
description: Describes the LocationChangedListener interface for Android and outlines the onLocationChanged method.
ms.author: krihenri
---

# LocationChangedListener Interface (Android only)

Interface for notifying when a location is being output by [MapLocationProvider](maplocationprovider-class.md).

## Methods

### onLocationChanged

Called when a new [Location](https://developer.android.com/reference/android/location/Location) is being emitted by the MapLocationProvider.

>```java
> void onLocationChanged(android.location.Location location);
>```
