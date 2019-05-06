
# MapAnimationKind enumeration

Specifies the animation to use when you change the view of the map. For example, you can specify animation when calling setScene and beginSetScene.

**Android**

>```java
> public enum MapAnimationKind
> {
>      DEFAULT,
>      NONE,
>      LINEAR,
>      BOW
> }
>```


**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapAnimationKind)
> {
>      MSMapAnimationKindDefault = 0,
>      MSMapAnimationKindNone,
>      MSMapAnimationKindLinear,
> }
> ```

## Values

### Default

Default animation. This will do linear animations if close, parabolic animations if distant)
For Android, see [DefaultMapCameraAnimation](Android/DefaultMapCameraAnimation-class.md).)

### None

No animation is used.

### Linear

A linear shift is made to the destination view.

### Bow

A "jump" animation to the new destination
