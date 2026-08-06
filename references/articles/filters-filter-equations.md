---
title: "Equations filter - Affinity Help Center"
source: https://www.affinity.studio/help/filters-filter-equations/
slug: filters-filter-equations
fetched: 2026-08-06
---

# Equations filter - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/filters-filter-equations/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Equations filter

The Equations filter applies geometric transformations to a pixel layer by evaluating mathematical expressions you define.

![Image 1: A pixel layer after applying an Equations filter expression.](https://images.ctfassets.net/3p2fxa94bzao/32L4s8GXjC2cEWQg5YTcMr/2943546c9445fb1d85c9f940289eeb84/filter_equations_after.jpg)

A pixel layer after applying an Equations filter expression.

![Image 2: The original pixel layer before the Equations filter is applied.](https://images.ctfassets.net/3p2fxa94bzao/y1il4mp7hBR0QbrmQif7r/0b65cd618ce5acfa270b2ce5c37e54e5/filter_equations_before.jpg)

The original pixel layer before the Equations filter is applied.

The Equations filter applies geometric transformations to a pixel layer by evaluating mathematical expressions you write directly in the filter dialog. Using built-in coordinate variables alongside trigonometric, exponential, and arithmetic functions, you can produce a wide range of distortion effects — from simple offsets and reflections to complex warps. Custom variables **a**, **b**, and **c** are also available, with their values controlled by sliders for real-time adjustment.

The filter is accessible via **Pixel > Filters > Distort > Equations**.

Equations is also available as a tool (Equation Transform) in the Compositing Studio

![Image 3](https://images.ctfassets.net/3p2fxa94bzao/3HLsf5xx2FlnBTmx7VwAkX/eb93eb77aa0dc236a5edfe2d6e7ef9f7/compositing_studio.svg)

.

*   The following variables and functions are available when writing expressions:

*   **x**, **y**—pixel coordinates along the X and Y axes (Cartesian mode).
*   **r**—radial distance from the center of the image (Polar mode).
*   **t**—angle in radians (theta) from the center of the image (Polar mode).
*   **w**, **h**—width and height of the layer in pixels.
*   **a**, **b**, **c**—custom parameters controlled by the Parameter sliders.

*   **+**, **-**, *****, **/**—addition, subtraction, multiplication, and division.
*   **^**—exponentiation.
*   **%**—modulo (remainder after division).

*   **sin()**, **cos()**, **tan()**—trigonometric functions; input in radians.
*   **asin()**, **acos()**, **atan()**—inverse trigonometric functions.
*   **sqrt()**—square root.
*   **abs()**—absolute value.
*   **floor()**, **ceil()**, **round()**—round down, round up, or round to nearest integer.
*   **log()**, **exp()**—natural logarithm and e raised to the power of the argument.
*   **min()**, **max()**—return the smaller or larger of two values.
*   **pow()**—raise a value to a specified power.

*   **pi**—π (approximately 3.14159).
*   **e**—Euler's number (approximately 2.71828).

The following settings can be adjusted in the filter dialog:

*   **Coordinate System**—choose from Cartesian or Polar coordinates.
*   **Cartesian**
    *   **x =**—enter an expression for the X-axis.
    *   **y =**—enter an expression for the Y-axis.

*   **Polar**
    *   **r =**—enter an expression for the radius.
    *   **t =**—enter an expression for the polar angle (theta).

*   **Parameter A (a)**—controls the value of custom variable **a**.
*   **Parameter B (b)**—controls the value of custom variable **b**.
*   **Parameter C (c)**—controls the value of custom variable **c**.
*   **Extend Mode**—chooses how to treat pixels outside of the image bounds:
    *   **Zero**—fills pixels outside the image bounds with zeros (alpha values).
    *   **Full**—fills pixels outside the image bounds with constant values (pure white).
    *   **Repeat**—fills pixels outside the image bounds with repetitions of the image's edge pixels.
    *   **Wrap**—fills pixels outside the image bounds with copies of the image; useful for positional offset filters and seamless texture authoring.
    *   **Mirror**—fills pixels outside the image bounds with mirrored (reflected) copies of the image.

1.   In the **Layers**panel, select the pixel layer you want to transform.
2.   On the **Pixel**menu, choose **Filters > Distort > Equations**.
3.   In the filter dialog, set the **Coordinate System**to **Cartesian**or **Polar**.
4.   Enter expressions in the available fields (**x**and **y**for Cartesian, or **r**and **t**for Polar).
5.   If your expressions use the custom variables **a**, **b**, or **c**, adjust the Parameter sliders to set their values.
6.   Set **Extend Mode**to control how pixels outside the image bounds are handled.
7.   Click **Apply**.

*   [Expressions for field input](https://www.affinity.studio/help/workspace-expressions/)
*   [Applying filters](https://www.affinity.studio/help/filters-filters-applying/)
*   [Procedural Texture filter](https://www.affinity.studio/help/filters-filter-proceduraltexture/)
*   [Custom Blur filter](https://www.affinity.studio/help/filters-filter-custom-blur/)
*   [Compositing Studio](https://www.affinity.studio/help/workspace-compositing-studio/)

How would you rate the help you received from this article?
