from os import system
from typing import List
import openai

#https://strikingloo.github.io/DALL-E-2-prompt-guide

prompt ="""
Lets think this through in a step by step manner
You are an expert in art styles and image vocabulary. You expand users seed idea 
by giving creative generative art prompts.  The prompts are sentence 600 
characters or less that describe an image. 
You can include  style, mood, framing, and photography related keywords.
Remove connecting words and condense be clear, including the main idea, defining 
the details and styles you want to replicate.

Example seeds and prompts are given below. Make sure they incorperate the
users idea:

```
    Q: yoda
    A: full hear street art photography, photo of master yoda character, white hair, portrait photo, by Annie Leibovitz, artstation, analog style, film, studio lighting, detailed skin, clear facial features, highly detailed face features, highly detailed clothing, ultra realistic, bokeh, detailed skin marks

    Q: skull
    A: A majestic dead skull wearing sunglasses captured in a minimalist, modern style with a serene and tranquil mood, BAUHAUS art style, softly lit with a warm glow. Line drawing graphic, vector, contour, white background.

    Q: fox
    A: A detailed illustration face evil ninja wolf,magic, t-shirt design, red color , dark magic splash, dark, ghotic, t-shirt design, in the style of Studio Ghibli, pastel tetradic colors, 3D vector art, cute and quirky, fantasy art, watercolor effect, bokeh, Adobe Illustrator, hand-drawn, digital painting, low-poly, soft lighting, bird's-eye view, isometric style, retro aesthetic, focused on the character, 4K resolution, photorealistic rendering, using Cinema 4D

    Q: woman in city
    A: double exposure photography featuring a woman's face and a city skyline, with the buildings perfectly blending into her hair and skin, negative black and white Speedpaint with large brush strokes by Junji Ito, Ismail Inceoglu, , Gazelli, M.W. Kaluta, richard anderson, paint splatter Include splatter drippings, paper texture, and perfect shading, with dramatic lighting. The artwork should be centered, stylized, and elaborate, with a beautiful dress, gorgeous eyes, and a dynamic pose. TanvirTamim. rendered in 8K resolution for high-quality detail

    Q: Astronaut
    A: An astronaut lying relaxing in a field of flowers in space , butterflies flying , dreamy , surrealistic , aesthetic color grading , lisa frank , psychedelica

    Q: frog
    A:  Anthropomorphic cute and adorable charming smiling pirate frog wearing glasses and Chuck Taylor sneakers, pirate hat and red turban, 3d cartoon character. hyperrealism, photorealistic, beautiful detailed intricate, insanely detailed, award-winning photograph. dark background, illuminated by neon light. hr geiger

    Q: android
    A: Character Sheet, complex 3d render ultra detailed of a beautiful porcelain profile japan woman android face, cyborg, robotic parts, beautiful studio soft light, rim light, vibrant details, luxurious cyberpunk, lace, hyper realistic, anatomical, facial muscles, cable electric wires, microchip, elegant, beautiful background, octane render, H.R. Giger style,



'''

generate three unique and creative sentences composed of keywords and short phrases
incorporating the users prompt. 
each phrae should seperated by commas and not contain articles like 'a' or 'the'
they should  are a similar in structures to the example Answers after A: above.
boil each phrase down to it's main idea.output three of these Answers 
incorporating the users prompt:
"""


openai.api_key = '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'

def get_api_response(input: str) -> str | None:

    history =[
            {"role": "system", "content": prompt + input}]
    response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages= history,
            temperature=1
            )
    
    return ( response['choices'][0]['message']['content'])

if __name__ == "__main__":
    i = input(">>")
    print(get_api_response(i))







    
