# hash_xxh3


Computes an XXH3 hash digest.

```tql
hash_xxh3(x:any, [seed=string]) -> string
```

## Description

The `hash_xxh3` function calculates a 64-bit XXH3 hash digest for the given value `x`.

## Examples

### Compute an XXH3 digest of a string

```tql
from {x: hash_xxh3("foo")}
```

```tql
{x: "ab6e5f64077e7d8a"}
```

## See Also

* fn[`hash_md5`](hash_md5.md)
* fn[`hash_sha1`](hash_sha1.md)
* fn[`hash_sha224`](hash_sha224.md)
* fn[`hash_sha256`](hash_sha256.md)
* fn[`hash_sha384`](hash_sha384.md)
* fn[`hash_sha512`](hash_sha512.md)
* fn[`hash_sha3_224`](hash_sha3_224.md)
* fn[`hash_sha3_256`](hash_sha3_256.md)
* fn[`hash_sha3_384`](hash_sha3_384.md)
* fn[`hash_sha3_512`](hash_sha3_512.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)