---
title: TrafficIncidentSeverity Enumeration | Microsoft Docs
description: Describes the TrafficIncidentSeverity enumeration for Android and iOS and provides the enumeration's syntax and additional references.
ms.author: pablocan
---

# TrafficIncidentSeverity Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Specifies the severity of traffic incident.

**Android**

>```java
> public enum TrafficIncidentSeverity {
>   LOW_IMPACT,
>   MINOR,
>   MODERATE,
>   SERIOUS
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapTrafficIncidentSeverity) {
>   MSMapTrafficIncidentSeverityLowImpact,
>   MSMapTrafficIncidentSeverityMinor,
>   MSMapTrafficIncidentSeverityModerate,
>   MSMapTrafficIncidentSeveritySerious
> }
>```

## See Also

* [TrafficIncident](TrafficIncident-class.md)