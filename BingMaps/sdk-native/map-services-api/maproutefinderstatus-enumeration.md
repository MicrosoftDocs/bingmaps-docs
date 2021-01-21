---
title: "MapRouteFinderStatus Enumeration | Microsoft Docs"
author: "kezhang"
---

# MapRouteFinderStatus Enumeration

Returns the status of a MapRouteFinder query. This enumeration provides values for the Status property of a MapRouteFinderResult.

**Android**

>```java
>public enum MapRouteFinderStatus {
>  SUCCESS(0),
>  UNKNOWN_ERROR(1),
>  INVALID_CREDENTIALS(2),
>  NO_ROUTE_FOUND(3),
>  NO_ROUTE_FOUND_WITH_GIVEN_OPTIONS(4),
>  ROUTE_RESULT_VIOLATES_OPTIONS (5),
>  START_POINT_NOT_FOUND(6),
>  END_POINT_NOT_FOUND(7),
>  NO_PEDESTRIAN_ROUTE_FOUND(8),
>  NETWORK_FAILURE(9),
>  NOT_SUPPORTED(10);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapRouteFinderStatus) {
>    MSMapRouteFinderStatusSuccess = 0,
>    MSMapRouteFinderStatusUnkonwnError,
>    MSMapRouteFinderStatusInvalidCredentials,
>    MSMapRouteFinderStatusNoRouteFound,
>    MSMapRouteFinderStatusNoRouteFoundWithGivenOptions,
>    MSMapRouteFinderStatusStartPointNotFound,
>    MSMapRouteFinderStatusEndPointNotFound,
>    MSMapRouteFinderStatusNoPedestrianRouteFound,
>    MSMapRouteFinderStatusNetworkFailure,
>    MSMapRouteFinderStatusNotSupported
>};
>```

## Values

### Success

The query was successful.

### UnknownError

The query returned an unknown error.

### InvalidCredentials

The query provided credentials that are not valid.

### NoRouteFound

The query did not find a route.

### NoRouteFoundWithGivenOptions

The query did not find a route with the specified options.

### RouteResultViolatesOptions

The route result violates the specified options.

### StartPointNotFound

The specified starting point is not valid in a route. For example, the point is in an ocean or a desert.

### EndPointNotFound

The specified ending point is not valid in a route. For example, the point is in an ocean or a desert.

### NoPedestrainRouteFound

The query did not find a pedestrian route.

### NetworkFailure

The query encountered a network failure.

### NotSupported

The query is not supported.

## See Also

* [MapRouteFinder](maproutefinder-class.md)
* [MapRouteFinderResult](maproutefinderresult-class.md)
* [OnMapRouteFinderResultListener](Android/onmaproutefinderresultlistener-interface.md)
* [MSMapRoutingCompletionBlock](iOS/maproutingcompletionblock-interface.md)