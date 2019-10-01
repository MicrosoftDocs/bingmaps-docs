
# CopyrightDisplay enumeration

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

>``` objectivec
> typedef NS_ENUM(NSInteger, MSCopyrightDisplay)
> {
>     MSCopyrightDisplayAlways,
>     MSCopyrightDisplayAllowHiding
> }
> ```

## Values

### Always

The copyright is always displayed.

### Allow hiding

When the map is 6 inches or smaller in the diagonal the copyright is hidden.