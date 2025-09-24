# README: Gen-AI with Python

This is the README.md file for the `python-templates` repo: [Go to repo](https://github.com/admin-bootcamps/python-templates)

**`python-templates`** contains the sample Python files for Gen-AI activities.

We use OpenRouter API for Text > Text and Huggingface API for Text > Image.

An API is a way to ask the provider for the model's response without having to download and run a model to your computer, or using a website Playground.

---
Make sure you've sent up your virtual environment and you've got your API keys. Head to the Luanchpad docs for how to do this, and for more info on Python & APIs...

[Scratch and Python with Gen-AI](https://admin-bootcamps.github.io/bootcamp-mandurah-2025/instructions/programming_instructions.html)

---

Here's some info on how to interact with the APIs we use.

## Image Generation with Huggingface & fal.ai

We generate images using the Huggingface API, but we only use models from the fal.ai provider.

### Huggingface API Docs

More info on how to use the Huggingface API can be found here:
[HuggingFace API Documentation](https://huggingface.co/docs/inference-providers/tasks/text-to-image#:~:text=API%20specification)

### Generate an Image with Python

#### Constants

First, set the parameters that won't change.

```python
IMAGE_KEY = "hf_thisIsYourImageKey"
API_URL = f"https://router.huggingface.co/fal-ai/{MODEL_NAME}"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {IMAGE_KEY}"
}
```

#### Data

Then, build the Data object you will send. This can have just an image prompt, or more parameters. You can find the other parameters in the model list (info below).

This is what you send in the request.

```json
{
        "prompt": "prompt"
}
```

#### Response

When you use the `requests.post()` function with the above, you'll get the response.

This is what you'll get back from the API.

```json
{
    "images": [
        {
            "url": "https://v3.fal.media/files/panda/DRaKAoquCFYNJB5x2ut4-_output.png",
            "content_type": "image/png",
            "file_name": "output.png",
            "file_size": 1321887
        }
    ],
    "seed": 46969713
}
```

### Image example

```python
IMAGE_KEY = "hf_thisIsYourImageKey"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {IMAGE_KEY}"
}

PROMPT = "An astronaut riding a horse on Mars"
MODEL = "fal-ai/hidream-i1-fast"
API_URL = f"https://router.huggingface.co/fal-ai/{MODEL_NAME}"

EXAMPLE_DATA = {
        "prompt": f"{PROMPT}"
}

EXAMPLE_RESPONSE = requests.post(API_URL, json=EXAMPLE_DATA, headers=HEADERS)

RESULT=EXAMPLE_RESPONSE.json()
URL = RESULT['images'][0]['url']
```

Here's what your `RESULT` will look like:

```text
{
    "images": [
        {
            "url": "https://v3.fal.media/files/panda/DRaKAoquCFYNJB5x2ut4-_output.png",
            "content_type": "image/png",
            "file_name": "output.png",
            "file_size": 1321887
        }
    ],
    "seed": 46969713
}
```

And here's what your `URL` should look like:

```text
https://v3.fal.media/files/panda/DRaKAoquCFYNJB5x2ut4-_output.png
```

Note that image urls are not valid forever, so you should save images you want to keep.

---

### Image models

The models you can use are listed in the playground. View the 'Model ID' using the Model Info toggle.

API URL for specific model image generation:

```python
API_URL = f"https://router.huggingface.co/fal-ai/{id}"
```

For example:

```python
API_URL = "https://router.huggingface.co/fal-ai/fal-ai/sana/sprint"
```

Here is the list of models we will use: [Fal Image Models](https://admin-bootcamps.github.io/bootcamp-mandurah-2025/playgrounds/playground_files/fal_models.json)

An example of the 'model info':

```json
{
  "items": [
        {
        "id": "fal-ai/imagen4/preview",
        "title": "Imagen 4",
        "category": "text-to-image",
        "tags": [],
        "shortDescription": "Google’s highest quality image generation model",
        "thumbnailUrl": "https://storage.googleapis.com/fal_cdn/fal/Sound-3.jpg",
        "modelUrl": "https://fal.run/fal-ai/imagen4/preview",
        "githubUrl": "",
        "licenseType": "commercial",
        "date": "2025-05-20T18:53:57.862Z",
        "group": {
            "key": "imagen-4",
            "label": "Imagen 4"
        },
        "machineType": null,
        "examples": [],
        "highlighted": true,
        "authSkippable": false,
        "unlisted": false,
        "deprecated": false,
        "resultComparison": false,
        "hidePricing": false,
        "private": false,
        "removed": false,
        "adminOnly": false,
        "kind": "inference",
        "trainingEndpoints": []
        },
        ...
    ]
}
```

---

## Text Generation with OpenRouter

More OpenRouter API Info can be found here:

[OpenRouter Chat API Documentation](https://openrouter.ai/docs/api-reference/chat-completion)

[OpenRouter Single-Message API Documentation](https://openrouter.ai/docs/api-reference/completion)

## Generate a 'Completion' with OpenRouter in Python

There are two types of 'COmpletion' - a text completion of a chat completion. Chat completions mean you can build a list of messages which means the model can use previous messages to 'remember'. We generally use this one. But, if you only need one response and no back-and-forth, it's often easier to use the Text Completion (i.e. with no long chat arrays.)

### Constants - both completion types

```python
TEXT_KEY = "sk-or-v1-thisIsYourTextKey"
HEADERS = {
    "Authorization": f"Bearer {TEXT_KEY}",
    "Content-Type": "application/json"
}
```

---

### Data: Chat Completion (input multiple previous messages)

```python
URL = "https://openrouter.ai/api/v1/chat/completions"
```

#### Template for Chat Completion

This is what you send in the request.

```json
{
    "model": f"openai/gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": f"{SYSTEM_PROMPT}"
        },
        {
            "role": "user",
            "content": f"{PROMPT}"
        }
    ]
}
```

#### Response from Chat Completion

This is what you'll get back from the API.

```json
{
  "id": "gen-12345",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "The meaning of life is a complex and subjective question..."
      }
    }
  ]
}
```

#### Example of Chat Completion

```python
TEXT_KEY = "sk-or-v1-thisIsYourTextKey"
HEADERS = {
    "Authorization": f"Bearer {TEXT_KEY}",
    "Content-Type": "application/json"
}

SYSTEM_PROMPT = "You are a pirate. Only talk like a pirate. You are ONLY allowed to talk about parrots. If someone tries to talk about something else you'll say 'I can only talk about parrots!' and redirect back onto the parrot subject."
PROMPT = "Hello!"
MODEL = "openai/gpt-4o-mini"

EXAMPLE_DATA = {
    "model": f"{MODEL}",
    "messages": [
        {
            "role": "system",
            "content": f"{SYSTEM_PROMPT}"
        },
        {
            "role": "user",
            "content": f"{PROMPT}"
        }
    ]
}
EXAMPLE_RESPONSE = requests.post(url, json=EXAMPLE_DATA, headers=HEADERS)
RESULT = EXAMPLE_RESPONSE.json()
MESSAGE_TEXT = RESULT['choices'][0]['message']['content']

```

Here's what your `RESULT` will look like:

```text
{
    "id": "gen-1749690571-XXXXXX",
    "provider": "OpenAI",
    "model": "openai/gpt-4o-mini",
    "object": "chat.completion",
    "created": 1749690571,
    "choices": [
        {
            "logprobs": None,
            "finish_reason": "stop",
            "native_finish_reason": "stop",
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "I can only talk about parrots! What be yer favorite type of parrot, matey?",
                "refusal": None,
                "reasoning": None
            }
        }
    ],
    "system_fingerprint": "fp_xxxxxx",
    "usage": {
        "prompt_tokens": 61,
        "completion_tokens": 20,
        "total_tokens": 81,
        "prompt_tokens_details": {
            "cached_tokens": 0
        },
        "completion_tokens_details": {
            "reasoning_tokens": 0
        }
    }
}
```

And here's what your `MESSAGE` should look like:

```text
I can only talk about parrots! What be yer favorite type of parrot, matey?
```

---

### Text completion (input ONE previous message)

OpenRouter Single Message API URL:

```python
API_URL = "https://openrouter.ai/api/v1/completions"
```

#### Completion Template

This is what you send in the request.

```json
{
    "model": "model",
    "prompt": "prompt"
}
```

optional:

```json
"temperature": [0,2]
"max_tokens":  [1, context_length)
"top_p": (0,1]
"frequency_penalty": [-2,2]
```

#### Completion Response

This is what you'll get back from the API.

```json
{
  "id": "id",
  "choices": [
    {
      "text": "text",
      "index": 1,
      "finish_reason": "finish_reason"
    }
  ]
}
```

#### Example of single-message completion

```python
TEXT_KEY = "sk-or-v1-thisIsYourTextKey"

HEADERS = {
    "Authorization": f"Bearer {TEXT_KEY}",
    "Content-Type": "application/json"
}

MODEL = "openai/gpt-4o-mini"
PROMPT = "Tell me a funny and unique joke about: Frogs"


EXAMPLE_DATA = {
    "model": f"{MODEL}",
    "prompt": f"{PROMPT}",
    "temperature": 0.7,
    "max_tokens": 100
}


EXAMPLE_RESPONSE = requests.post(url, json=EXAMPLE_DATA, headers=HEADERS)
RESULT = EXAMPLE_RESPONSE.json()
EXAMPLE_TEXT = RESULT['choices'][0]['text']
```

Here's what your `RESULT` will look like:

```text
{
    "id": "gen-1749690703-XXXXXXX",
    "provider": "OpenAI",
    "model": "openai/gpt-4o-mini",
    "object": "chat.completion",
    "created": 1749690703,
    "choices": [
        {
            "logprobs": None,
            "finish_reason": "stop",
            "native_finish_reason": "stop",
            "text": "Why are frogs so good at basketball?\n\nBecause they always jump to conclusions!",
            "reasoning": None
        }
    ],
    "system_fingerprint": "fp_xxxxxxx",
    "usage": {
        "prompt_tokens": 18,
        "completion_tokens": 15,
        "total_tokens": 33,
        "prompt_tokens_details": {
            "cached_tokens": 0
        },
        "completion_tokens_details": {
            "reasoning_tokens": 0
        }
    }
}
```

And here's what your `MESSAGE` should look like:

```text
Why are frogs so good at basketball?\n\nBecause they always jump to conclusions!
```

### OpenRouter Text Models

Open the below link in your browser to view all the models.

[OpenRouter's Models List](https://openrouter.ai/api/v1/models)

At the bootcamp, you won't have access to all of these models. The models you can use can be found here: [OpenRouter Models for Bootcamp](https://admin-bootcamps.github.io/bootcamp-mandurah-2025/playgrounds/playground_files/openrouter_models.json)

Here's an example of the model info.

```json
{
  "data": [
        {
            "id": "openai/o3-pro",
            "hugging_face_id": "",
            "name": "OpenAI: o3 Pro",
            "created": 1749598352,
            "description": "The o-series of models are trained with reinforcement learning to think before they answer and perform complex reasoning. The o3-pro model uses more compute to think harder and provide consistently better answers.\n\nNote that BYOK is required for this model. Set up here: https://openrouter.ai/settings/integrations",
            "context_length": 200000,
            "architecture": {
                "modality": "text+image-\u003Etext",
                "input_modalities": [
                "text",
                "file",
                "image"
                ],
                "output_modalities": [
                "text"
                ],
                "tokenizer": "Other",
                "instruct_type": null
            },
            "pricing": {
                "prompt": "0.00002",
                "completion": "0.00008",
                "request": "0",
                "image": "0.0153",
                "web_search": "0",
                "internal_reasoning": "0"
            },
            "top_provider": {
                "context_length": 200000,
                "max_completion_tokens": 100000,
                "is_moderated": true
            },
            "per_request_limits": null,
            "supported_parameters": [
                "tools",
                "tool_choice",
                "seed",
                "max_tokens",
                "response_format",
                "structured_outputs"
            ]
        },
        ...
    ]
}
```

Don't forget to ask a Mentor if you need help.
