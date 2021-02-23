---
title: "ManeuverWarningSeverity Enumeration | Microsoft Docs"
ms.author: "kezhang"
---

# ManeuverWarningSeverity Enumeration

Represents the severity of potential issue along a route leg.

**Android**

>```java
>public enum ManeuverWarningSeverity {
>  NONE(0),
>  LOW_IMPACT(1),
>  MINOR(2),
>  MODERATE(3),
>  SERIOUS(4);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapManeuverWarningSeverity) {
>    MSMapManeuverWarningSeverityNone = 0,
>    MSMapManeuverWarningSeverityLowImpact,
>    MSMapManeuverWarningSeverityMinor,
>    MSMapManeuverWarningSeverityModerate,
>    MSMapManeuverWarningSeveritySerious
>};
>```

## Values

### None

The issue has no impact.

### LowImpact

The issue has a low impact.

### Minor

The issue has a minor level impact.

### Moderate

The issue has a moderate level of impact.

### Serious

The issue has a high level of impact.

## See Also

* [ManeuverWarning](maneuverwarning-class.md)
* [ManeuverWarningKind](maneuverwarningkind-enumeration.md)