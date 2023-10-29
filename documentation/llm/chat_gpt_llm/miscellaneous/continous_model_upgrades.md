# Continuous Model Upgrades by OpenAI

OpenAI adopts a dynamic approach to its model upgrades, ensuring developers always have access to the most optimized versions. This commitment to enhancement and adaptation is rooted in continuous feedback from the developer community.

---

## Extended Support for Select Models

In response to developer feedback, OpenAI has confirmed extended support for certain models in the API. Specifically:

- **gpt-3.5-turbo-0301**
- **gpt-4-0314**

These models will receive support until at least June 13, 2024. The details regarding this extension can be found in OpenAI's updated June 13 blog post.

---

## Continual Updates & Static Versions

OpenAI introduced a significant shift with the release of gpt-3.5-turbo. Now, some models, such as gpt-3.5-turbo, gpt-4, and gpt-4-32k, are under continuous updates. Developers can ascertain the exact version of the model used by analyzing the response object from a ChatCompletion request.

For those preferring consistent model behavior, OpenAI provides static model versions, which will remain unchanged for a minimum of three months post the introduction of an updated model. This combination of continual updates and static versions offers developers flexibility based on their specific needs.

---

## Model Contribution & Temporary Snapshots

OpenAI's commitment to enhancement extends to the broader developer community. The organization has provided mechanisms for individuals to contribute evals, directly influencing model improvements for diverse applications. The OpenAI Evals repository is the gateway for such contributions.

It's noteworthy that some models are temporary snapshots. Their deprecation dates will be announced once newer versions are available:

- **gpt-3.5-turbo-0301** (Discontinuation by June 13, 2024 at the earliest) - Replacement: gpt-3.5-turbo-0613
- **gpt-4-0314** (Discontinuation by June 13, 2024 at the earliest) - Replacement: gpt-4-0613
- **gpt-4-32k-0314** (Discontinuation by June 13, 2024 at the earliest) - Replacement: gpt-4-32k-0613

For a comprehensive understanding of model deprecation and its implications, refer to OpenAI's deprecation page.

