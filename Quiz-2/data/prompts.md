## Prompts for Quiz-2
For clarity I will refer to the whole recipe text as just **(Recipe Text)**  

### Prompt-full Approach
Prompt 1:  **(Recipe Text)** convert this recipe into json with the recipe representation record (r3) format with the following metadata 'recipe_name' 'data_provenance' 'macronutrients' 'ingredients' 'instructions'  
Out:   
[Chocolate Cake Output 1](5min_choc_cake1.json)  
[Jello Fondant Output 1](jello_marshmallow_fondant.json)

Prompt 2: **(Recipe Text)** convert this recipe into a recipe representation record format in json.  
Out:  
[Chocolate Cake Output 2](5min_choc_cake2.json)  
[Jello Fondant Output 2](jello_marshmallow_fondant2.json)  

Prompt 3: **(Recipe Text)** convert this recipe into r3 format in json.  
Out:
[Chocolate Cake Output 3](5min_choc_cake3.json)  
[Jello Fondant Output 3](jello_marshmallow_fondant3.json)  

### Prompt-partial Approach

Prompt 1: **(Recipe Text)** convert this recipe into r3 format, starting with just the recipe name, data provenance, and macronutrients.

Prompt 1b: Add the ingrediants and instructions to that file.

Out:
