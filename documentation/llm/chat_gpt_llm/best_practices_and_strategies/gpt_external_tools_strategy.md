# Strategy: Use External Tools

## Tactic: Use Embeddings-based Search for Efficient Knowledge Retrieval

**Description**:
Leveraging external sources of information as part of a model's input can greatly enhance its ability to produce informed and up-to-date responses. For instance, when queried about a particular movie, incorporating high-quality details about the film (actors, director, etc.) into the model’s input can yield more insightful outputs. To dynamically introduce pertinent information into the model's input at runtime, embeddings can be utilized to ensure efficient knowledge retrieval.

### What is a Text Embedding?
A text embedding is a vector representation that captures the semantic essence of text strings. Text strings that are related or similar will have closer embeddings compared to unrelated strings. The proximity of embeddings, coupled with the availability of swift vector search algorithms, enables embeddings to be a powerful tool for efficient knowledge retrieval.

### How to Implement Knowledge Retrieval using Embeddings?
1. **Chunking the Text Corpus**: Divide the text corpus into manageable chunks.
2. **Embedding the Chunks**: Convert each chunk into its embedding representation and store it.
3. **Embedding the Query**: Transform the given query into its embedding.
4. **Vector Search**: Execute a vector search to find the stored text chunk embeddings that are most related to the query's embedding (i.e., closest in the embedding space).

For practical implementations, refer to the [OpenAI Cookbook](https://github.com/openai/openai-cookbook). The tactic titled "Instruct the model to use retrieved knowledge to answer queries" provides a comprehensive example detailing how knowledge retrieval can be utilized to minimize the chances of a model generating inaccurate facts.
