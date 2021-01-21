---
title: "ManeuverWarning Class | Microsoft Docs"
ms.author: "kezhang"
---

# ManeuverWarning Class

Represents a potential issue along a route leg.

## Properties

### WarningKind

Gets the warning type of potential issue along a route leg.

_See also:_ [ManeuverWarningKind](maneuverwarningkind-enumeration.md)

**Android**

>```java
>ManeuverWarningKind getKind()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSMapManeuverWarningKind kind;
>```

### WarningSeverity

Gets the severity of a potential issue along a route leg.

_See also:_ [ManeuverWarningSeverity](maneuverwarningseverity-enumeration.md)

**Android**

>```java
>ManeuverWarningSeverity getSeverity()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSMapManeuverWarningSeverity severity;
>```

## See Also

* [MapRouteManeuver](maproutemaneuver-class.md)