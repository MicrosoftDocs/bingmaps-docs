---
title: MapUriTileMapLayer Class | Microsoft Docs
description: Describes the MapUriTileMapLayer class for Android and iOS and provides the class's properties and additional references.
ms.author: pablocan
---

# MapUriTileMapLayer Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Display tiles based on developer-supplied URLs.

**Android**

>```java
> class UriTileMapLayer extends MapLayer
>```

**iOS**

>```objectivec
> @interface MSMapUriTileMapLayer : MSMapLayer
>```

## Properties

### UriFormatString

The URI format template to use.  See [this article](https://msdn.microsoft.com/library/windowsphone/develop/windows.ui.xaml.controls.maps.httpmaptiledatasource.uriformatstring.aspx) for acceptable tokens that get replaced.

**Android**

>```java
> string getUriFormatString()
> void setUriFormatString(string uriFormatString)
>```

**iOS**

>```objectivec
> @property (nonatomic) NSString *uriFormatString
>```

## See Also

[MapLayer](MapLayer-class.md)