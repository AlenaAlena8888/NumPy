import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import time
import os
import pandas as pd
import matplotlib.pyplot as plt

def download_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16
    ).to("cuda")
    return pipe

pipe = download_model()

def generate_image(prompt, pipe, steps=20, guidance=7.5,
                   width=512, height=512, seed=None, negative_prompt=None, save_path="outputs"):

    if seed is not None:
        generator = torch.Generator(device="cuda").manual_seed(seed)
    else:
        generator = None

    os.makedirs(save_path, exist_ok=True)
    start_time = time.time()

    image = pipe(
        prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=steps,
        guidance_scale=guidance,
        width=width,
        height=height,
        generator=generator
    ).images[0]

    elapsed_time = time.time() - start_time

    filename = f"{save_path}/{prompt[:20].replace(' ', '_')}_steps{steps}_guid{guidance}_size{width}x{height}.png"
    image.save(filename)

    return image, elapsed_time

uk_prompts = [
    "Гірський пейзаж з водоспадом на заході сонця",
    "Кіт у космічному скафандрі на Місяці",
    "Старовинний замок у тумані"
]

en_prompts = [
    "Mountain landscape with waterfall at sunset",
    "Cat in space suit on the Moon",
    "Ancient castle in the fog"
]

steps_list = [10, 20, 30, 50]
guidance_list = [3.0, 7.5, 12.0, 15.0]
sizes = [(256,256), (512,512), (768,768)]
seed = 42
negative_prompt = "blurry, bad quality, distorted"
results = []

for prompt in uk_prompts + en_prompts:
    for steps in steps_list:
        for guidance in guidance_list:
            for width, height in sizes:
                image, t = generate_image(
                    prompt, pipe,
                    steps=steps, guidance=guidance,
                    width=width, height=height,
                    seed=seed, negative_prompt=negative_prompt
                )
                results.append({
                    "prompt": prompt,
                    "steps": steps,
                    "guidance": guidance,
                    "width": width,
                    "height": height,
                    "time_sec": t
                })

                df_results = pd.DataFrame(results)
                print(df_results.head())

                df_results.to_excel("SD_experiment_results.xlsx", index=False)

df_agg = df_results.groupby("steps")["time_sec"].mean()
plt.figure(figsize=(8,5))
plt.plot(df_agg.index, df_agg.values, marker='o')
plt.title("Час генерації від кількості кроків")
plt.xlabel("num_inference_steps")
plt.ylabel("Час (сек)")
plt.grid(True)
plt.show()

df_agg2 = df_results.groupby("guidance")["time_sec"].mean()
plt.figure(figsize=(8,5))
plt.plot(df_agg2.index, df_agg2.values, marker='o', color='orange')
plt.title("Час генерації від guidance_scale")
plt.xlabel("guidance_scale")
plt.ylabel("Час (сек)")
plt.grid(True)
plt.show()