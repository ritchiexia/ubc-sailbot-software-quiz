# Technical Quiz - UBC Sailbot Software

Using C++ or Python, please write a class, named **AngleCalc** that contains the following methods. Please write accompanying unit tests as well using any framework you desire (e.g. [GoogleTest](https://github.com/google/googletest), [unittest](https://docs.python.org/3/library/unittest.html])). You may use any resources you find but must complete the quiz individually.

1. An autonomous sailing program uses angles between -180 and 179. Create a method with the
following declaration:

```C++
/**
 * Bounds the provided angle between [-180, 180) degrees.
 * Ex. 360 becomes 0, 270 becomes -90, -450 becomes -90.
 * @param angle Input angle in degrees.
 * @return The bounded angle in degrees.
 */
float boundTo180(float angle);
```

2. It's incredibly valuable to be able to determine whether an angle is between two others. Create a method
with the following declaration:

```C++
/**
 * Determines whether |middle_angle| is in the acute angle between the other two bounding angles.
 * Note: Input angles are bounded to 180 for safety.
 * Ex. -180 is between -90 and 110 but not between -90 and 80.
 * @param first_angle First angle in degrees.
 * @param middle_angle Middle angle in degrees.
 * @param second_angle Second angle in degrees.
 * @return Whether |middle_angle| is between |first_angle| and |second_angle| (exclusive).
 */
bool isAngleBetween(float first_angle, float middle_angle, float second_angle);
```

## Submission Instructions
You can either:

1. Push your code to a public repository and send us the repository's link (preferred)
2. Send us your code as a zip file

Please include instructions on how to run your unit tests. 