---
title: "Overview"
description: "Limit sensitive-data exposure while preserving useful structure."
canonical: https://tenzir.com/docs/v7.0.0/guides/protect
source: https://tenzir.com/docs/v7.0.0/guides/protect.md
section: "Docs"
---

# Overview

> Limit sensitive-data exposure while preserving useful structure.

Protection limits sensitive-data exposure before events leave a trust boundary. Depending on the use case, you can anonymize values irreversibly, replace them with stable pseudonyms, or encrypt them for controlled recovery.

Our guide on [masking sensitive data](protect/mask-sensitive-data.md) covers redaction, hashing, pseudonymization, and prefix-preserving IP address encryption.

Our guide on [encrypting sensitive data](protect/encrypt-sensitive-data.md) covers reversible encryption: managing keys, encrypting and decrypting fields, keeping equal values comparable, preserving value formats, and encrypting with a public key so that only the holder of the private key can decrypt.
