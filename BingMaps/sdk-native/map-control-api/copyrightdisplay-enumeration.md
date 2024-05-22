---
title: CopyrightDisplay Enumeration | Microsoft Docs
description: Describes the CopyrightDisplay enumeration for Android and iOS and provides the enumeration's always and allow hiding values.
ms.author: pablocan
---

# CopyrightDisplay Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Controls the display of the copyright on the Map.

**Android**

>```java
> public enum CopyrightDisplay
> {
>      ALWAYS,
>      ALLOW_HIDING
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSCopyrightDisplay)
> {
>     MSCopyrightDisplayAlways,
>     MSCopyrightDisplayAllowHiding
> }
>```

## Values

### Always

The copyright is always displayed.

### Allow hiding

When the map is 6 inches or smaller in the diagonal the copyright is hidden.