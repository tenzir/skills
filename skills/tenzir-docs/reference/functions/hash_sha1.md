# hash_sha1


Computes a SHA-1 hash digest.

```tql
hash_sha1(x:any, [seed=string]) -> string
```

## Description

The `hash_sha1` function calculates a SHA-1 hash digest for the given value `x`.

## Examples

### Compute a SHA-1 digest of a string

```tql
from {x: hash_sha1("foo")}
```

```tql
{x: "0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33"}
```

## See Also

* fn[`hash_md5`](/reference/functions/hash_md5.md)
* fn[`hash_sha224`](/reference/functions/hash_sha224.md)
* fn[`hash_sha256`](/reference/functions/hash_sha256.md)
* fn[`hash_sha384`](/reference/functions/hash_sha384.md)
* fn[`hash_sha512`](/reference/functions/hash_sha512.md)
* fn[`hash_sha3_224`](/reference/functions/hash_sha3_224.md)
* fn[`hash_sha3_256`](/reference/functions/hash_sha3_256.md)
* fn[`hash_sha3_384`](/reference/functions/hash_sha3_384.md)
* fn[`hash_sha3_512`](/reference/functions/hash_sha3_512.md)
* fn[`hash_xxh3`](/reference/functions/hash_xxh3.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)