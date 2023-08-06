# EMO_AI
Use state-of-the-art to detect the user's emotion on social apps, particularly needed in modern society

## Installation
#### it's recommended to install pytorch via [official guide](https://pytorch.org/) first
#### package info: [here]()

```bash
# stable version: have to install transformers, tokenizers, torch by hand ...
pip install EMO-AI==0.0.5

# latest version
pip install EMO-AI
```

## Usage

#### Very high level one
```python
from EMO_AI.all import *
# default model w/out pretrained weight
model = get_model(pretrained=False)
print(get_output("this love has taken it's toll on me", model)
```

#### High level one
```python
from EMO_AI.model_api import *
PATH = "the_model.pt"
model = get_model(PATH)
text = "This love has taken its toll on me"
result = get_output(text, model)
print(result)
```

#### A bit in-detail one
```python
from EMO_AI.model_api import *
from EMO_AI.data_process import *
t = "Elvis is the king of rock"
tokenizer = get_tokenizer()
PATH = "your_pretrained_model.pt"
# check how the model is saved in the first place
model = get_model(PATH, inference_only=True)
import torch
with torch.no_grad():
    model.eval() # evaluate mode
    # convert_text_to_tensor(t) would work, but kinda slower and wasteful
    rep = model(convert_text_to_tensor(t, tokenizer))
# print output tensor from forward pass
print(rep)
# get predicted emotion
print_emotion(rep)
```
