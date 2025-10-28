import time
import torch
from diffusers import StableDiffusionPipeline

def download_model():
    return "runwayml/stable-diffusion-v1-5"

def prepare_pipe(model_name, device="cuda"):
    pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16)
    pipe = pipe.to(device)
    return pipe

def generate_image(pipe, prompt, steps, guidance, width, height, seed=None, negative_prompt=None):
    generator = None
    if seed is not None:
        generator = torch.Generator(device=pipe.device).manual_seed(seed)
    start = time.time()
    result = pipe(prompt=prompt,
                  num_inference_steps=steps,
                  guidance_scale=guidance,
                  width=width,
                  height=height,
                  generator=generator,
                  negative_prompt=negative_prompt)
    image = result.images[0]
    elapsed = time.time() - start
    return image, elapsed

if __name__ == "__main__":
    model = download_model()
    pipe = prepare_pipe(model, device="cuda")

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

    steps_list = [10,20,30,50]
    guidance_list = [3.0,7.5,12.0,15.0]
    sizes = [(256,256),(512,512),(768,768)]

    out_dir = "../images/"

    idx = 0
    for pset, lang in [(uk_prompts,"uk"), (en_prompts,"en")]:
        for prompt in pset:
            for steps in steps_list:
                for guidance in guidance_list:
                    for size in sizes:
                        seed = 42
                        img, t = generate_image(pipe, prompt, steps, guidance, size[0], size[1], seed=seed)
                        fname = f"{lang}_p{idx}_s{steps}_g{guidance}_w{size[0]}_seed{seed}.png"
                        img.save(out_dir + fname)
                        print("Saved", fname, " time:", round(t,2))
            idx += 1