# hash_sha3_384


Computes a SHA3-384 hash digest.

```tql
hash_sha3_384(x:any, [seed=string]) -> string
```

## Description

The `hash_sha3_384` function calculates a SHA3-384 hash digest for the given value `x`.

## Examples

### Compute a SHA3-384 digest of a string

```tql
from {x: hash_sha3_384("foo")}
```

```tql
{x: "665551928d13b7d84ee02734502b018d896a0fb87eed5adb4c87ba91bbd6489410e11b0fbcc06ed7d0ebad559e5d3bb5"}
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
* fn[`hash_sha3_512`](hash_sha3_512.md)
* fn[`hash_xxh3`](hash_xxh3.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)