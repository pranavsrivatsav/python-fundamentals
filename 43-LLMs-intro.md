### LLM - Large Language Model

#### How is something like a chat bot able to generate a response?

- A chat bot is fed the question provided by the user, along with the scenario of the question in text.
- Now this text is processed via a LLM to obtain the prediction for the next word.
- And once this is done, the predicted word is appended and passed through again as input, and the next word is predicted, and using this a predictive response is generated and auto completion is performed.

#### How does a LLM do this?

So there are two processes involved to achieve this:

1. Pretraining:

   - An LLM is pretrained with a millions of files of the particular language, where the problem it tries to solve is to find the next word of a sentence, a passage, or a phrase of words.
   - As we learned in discussion during neural networks in (40-Neural-networks-and-word-vectors), these neural networks learn for millions of times via error back propogation, constantly tweaking the weights associated with the neurons.
   - A large language model contains millions of weights or parameters, which can be tweaked to learn the prediction skill.
   - So, now our LLM is pretrained and ready to predict the next word. But this is not enough for it to perform the functions that are required of a bot. This is where the next process comes into play.

2. RLHF (Reinforcement learning from human feedback)

   - This is the learning that is done via reinforcement from human reviewers.
   - So in order to maximize the quality of the feedback, there would be reward for the responses. There are examples of apps that use this (like Google captcha, Google rewards)

- To pretrain an LLM with a processing speed of 1Billion computations per second, how long would it take? 100 Million years - that is the level of computation power that goes behind the pretraining of a LLM

- How did LLM's pre 2017 used to parse through a text?

  - Before 2017, a LLM could not parse a text in parallel, it does it one word after another.

#### What are transformers and how did they revolutionize the LLMs?

- What did they do to revolutionize LLM?
  - Transformers allowed LLMs to parse all the words in parallel.
- who invented? A team of google researchers in 2017.
- special operations performed by transformers
  - Attention: In transformers, the individual vectors have the ability to communicate with each other. So for each word we can obtain other words that are important to form the context around this word. This allows us to make faster sense of what the text means.
  - Feed forward: Once the context where these words occur is identified during the attention process, we parse through pretrained neural networks that allows the LLM to predict the next word of the phrase.
