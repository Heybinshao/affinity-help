---
title: "Using regular expressions - Affinity Help Center"
source: https://www.affinity.studio/help/extras-regex/
slug: extras-regex
fetched: 2026-08-06
---

# Using regular expressions - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/extras-regex/

1.   [Help Center](https://www.affinity.studio/help/)
2.   Using regular expressions

Affinity supports the use of regular expressions to find document content that matches specified patterns. Regular expressions are widely used in word processing and DTP.

Regular expressions are used in several contexts in Affinity:

*   To find (and optionally replace) document text that matches a pattern.
*   To toggle the visibility of layers whose names match a pattern (via the **States** panel).
*   To perform calculations in fields. See [Field input](https://www.affinity.studio/help/workspace-field-input/) and [Expressions in field input](https://www.affinity.studio/help/workspace-expressions/) for more information, including examples.

Regular expressions use special syntax to specify patterns. The examples below demonstrate common syntax you can use to write your own expressions.

A comprehensive guide to the full power of regular expressions is beyond the scope of Affinity Help. Learn more from online resources such as www.regular-expressions.info and regexone.com.

The States panel is case sensitive unless your expression explicitly states otherwise.

The Find and Replace panel is case sensitive when the **Match Case** option is enabled.

On each panel, case can be ignored for part or all of an expression:

*   Ignore the case of a specific character by using a character class. For example, _[aA]_ or _[a-eA-E]_ to match the letter _a_ or all letters from _a_ to _e_.
*   Ignore the case of all letters by starting an expression with _(?i)_. For example, _(?i)internet_ will match both _Internet_ and _internet_.

In an Affinity document, some layers are named _Dust removal_ or _Blemish removal_. To simplify layer management, we want to control their visibility simultaneously.

On the States panel, add this query: _(?i)(Dust|Blemish) removal_. This matches any layer name where _Dust_ or _Blemish_ is followed by _removal_, ignoring capitalization.

To toggle matching layers' visibility, click the query's **Hide** or **Show** button.

In a document, we've used the layer name _offset fill_ to identify layers that were manually repositioned to create a handmade misprinted effect.

In some cases, the words may appear in reverse order.

On the States panel, add this query: _(?i)(?=.*offset)(?=.*fill).*$_. This matches any layer name containing both _offset_ and _fill_, in any order or position, ignoring capitalization.

In a CAD architectural design document, layer names identify building components using a two-letter prefix, followed by one or more groups of an underscore followed by some digits. For example, _Ss-35\_10\_15_.

On the States panel, you can control the visibility of layers belonging to a specific component category using an expression like _[Ss][Ss](\_[0-9]{1,})+_. This matches names that begin with two S characters (regardless of letter case), followed by numeric groups.

To control the visibility of layers from all other component categories, modify the expression slightly: _(^[Ss][Ss])(\_[0-9]{1,})+_. The caret (^) ensures the match occurs only at the start of the layer name.

We want to find all instances of a specific word in text, but exclude those that are directly preceded by another word.

With **Regular Expression** enabled in the Find and Replace panel's formatting options, you can use a 'negative lookbehind' to achieve this.

For example: _(?<!proin )aliquam_ will match all occurrences of _aliquam_ except those immediately preceded by _proin_ and a space.

You can also exclude matches preceded by any one of several words. For example, to exclude instances of _error_ when it's preceded by either _the_ or _an_, use: _(?<!(the|an) )error_.

*   [Layer states](https://www.affinity.studio/help/object-control-layer-states/)
*   [Find and replace](https://www.affinity.studio/help/text-find-and-replace/)

How would you rate the help you received from this article?
