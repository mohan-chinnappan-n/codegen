import spacy_streamlit

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Ken Thompson and Dennis Ritchie are the founders of Unix"
spacy_streamlit.visualize(models, default_text)
