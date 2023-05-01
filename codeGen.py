# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
# import sys

import numpy as np


import streamlit as st

params = st.experimental_get_query_params()

st.write(f"""

## Parameters 
```python
{params}
```
""")




nlp = spacy.load('en_core_web_sm')
apex_types = ['boolean', 'string', 'blob', 'date', 'time',  'datetime', 'decimal', 'double', 'id', 'integer', 'long', 'object', ]

def generate_apex_class(natural_language_input):
    doc = nlp(natural_language_input)
    class_name = None
    variables = []

    # extract the class name and variables from the input
    for token in doc:
        # print (f'token: {token}, token.pos_: {token.pos_}, token.text.title: {token.text.title()}')
        if token.pos_ in ['NOUN', 'PROPN'] and not class_name and token.text.lower() not in ['class' ]:  
            class_name = token.text.title()
        elif token.pos_ == 'NOUN' and class_name and token.text.lower() not in apex_types:
             variables.append((token.text.lower(), token.pos_))

    # generate the Apex code
    var_type = 'String'
    code = f'public class {class_name} {{\n'
    for variable in variables:
        name, pos = variable
        code += f'    public {var_type} {name} {{ get; set; }}\n'
    code += '}'

    return code

#---------------
input_text = str(params['input']) #or  "Create a class called Customer with  name and age"

generated_code = generate_apex_class(input_text)
print(generated_code)
st.write(f"""
## Generated code
### Input
```
{input_text}
```
---
```java
 {generated_code}
```
 """)


