import os
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

MODEL_NAME = "meta-llama/Llama-2-7b-hf"
DATA_PATH = "../data/processed/dataset.jsonl"

def main():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto", load_in_8bit=False, torch_dtype="auto", trust_remote_code=True)

    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=["q_proj","v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    model = get_peft_model(model, lora_config)

    ds = load_dataset("json", data_files={"train": DATA_PATH})["train"]

    def tokenize_fn(examples):
        texts = [ (ex.get("input","") + "\n" + ex.get("output","")) for ex in examples["output"] ]
        return tokenizer(texts, truncation=True, max_length=1024, padding="max_length")

    tokenized = ds.map(lambda x: tokenizer(x["output"], truncation=True, max_length=1024, padding="max_length"), batched=True)
    tokenized = tokenized.remove_columns([c for c in tokenized.column_names if c not in ["input_ids","attention_mask"]])
    tokenized.set_format(type="torch")

    training_args = TrainingArguments(
        output_dir="../results/saved_loras",
        per_device_train_batch_size=1,
        num_train_epochs=3,
        learning_rate=2e-4,
        logging_steps=10,
        save_total_limit=3,
        fp16=True,
        gradient_accumulation_steps=4,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized,
        tokenizer=tokenizer
    )

    trainer.train()
    trainer.save_model("../results/saved_loras/my_lora")
    print("Done")

if __name__ == "__main__":
    main()