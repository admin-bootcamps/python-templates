# Gen-AI with Python

This folder contains the sample Python files for Gen-AI activities.

We use OpenRouter API for Text > Text and Huggingface API for Text > Image.

An API is a way to ask the provider for the model's response without having to download and run a model to your computer, or using a website Playground.

## 1. Setup: Python in VSCode

### Create a Virtual Environment

1. In a new window, click 'Open Folder' and open your python_files folder. If a pop up comes up, click 'Yes, I trust the Authors'.

2. Press Ctrl+Shift+P and start typing 'Python: Create Environment' until the option appears.

3. Click 'Venv'.

4. Choose the latest version of Python you have installed.
5. Wait until your environment is created. You'll see a folder called '.venv' appear.

6. If you don't see the folders in the siderbar, press Ctrl+B to show/hide the folders list.

7. When this process is finished, a pop up in the bottom-right corner will say 'The following environment is selected: d:\python_files\.venv\......'

8. Press Ctrl+` to show the Terminal.

9. Click the expand arrow next to the '+' and open a Command Prompt window.
10. You should see your current file location with (.venv) before it. This confirms your virtual environment is set up and active.

### Install Requirements with pip

Type `pip --version` and press Enter to make sure you have pip installed.
You should get something like this:

```bash
> pip 25.x.x from d:\python_files\.venv\Lib\site-packages\pip (python 3.x)
```

Install the libraries.

```bash
pip install -r requirements.txt
```

The last two lines of the output should be something like this:

```bash
> Installing collected packages: urllib3, pillow, idna, charset-normalizer, certifi, requests
> Successfully installed certifi charset-normalizer idna pillow requests urllib3
```

Now, you'll be able to run your python file!
Open your python file from the sidebar, and make sure you've entered your TEXT_KEY or IMAGE_KEY.
Clik the 'Run' button in the top-right corner.
A new Python terminal will open and show you the output.
To stop an execution, click anywhere inside the Python terminal and press Ctrl+C.

---

## 2. IMAGE GENERATION

### 2.1 HUGGINGFACE API DOCUMENTATION

[HuggingFace API Documentation](https://huggingface.co/docs/inference-providers/tasks/text-to-image#:~:text=API%20specification)

#### CONSTANTS

```python
IMAGE_KEY = "hf_thisIsYourImageKey"
API_URL = f"https://router.huggingface.co/fal-ai/{MODEL_NAME}"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {IMAGE_KEY}"
}
```

### 2.2 IMAGE TEMPLATE

#### Data

This is what you send in the request.

```json
{
        "prompt": "prompt"
}
```

#### Response

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

### 2.3 IMAGE EXAMPLE

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

### 2.4 IMAGE MODELS

[Fal-AI Model information](https://fal.ai/api/models?categories=text-to-image)

API URL for specific model image generation:

```python
API_URL = f"https://router.huggingface.co/fal-ai/{id}"
```

For example:

```python
API_URL = "https://router.huggingface.co/fal-ai/fal-ai/imagen4/preview"
```

Here is the list of models we will use: [Fal Image Models](https://admin-bootcamps.github.io/playgrounds/fal_models.json)

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

## 3. TEXT GENERATION

### 3.1 OPENROUTER API DOCUMENATION

[OpenRouter Chat API Documentation](https://openrouter.ai/docs/api-reference/chat-completion)

[OpenRouter Single-Message API Documentation](https://openrouter.ai/docs/api-reference/completion)

#### CONSTANTS

```python
TEXT_KEY = "sk-or-v1-thisIsYourTextKey"
HEADERS = {
    "Authorization": f"Bearer {TEXT_KEY}",
    "Content-Type": "application/json"
}
```

---

### 3.2 Chat Completion (input multiple previous messages)

```python
URL = "https://openrouter.ai/api/v1/chat/completions"
```

#### CHAT TEMPLATE

##### Data

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

##### Response

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

#### CHAT EXAMPLE

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

### 3.3 COMPLETION (input ONE previous message)

OpenRouter Single Message API URL:

```python
API_URL = "https://openrouter.ai/api/v1/completions"
```

#### COMPLETION TEMPLATE

##### Data

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

#### Response

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

#### COMPLETION EXAMPLE

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

### 3.4 TEXT MODELS

Open the below link in your browser to view all the models.

[OpenRouter Models List](https://openrouter.ai/api/v1/models)

The models we recommend can be found here: [OpenRouter Models](https://admin-bootcamps.github.io/playgrounds/openrouter_models.json)

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
