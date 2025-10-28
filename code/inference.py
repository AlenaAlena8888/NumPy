from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base = "meta-llama/Llama-2-7b-hf"
lora_path = "../results/saved_loras/my_lora"

tokenizer = AutoTokenizer.from_pretrained(base, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(base, device_map="auto", trust_remote_code=True)
model = PeftModel.from_pretrained(model, lora_path)

prompt = "Поясни простими словами, що таке LoRA:"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(out[0], skip_special_tokens=True))