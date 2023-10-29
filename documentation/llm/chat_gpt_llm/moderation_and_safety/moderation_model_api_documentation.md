# Moderation Model - OpenAI API Documentation

## Overview
OpenAI's Moderation models are tailored to evaluate and classify content based on OpenAI's predefined usage policies. They play an instrumental role in identifying potential policy violations in various categories.

## Capabilities
- **Content Classification**: The models sift through content and classify it under distinct categories:
  - Hate
  - Hate/Threatening
  - Self-Harm
  - Sexual
  - Sexual/Minors
  - Violence
  - Violence/Graphic
- **Token Management**: For extensive content, the models automatically segment the input into 4,096-token chunks. For content exceeding 32,768 tokens, truncation comes into play, potentially excluding a minimal number of tokens from evaluation.
- **Result Interpretation**: The API response displays the maximum value observed across categories. For instance, if a 4K-token chunk registers a category score of 0.9901 and another scores 0.1901, the higher value, 0.9901, is reflected in the API outcome.

## Models
- **text-moderation-latest**: This model stands as the pinnacle of moderation capabilities, offering marginally higher accuracy than its stable counterpart. It can accommodate up to 32,768 tokens.
- **text-moderation-stable**: Though slightly dated, this model's capabilities are nearly on par with the latest version. It also supports up to 32,768 tokens.

## Additional Resources
For an in-depth understanding of the Moderation models and their application, refer to the [moderation guide](#).

