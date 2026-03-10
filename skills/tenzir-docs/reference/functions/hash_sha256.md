# hash_sha256


Computes a SHA-256 hash digest.

```tql
hash_sha256(x:any, [seed=string]) -> string
```

## Description

The `hash_sha256` function calculates a SHA-256 hash digest for the given value `x`.

## Examples

### Compute a SHA-256 digest of a string

```tql
from {x: hash_sha256("foo")}
```

```tql
{x: "2c26b46b68ffc68ff99b453c1d30413413422e6e6c8ee90c3abeac38044e8a8c1b0"}
```

## See Also

* fn[`hash_md5`](hash_md5.md)
* fn[`hash_sha1`](hash_sha1.md)
* fn[`hash_sha224`](hash_sha224.md)
* fn[`hash_sha384`](hash_sha384.md)
* fn[`hash_sha512`](hash_sha512.md)
* fn[`hash_sha3_224`](hash_sha3_224.md)
* fn[`hash_sha3_256`](hash_sha3_256.md)
* fn[`hash_sha3_384`](hash_sha3_384.md)
* fn[`hash_sha3_512`](hash_sha3_512.md)
* fn[`hash_xxh3`](hash_xxh3.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)