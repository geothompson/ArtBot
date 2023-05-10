from os import system
from typing import List
import openai

#https://strikingloo.github.io/DALL-E-2-prompt-guide

prompt ="""
expand users seed idea by creating generative art prompts expanding upon  The prompts are sentence 400 characters or less that describe an image. 
try to include a style and mood, and framing, remove connecting words and condense
be clear with the main idea and  define the details and styles you want to replicate. 

The guidlines to write the prompts are below but make sure they incorperate the users idea:

``` 
Include adjectives similar to these:

beautiful
realistic
colorful
massive
abstract
aesthetic
ball bearing
biomorphic
brushwork
classic
clever
complex
conceptual

in addition, you should try and incorperate one or all of these categories

Style of art: stencil art, crayon, chalk, oil paintings, etc.
Camera view: ultra wide-angle, street level view, panoramic, etc.
Specific objects
Artists: Including an artist’s name in the prompt can mimic their style

the text prompts should include specific keywords that describe the desired style of the artwork. Some suggested style keywords are:

Abstract Expressionism
Abstraction
Academic
Action painting
Aesthetic
Allover painting
Angular
Appropriation
Architecture
Artifice
Automatism
Avant-garde
Baroque
Bauhaus
Contemporary
Cubism
Cyberpunk
Digital art
Fantasy
Impressionism
Minimal
Modern
Pixel art
Realism
Surrealism
```
format your answeres like these example prompts:
    “Pixar style 3D render of a baby hippo, 4k, high resolution, trending in artstation”

    “An oil painting of a mechanical clockwork flying machine from the renaissance, Gorgeous digital painting, amazing art, artstation 3, realistic”

    “fantasy tavern interior | Breath-taking digital painting with warm colours amazing art mesmerizing, captivating, artstation 3”

    “Cluttered house in the woods | anime oil painting high resolution cottagecore ghibli inspired 4k”

generate three promts without articles like "a" or "the" from the idea:
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







    
