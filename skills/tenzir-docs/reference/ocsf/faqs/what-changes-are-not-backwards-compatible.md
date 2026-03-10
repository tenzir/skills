# What changes are not backwards compatible?

> OCSF FAQ: What changes are not backwards compatible?


1. The removal of an event, object, attribute, data type, or enum member.

   1. The `name` of an event or object is missing in the NEW schema.
   2. The dictionary key of an attribute or data type (its implied `name`) is missing in the NEW schema.
   3. The dictionary key of an enum member (its value) is missing in the NEW schema.
   4. The `uid` or `class_uid` of an event is missing in the NEW schema.

2. Renaming an event, object, attribute, or enum member.
   1. A special case of removal in which the same `caption` belongs to an element with a different `name`, key, or `class_uid`; or the same `class_uid` belongs to an event with a different name.

3. Changing the data type of an attribute **unless**:

   1. The data type is changing from `int` to `long`. This exception is allowed on the basis that *nearly* all encodings use variable lengths by default, meaning that data written in nearly all encodings as an `int` can be safely interpreted as a `long`.
   2. Changing a scalar type when the underlying type (e.g. `string_t`) remains the same and there are no constraints on the new type.

4. Changing the `requirement` value of an attribute from `optional` or `recommended` to `required`.

5. Making the `constraints` of a data type more restrictive.

6. Adding a `required` attribute to an existing event or object.

7. Changing the `caption` of an event, enum member, or category.