---
title: MapServices Class | Microsoft Docs
description: Describes the MapServices class for Android and iOS and provides the class's static methods and additional references.
ms.author: pablocan
---

# MapServices Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Provides common methods for map services such as [MapLocationFinder](MapLocationFinder-class.md).

## Static Methods

### SetContext (Android only)

Sets the application context for internal infrastructure. Only required for headless use of map services.

>```java
> void setContext(Context applicationContext)
>```

### SetCredentialsKey

Sets user's Bing Maps key which will then be used for API requests.

**Android**

>```java
> void setCredentialsKey(String key)
>```

**iOS**

>```objectivec
> + (void)setCredentialsKey:(NSString*)key
>```

### GetLanguage

Gets the user language for the map control.

**Android**

>```java
> String getLanguage()
>```

**iOS**

>```objectivec
> + (NSString*)getLanguage
>```

### SetLanguage

Sets the user language for the map control.

**Android**

>```java
> void setLanguage(String language)
>```

**iOS**

>```objectivec
> + (void)setLanguage:(NSString*)language
>```

### GetRegion

Gets the user region for the map control.

**Android**

>```java
> String getRegion()
>```

**iOS**

>```objectivec
> + (NSString*)getRegion
>```

### SetRegion

Sets the user region for the map control.

**Android**

>```java
> void setRegion(String region)
>```

**iOS**

>```objectivec
> + (void)setRegion:(NSString*)region
>```

## See Also

* [MapLocationFinder](MapLocationFinder-class.md)
