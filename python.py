import spacy_streamlit
import streamlit as st
import pandas as pd
from spacy_transformers import Transformer
from spacy_transformers.pipeline_component import DEFAULT_CONFIG

DEFAULT_TEXT = """Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002."""

model = "en_core_web_trf"

st.title("Identifyer")
text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)
doc = spacy_streamlit.process_text(model, text)

spacy_streamlit.visualize_ner(
    doc,
    labels=["CARDINAL", "DATE", "EVENT", "FAC", "GPE", "LANGUAGE", "LAW", "LOC", "MONEY", "NORP", "ORDINAL", "ORG", "PERCENT", "PERSON", "PRODUCT", "QUANTITY", "TIME", "WORK_OF_ART"],
    show_table=False,
    title="filter",
)

df = pd.DataFrame(pd.DataFrame({
'type': ["ORG", "DATE", "EVENT", "FAC", "GPE", "LOC", "MONEY", "NORP", "PERCENT", "PERSON", "PRODUCT", "QUANTITY", "TIME", "WORK_OF_ART", "LANGUAGE", "LAW", "ORDINAL", "CARDINAL"],
'meaning': ["Companies, agencies, institutions, etc.", "Absolute or relative dates or periods", "Named hurricanes, battles, wars, sports events, etc.", "Buildings, airports, highways, bridges, etc.", "Countries, cities, states", "Non-GPE locations, mountain ranges, bodies of water", "Monetary values, including unit", "Nationalities or religious or political groups", "Percentage (including “%”)", "People, including fictional", "Vehicles, weapons, foods, etc. (Not services)", "Measurements, as of weight or distance", "Times smaller than a day", "Titles of books, songs, etc.", "Any named language", "Named documents made into laws", "first”, “second”, ...", "Numerals that do not fall under another type"],
}))

df.index = [""] * len(df)
st.table(df)
