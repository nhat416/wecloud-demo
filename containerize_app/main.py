from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pathlib import Path
import random

app = FastAPI()

# Define the Q&A list
qa_list = {
    "what is a black hole": "A black hole is a region of space where the gravitational pull is so strong that nothing, not even light, can escape from it.",
    "what is the speed of light": "The speed of light in a vacuum is approximately 299,792 kilometers per second (186,282 miles per second).",
    "what is dark matter": "Dark matter is a form of matter that does not emit, absorb, or reflect light, making it invisible. It is thought to make up about 27% of the universe.",
    "what is dark energy": "Dark energy is a mysterious force that is causing the expansion of the universe to accelerate. It is thought to make up about 68% of the universe.",
    "what is a supernova": "A supernova is a powerful and luminous explosion that occurs when a star exhausts its nuclear fuel and collapses under its own gravity.",
    "what is a neutron star": "A neutron star is a dense, compact object that remains after a supernova explosion. It is composed mostly of neutrons and has a very strong gravitational field.",
    "what is the big bang": "The Big Bang is the leading explanation for the origin of the universe. It suggests that the universe began as a singularity around 13.8 billion years ago and has been expanding ever since.",
    "what is a galaxy": "A galaxy is a massive system of stars, stellar remnants, interstellar gas, dust, and dark matter, bound together by gravity. The Milky Way is an example of a galaxy.",
    "what is a quasar": "A quasar is an extremely luminous and active galactic nucleus, powered by a supermassive black hole at its center.",
    "what is cosmic microwave background radiation": "Cosmic microwave background radiation is the thermal radiation left over from the Big Bang. It provides evidence for the early state of the universe."
}

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(question: Question):
    normalized_question = question.question.lower().rstrip('?')
    answer = qa_list.get(normalized_question)
    if answer:
        return {"answer": answer}
    else:
        hint_question = random.choice(list(qa_list.keys()))
        return {
            "answer": "This question is not part of my pre-defined Q&A list of questions and answers. Please ask another question.\n"
                      "Here is a suggested question you can ask: '{}'?".format(
                hint_question)
        }

@app.get("/", response_class=HTMLResponse)
async def read_index():
    html_content = Path("backup/index.html.bk").read_text()
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)