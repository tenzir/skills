---
title: "hash_sha1"
canonical: https://tenzir.com/docs/reference/functions/hash_sha1
source: https://tenzir.com/docs/reference/functions/hash_sha1.md
section: "Docs"
---

# hash_sha1

> Computes a SHA-1 hash digest.

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

* [`hash_crc32`](hash_crc32.md)
* [`hash_md5`](hash_md5.md)
* [`hash_sha224`](hash_sha224.md)
* [`hash_sha256`](hash_sha256.md)
* [`hash_sha384`](hash_sha384.md)
* [`hash_sha512`](hash_sha512.md)
* [`hash_sha3_224`](hash_sha3_224.md)
* [`hash_sha3_256`](hash_sha3_256.md)
* [`hash_sha3_384`](hash_sha3_384.md)
* [`hash_sha3_512`](hash_sha3_512.md)
* [`hash_xxh3`](hash_xxh3.md)
* [Manipulate strings](../../guides/shape/manipulate-strings.md)
