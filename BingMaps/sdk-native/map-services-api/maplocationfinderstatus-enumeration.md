---
title: MapLocationFinderStatus Enumeration | Microsoft Docs
description: Describes the MapLocationFinderStatus enumeration for Android and iOS and provides the enumeration's values and additional references.
ms.author: pablocan
---

# MapLocationFinderStatus Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Represents the status of a completed geocoding request.

**Android**

>```java
>public enum MapLocationFinderStatus
>{
>    SUCCESS(0),
>    CANCEL(1),
>    BAD_RESPONSE(2),
>    INVALID_CREDENTIALS(3),
>    NETWORK_FAILURE(4),
>    SERVER_ERROR(5),
>    UNKNOWN_ERROR(6),
>    EMPTY_RESPONSE(7);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapLocationFinderStatus)
>{
>    MSMapLocationFinderStatusSuccess = 0,
>    MSMapLocationFinderStatusCancel = 1,
>    MSMapLocationFinderStatusBadResponse = 2,
>    MSMapLocationFinderStatusInvalidCredentials = 3,
>    MSMapLocationFinderStatusNetworkFailure = 4,
>    MSMapLocationFinderStatusServerError = 5,
>    MSMapLocationFinderStatusUnknownError = 6,
>    MSMapLocationFinderStatusEmptyResponse = 7
>};
>```

## Values

### Success

The request completed successfully.

### Cancel

The request was cancelled by the user.

### BadResponse

A fatal parsing error has occured while processing the response.

### InvalidCredentials

The credentials provided for the request were not valid.

### NetworkFailure

A network failure has occured while processing the request.

### ServerError

A server error has occured while processing the request.

### UnknownError

An unknown error has occured while processing the request.

### EmptyResponse

The request succeeded but the response was empty.

## See Also

* [MapLocationFinderResult](MapLocationFinderResult-class.md)
