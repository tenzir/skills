# hash_sha3_512


Computes a SHA3-512 hash digest.

```tql
hash_sha3_512(x:any, [seed=string]) -> string
```

## Description

The `hash_sha3_512` function calculates a SHA3-512 hash digest for the given value `x`.

## Examples

### Compute a SHA3-512 digest of a string

```tql
from {x: hash_sha3_512("foo")}
```

```tql
{x: "4bca2b137edc580fe50a88983ef860ebaca36c857b1f492839d6d7392452a63c82cbebc68e3b70a2a1480b4bb5d437a7cba6ecf9d89f9ff3ccd14cd6146ea7e7"}
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
* fn[`hash_xxh3`](hash_xxh3.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)