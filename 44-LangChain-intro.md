### LangChain

[Resource](https://www.youtube.com/watch?v=1bUy-1hGZpI)

#### Intro

- Let's suppose we are trying to build an application that needs to

  - gets questions from the user
  - scraps the data from the web and finds an accurate response
  - delivers the response to the user

- if you see each of the features of our application will require the involvement of LLMs
- Now, instead of restricting ourself to use one LLM to build these features, we can choose and use multiple LLMs fitting the best one for the feature.
- This is what LangChain enables us to do, chaining LLMs
- On top of this LangChain has a lot of abstractions built in to hide the complexity of performing this chaining to the developers using it.

#### Important components/concepts related to LangChain

- LLM: As explained earlier, we can use multiple LLMs in our applications and chain them in a langchain, from open sourced LLAMA2 to close sourced GPT-4

- Prompts: Prompts help us to fine tune the LLMs. There are different methods of prompts, for eg:

  - We can use a direct prompt like "Restrict usage of technical terms in your response".
  - Multi-shot prompting: We can provide examples of input-response to tune/train the LLM, so that we expect similar type of responses for similar input.
  - Output format: We can simply provide a format to tune the response.
  - The above are just a sample of type of prompts we can provide.

- Chains:

  - We can use multiple LLMs and for each of the LLMs, fine tuning can be done with prompts respective to those LLMs.
  - Chains help us to link this all together, where the output of one function is provided as an input to another.

- Indexes:

  - On top of the training data, we might need to pass our own data/internal files or emails to train the LLMs to customize them for our purposes.
  - This training data can be provided in a number of ways. Indexes are a way to help us to do this.
  - The training data can be provided in several ways, like the below examples:
    - Doc Loader: Google Drive, One Drive or Databases like MongoDb via Pandas etc.
    - Vector DBs: Vector DBs like Chroma, Pinecone, where the a large amount of details can be stored in a less human accessible way, via mathematical representations of data, that are called Vectors.
    - File Splitters: They allow us to split the input in a semantical way, and then we can merge this splitted input in a manner of our choosing.

- Memory: LLMs dont have a long term memory of their own.

  - In order to get the next output, we might need to provide the entire conversation as an input, or a summary of the conversation.
  - LangChain solves this problem by providing utilities to help us store this, the entire conversation or a part of the conversation etc.

- Agents: Agents are applications that are provisioned with two main elements: LLMs and a set of tools.
  - For any given set of input, they leverage the power of LLMs to decide on what action to take.
  - Once an action is decided, they leverage the tools to perform this action.
  - For eg: Something like a customer support bot, where it can perform actions based on the issue shared by the customer
    - If the issue is decipherable by the LLM, and the output of LLM is mapped to a defined action using a tool,
      - it can automatically raise a ticket assigning the same to a service executive.
    - Or if a certain action is not being able to be mapped out.
      - it can handover the conversation to a real human support executive.

#### Use Cases of LangChain

- chat bots
- summarization
- Question anwering
- Data Augmentation: We can use LLMs to generate data to train new models
