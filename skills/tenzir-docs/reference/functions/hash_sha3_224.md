# hash_sha3_224


Computes a SHA3-224 hash digest.

```tql
hash_sha3_224(x:any, [seed=string]) -> string
```

## Description

The `hash_sha3_224` function calculates a SHA3-224 hash digest for the given value `x`.

## Examples

### Compute a SHA3-224 digest of a string

```tql
from {x: hash_sha3_224("foo")}
```

```tql
{x: "f4f6779e153c391bbd29c95e72b0708e39d9166c7cea51d1f10ef58a"}
```

## See Also

* fn[`hash_md5`](hash_md5.md)
* fn[`hash_sha1`](hash_sha1.md)
* fn[`hash_sha224`](hash_sha224.md)
* fn[`hash_sha256`](hash_sha256.md)
* fn[`hash_sha384`](hash_sha384.md)
* fn[`hash_sha512`](hash_sha512.md)
* fn[`hash_sha3_256`](hash_sha3_256.md)
* fn[`hash_sha3_384`](hash_sha3_384.md)
* fn[`hash_sha3_512`](hash_sha3_512.md)
* fn[`hash_xxh3`](hash_xxh3.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)