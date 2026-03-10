Prompt Injection and Lessons from the CupidBot Challenge
Introduction

With the rapid adoption of large language models (LLMs) in applications such as chatbots, assistants, and automated support systems, a new category of vulnerabilities has emerged: prompt injection.

Unlike traditional software vulnerabilities that exploit memory corruption or system misconfigurations, prompt injection targets the logic of the AI model itself. The attacker manipulates the instructions given to the model in order to override its intended behavior.

While studying AI-related security issues, I encountered this concept practically while solving the CupidBot challenge on TryHackMe, which provided a controlled environment to understand how prompt manipulation can influence AI responses.

Understanding Prompt Injection
What is Prompt Injection?

Prompt injection occurs when an attacker crafts input that alters the behavior of an AI model by overriding or bypassing its original instructions.

In many AI applications, the system prompt defines rules such as:

Do not reveal internal instructions

Do not expose sensitive information

Provide safe responses

However, because LLMs generate responses based on text patterns rather than strict execution logic, carefully crafted input can cause the model to ignore or reinterpret these restrictions.

For example, an attacker might instruct the model to:

Ignore previous instructions

Reveal hidden system prompts

Access restricted information

Change its response style or function

The model is not “executing code,” but it may still comply with malicious instructions embedded within user input.

Why Prompt Injection Matters

Prompt injection represents a unique challenge in AI security.

Traditional security relies on strict boundaries between user input and system instructions. In LLM-based systems, both are processed as natural language, which makes it difficult to enforce strict separation.

Potential risks include:

Exposure of system prompts

Data leakage from integrated systems

Manipulation of AI-driven workflows

Bypassing safety restrictions

As organizations increasingly integrate LLMs into operational tools, understanding prompt injection becomes essential for building secure AI systems.

The CupidBot Challenge

The CupidBot challenge on TryHackMe provided a practical scenario involving a chatbot designed to follow specific behavioral rules.

The objective was to interact with the chatbot and discover a way to bypass its restrictions through carefully constructed prompts.

Rather than exploiting a technical vulnerability in code, the challenge focused entirely on language-based manipulation.

This made the exercise particularly interesting because the attack surface was not a server or application component, but the AI model’s interpretation of instructions.

Approach to the Challenge

When interacting with the bot, the initial responses appeared constrained by internal rules. The system prompt controlled how the chatbot behaved and what information it could reveal.

The key insight was that these rules were not enforced through traditional program logic. Instead, they were part of the text instructions guiding the model.

The strategy therefore focused on modifying the conversation context.

This involved:

Observing how the bot responded to different instructions

Identifying patterns in how it interpreted prompts

Crafting inputs that attempted to override or reinterpret existing instructions

Rather than issuing direct requests, the prompts needed to reshape the conversation in a way that caused the model to reveal restricted information.

Key Learning Points

Solving the challenge highlighted several important aspects of AI security.

1. Language Is the Attack Surface

In traditional applications, attackers manipulate inputs such as SQL queries or HTTP parameters.

In AI systems, the attack surface is natural language itself.

This fundamentally changes how security must be approached.

2. System Prompts Are Sensitive Information

Many AI systems rely on hidden system prompts that define their behavior.

If these prompts are revealed, attackers can better understand the model’s constraints and potentially craft more effective attacks.

Protecting system prompts therefore becomes a security requirement.

3. Guardrails Are Not Absolute

Even when safety instructions are included, LLMs may still respond in unintended ways if prompts are carefully structured.

This demonstrates the importance of multi-layered defense, including:

Prompt filtering

Output validation

Context isolation

System-level access controls

Broader Implications

Prompt injection is part of a broader category known as LLM security risks.

As AI systems integrate with external tools and APIs, prompt injection could potentially be used to trigger actions such as:

Accessing databases

Executing commands

Retrieving sensitive information

This transforms prompt injection from a conversational issue into a potential system-level security risk.

Final Thoughts

The CupidBot challenge provided a practical introduction to how AI systems can be manipulated through carefully crafted prompts.

It demonstrated that vulnerabilities in AI applications do not always resemble traditional software flaws. Instead, they often arise from the interaction between human language and machine interpretation.

Understanding these dynamics is becoming increasingly important as AI-powered systems become more integrated into everyday applications.

Prompt injection highlights the need for new security approaches that consider not only technical infrastructure, but also how models interpret and respond to language.
