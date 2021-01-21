---
title: "TrafficIncidentSeverity Enumeration | Microsoft Docs"
ms.author: "pablocan"
---

# TrafficIncidentSeverity Enumeration

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