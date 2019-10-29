---
title: "MapUriTileMapLayer Class | Microsoft Docs"
author: "bmnxplat"
---
 
# MapUriTileMapLayer Class

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

The URI format template to use.  See [this article](http://msdn.microsoft.com/en-us/library/windowsphone/develop/windows.ui.xaml.controls.maps.httpmaptiledatasource.uriformatstring.aspx) for acceptable tokens that get replaced.

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