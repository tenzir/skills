# ECS categorization fields [ecs-category-field-values-reference]

At a high level, ECS provides fields to classify events in two different ways: "Where it’s from" (e.g., `event.module`, `event.dataset`, `agent.type`, `observer.type`, etc.), and "What it is." The categorization fields hold the "What it is" information, independent of the source of the events.

ECS defines four categorization fields for this purpose, each of which falls under the `event.*` field set.

## Categorization fields [ecs-category-fields]

* [event.kind](../categorization.yaml)
* [event.category](../categorization.yaml)
* [event.type](../categorization.yaml)
* [event.outcome](../categorization.yaml)

::::{note}
If your events don’t match any of these categorization values, you should leave the fields empty. This will ensure you can start populating the fields once the appropriate categorization values are published, in a later release.
::::

## Categorization usage [ecs-category-usage]

[Using the categorization fields](categorization-usage.md) contains examples combining the categorization fields to classify different types of events.
