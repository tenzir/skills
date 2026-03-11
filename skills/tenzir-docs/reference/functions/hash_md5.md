# hash_md5


Computes an MD5 hash digest.

```tql
hash_md5(x:any, [seed=string])
```

## Description

The `hash` function calculates a hash digest of a given value `x`.

### `x: any`

The value to hash.

### `seed = string (optional)`

The seed for the hash.

## Examples

### Compute an MD5 digest of a string

```tql
from { x: hash_md5("foo") }
```

```tql
{ x: "acbd18db4cc2f85cedef654fccc4a4d8" }
```

## See Also

* fn[`hash_sha1`](/reference/functions/hash_sha1.md)
* fn[`hash_sha224`](/reference/functions/hash_sha224.md)
* fn[`hash_sha256`](/reference/functions/hash_sha256.md)
* fn[`hash_sha512`](/reference/functions/hash_sha512.md)
* fn[`hash_sha384`](/reference/functions/hash_sha384.md)
* fn[`hash_sha3_224`](/reference/functions/hash_sha3_224.md)
* fn[`hash_sha3_256`](/reference/functions/hash_sha3_256.md)
* fn[`hash_sha3_384`](/reference/functions/hash_sha3_384.md)
* fn[`hash_sha3_512`](/reference/functions/hash_sha3_512.md)
* fn[`hash_xxh3`](/reference/functions/hash_xxh3.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)