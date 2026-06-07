# Artifacts generated from ECS

Various kinds of files or programs can be generated directly based on ECS.

In this directory, you'll find the following:

* [beats/fields.ecs.yml](https://github.com/elastic/ecs/blob/354fd8d0ca99faa15405d1ea1d3bb396724d3e5a/generated/beats/fields.ecs.yml): The YAML field definition file
  used by **Beats to import ECS** in it's broader field schema. This might also
  be useful to community Beats maintainers.

* [csv/fields.csv](https://github.com/elastic/ecs/blob/354fd8d0ca99faa15405d1ea1d3bb396724d3e5a/generated/csv/fields.csv): A csv file you can use to import ECS field
  definitions in a **spreadsheet**. GitHub's csv rendering lets you filter
  the fields, too.

* [ecs/\*.yml](https://github.com/elastic/ecs/tree/354fd8d0ca99faa15405d1ea1d3bb396724d3e5a/generated/ecs): These are the files to use when you need to **consume ECS
  programmatically**. The code generating the other ECS artifacts all operate on one
  of these two representations (documentation, csv, Elasticsearch template, etc).
  The two files are the fully fleshed out representation of ECS:
  default values are filled in, all fields being reused elsewhere are made explicit,
  additional attributes are computed.

* [elasticsearch/](https://github.com/elastic/ecs/tree/354fd8d0ca99faa15405d1ea1d3bb396724d3e5a/generated/elasticsearch#readme): Reference Elasticsearch **component templates**
  and a sample legacy all-in-one template to get started using ECS.
  Check out how to use them in [elasticsearch/README.md](https://github.com/elastic/ecs/tree/354fd8d0ca99faa15405d1ea1d3bb396724d3e5a/generated/elasticsearch#readme).
  Note that you can customize the content of these templates by following the
  instructions in [USAGE.md](https://github.com/elastic/ecs/blob/354fd8d0ca99faa15405d1ea1d3bb396724d3e5a/USAGE.md)

If you'd like to share your own generator with the ECS community, you're welcome
to look at our [contribution guidelines](https://github.com/elastic/ecs/blob/354fd8d0ca99faa15405d1ea1d3bb396724d3e5a/CONTRIBUTING.md), and then at the
generators in `scripts/generators`.
