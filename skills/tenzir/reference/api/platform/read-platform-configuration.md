---
title: "Read platform configuration"
description: "Unauthenticated discovery: where this platform serves its API and gateway."
canonical: https://tenzir.com/docs/reference/api/platform/read-platform-configuration
source: https://tenzir.com/docs/reference/api/platform/read-platform-configuration.md
section: "Docs"
---

# Read platform configuration

> Unauthenticated discovery: where this platform serves its API and gateway.

`GET /.well-known/tenzir-platform`

Unauthenticated discovery: where this platform serves its API and gateway.

## Responses

### `200`: What a client needs to reach a platform it only knows the address of: where the API and gateway are, and which keys the requests it sends to a deployment are signed with

Media type: `application/json`

* `apiUrl` (`string`, required)

* `gatewayUrl` (`string`, required)

* `ingestRegions` (`array<string>`, required): The regions that new ingest endpoints may live in, the default first. Only deployments that Tenzir hosts in an endpoint's region may read it. Empty when the platform has one broker that every deployment reaches

* `deploymentKeys` (`Deployment Keys`, required): The JWK set a deployment checks the platform’s requests against. It holds more than one key while a rotation is under way

  * `keys` (`array<Deployment Key>`, required)

    Array items:

    * `kty` (`"OKP"`, required)
    * `crv` (`"Ed25519"`, required)
    * `alg` (`"EdDSA"`, required)
    * `use` (`"sig"`, required)
    * `kid` (`string`, required)
    * `x` (`string`, required)

* `hostedDeployments` (`boolean`, required): Whether the platform can run deployments itself

* `demoOrganization` (`string | null`, optional): A UUID

### `400`: Validation

Media type: `application/json`

* `_tag` (`"Validation"`, required)
* `message` (`string`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
