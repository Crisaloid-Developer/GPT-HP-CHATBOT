# -*- coding: utf-8 -*-
"""Copy of YT LaMini-Flan-T5-783M 8Bit  .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tUAR7OkTIKnLKa-FjeuSuTc7MhFzwxpd
"""

!pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1
!pip install nvidia-cublas-cu12==12.1.3.1 nvidia-cuda-cupti-cu12==12.1.105 nvidia-cuda-nvrtc-cu12==12.1.105 nvidia-cuda-runtime-cu12==12.1.105 nvidia-cudnn-cu12==8.9.2.26 nvidia-cufft-cu12==11.0.2.54 nvidia-curand-cu12==10.3.2.106 nvidia-cusolver-cu12==11.4.5.107 nvidia-cusparse-cu12==12.1.0.106 nvidia-nccl-cu12==2.20.5 nvidia-nvtx-cu12==12.1.105



!nvidia-smi

"""# LaMini-Flan-T5-783M"""

!pip install --upgrade torch torchvision

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
import torch

checkpoint = "MBZUAI/LaMini-Flan-T5-783M"
# checkpoint = "MBZUAI/LaMini-Neo-1.3B"
# checkpoint = "MBZUAI/LaMini-GPT-1.5B"



tokenizer = AutoTokenizer.from_pretrained(checkpoint)
base_model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint,
                                             device_map='auto',
                                             torch_dtype=torch.float16,
                                             load_in_8bit=True)

pipe = pipeline('text2text-generation',
                 model = base_model,
                 tokenizer = tokenizer,
                 max_length=512,
                 do_sample=True,
                 temperature=0.7,
                 top_p=0.95,
                 repetition_penalty=1.15
                 )

"""### The prompt & response"""

import json
import textwrap

human_prompt = 'What is the meaning of life?'

def get_prompt(instruction):
    prompt_template = f"Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{instruction}\n\n### Response:"
    return prompt_template

print(get_prompt('What is the meaning of life?'))

def parse_text(data):
    for item in data:
        text = item['generated_text']
        wrapped_text = textwrap.fill(text, width=100)
        print(wrapped_text +'\n\n')
        # return assistant_text

data = [{'generated_text': 'What is the capital of England? \n### Response: The capital city of England is London.'}]
parse_text(data)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'my heatpump leaks water what i can do? reply giving possible solutions in bulletpoints'
# generated_text = pipe(get_prompt(prompt))
# parse_text(generated_text)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'What is the capital of England?'
# generated_text = pipe(get_prompt(prompt))
# parse_text(generated_text)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Write a short note to Sam Altman giving reasons to open source GPT-4'
# generated_text = pipe(get_prompt(prompt))
# parse_text(generated_text)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'As an AI do you like the Simpsons? What dow you know about Homer?'
# generated_text = pipe(get_prompt(prompt))
# parse_text(generated_text)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Tell me about Homer on the TV show the simpsons'
# generated_text = pipe(get_prompt(prompt),
#                        max_length=512,
#                      do_sample=True)
# parse_text(generated_text)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Tell me about Homer on the TV show the simpsons'
# generated_text = pipe(get_prompt(prompt))
# parse_text(generated_text)

# Commented out IPython magic to ensure Python compatibility.
# 
# %%time
# prompt = 'Answer the following question by reasoning step by step. The cafeteria had 23 apples. If they used 20 for lunch, and bought 6 more, how many apple do they have?'
# generated_text = pipe(get_prompt(prompt))
# parse_text(generated_text)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Answer the following yes\/no question by reasoning step-by-step. \n Can you write a whole Haiku in a single tweet?'
# generated_text = pipe(get_prompt(prompt))
# parse_text(generated_text)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Tell me about Harry Potter and studying at Hogwarts?'
# generated_text = pipe(get_prompt(prompt))
# parse_text(generated_text)

"""## WizardLM Answers below"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# # prompt = 'What are the difference between Llamas, Alpacas and Vicunas?'

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Write a short note to Sam Altman giving reasons to open source GPT-4'

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'What is the capital of England?'

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Write a story about a Koala playing pool and beating all the camelids.'

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'As an AI do you like the Simpsons? What dow you know about Homer?')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Answer the following question by reasoning step by step. The cafeteria had 23 apples. If they used 20 for lunch, and bought 6 more, how many apple do they have?'

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Answer the following yes\/no question by reasoning step-by-step. \n Can you write a whole Haiku in a single tweet?'
# raw_output = pipe(get_prompt(prompt))
# parse_text(raw_output)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Can Geoffrey Hinton have a conversation with George Washington? Give the rationale before answering.'
# raw_output = pipe(get_prompt(prompt))
# parse_text(raw_output)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Could Geoffrey Hinton have had dinner with Harry Potter? Give the rationale before answering.'
# raw_output = pipe(get_prompt(prompt))
# parse_text(raw_output)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'tell me about 3 facts about Marcus Aurelius that most people dont know'
# raw_output = pipe(get_prompt(prompt))
# parse_text(raw_output)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Who was Marcus Aureliuss son?'
# raw_output = pipe(get_prompt(prompt))
# parse_text(raw_output)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Who was Marcus Aureliuss son and what was he like?'
# raw_output = pipe(get_prompt(prompt))
# parse_text(raw_output)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Who was the emperor Commodus?'
# raw_output = pipe(get_prompt(prompt))
# parse_text(raw_output)
#

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = 'Tell me about Harry Potter and studying at Hogwarts?'
# raw_output = pipe(get_prompt(prompt))
# parse_text(raw_output)
#

