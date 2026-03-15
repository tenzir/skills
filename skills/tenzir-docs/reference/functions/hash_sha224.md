# hash_sha224


Computes a SHA-224 hash digest.

```tql
hash_sha224(x:any, [seed=string]) -> string
```

## Description

The `hash_sha224` function calculates a SHA-224 hash digest for the given value `x`.

## Examples

### Compute a SHA-224 digest of a string

```tql
from {x: hash_sha224("foo")}
```

```tql
{x: "0808f64e60d58979fcb676c96ec938270dea42445aeefcd3a4e6f8db"}
```

## See Also

* [`hash_md5`](/reference/functions/hash_md5.md)
* [`hash_sha1`](/reference/functions/hash_sha1.md)
* [`hash_sha256`](/reference/functions/hash_sha256.md)
* [`hash_sha384`](/reference/functions/hash_sha384.md)
* [`hash_sha512`](/reference/functions/hash_sha512.md)
* [`hash_sha3_224`](/reference/functions/hash_sha3_224.md)
* [`hash_sha3_256`](/reference/functions/hash_sha3_256.md)
* [`hash_sha3_384`](/reference/functions/hash_sha3_384.md)
* [`hash_sha3_512`](/reference/functions/hash_sha3_512.md)
* [`hash_xxh3`](/reference/functions/hash_xxh3.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)