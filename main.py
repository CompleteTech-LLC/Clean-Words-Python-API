from fastapi import FastAPI, HTTPException
from typing import List
import re

app = FastAPI()

def clean_word_list(word_list: List[str]) -> List[str]:
    """
    This function takes a list of words and returns a new list with words
    that contain only ASCII letters (a-z, A-Z) and hyphens (-).
    """
    cleaned_list = []
    for word in word_list:
        # Using regex to match only ASCII letters and hyphens
        if re.match(r'^[a-zA-Z\-]+$', word):
            cleaned_list.append(word)
    
    return cleaned_list

@app.post("/clean-words/", response_model=List[str])
async def clean_words(word_list: List[str]):
    try:
        cleaned_list = clean_word_list(word_list)
        return cleaned_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
