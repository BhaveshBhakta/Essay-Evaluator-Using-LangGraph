from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
import operator
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    temperature=0.2, 
    groq_api_key=os.getenv("GROQ_API_KEY"), # Retrive API key from environment variable
    model_name="llama-3.3-70b-versatile"
)


class EvaluationSchema(BaseModel):
    feedback: str = Field(description="Detailed feedback for the essay")
    score: int = Field(description="Score out of 10", ge=0, le=10)


structured_model = model.with_structured_output(EvaluationSchema)


class EssayState(TypedDict):
    essay: str
    language_feedback: str
    analysis_feedback: str
    clarity_feedback: str
    overall_feedback: str
    individual_scores: Annotated[list[int], operator.add]
    avg_score: float


def evaluate_language(state: EssayState):
    prompt = f"""
Evaluate the LANGUAGE QUALITY of the following UPSC essay.
Give feedback and score /10.

Essay:
{state['essay']}
"""
    output = structured_model.invoke(prompt)
    return {"language_feedback": output.feedback, "individual_scores": [output.score]}


def evaluate_analysis(state: EssayState):
    prompt = f"""
Evaluate the DEPTH OF ANALYSIS of the following UPSC essay.
Give feedback and score /10.

Essay:
{state['essay']}
"""
    output = structured_model.invoke(prompt)
    return {"analysis_feedback": output.feedback, "individual_scores": [output.score]}


def evaluate_thought(state: EssayState):
    prompt = f"""
Evaluate the CLARITY OF THOUGHT of the following UPSC essay.
Give feedback and score /10.

Essay:
{state['essay']}
"""
    output = structured_model.invoke(prompt)
    return {"clarity_feedback": output.feedback, "individual_scores": [output.score]}


def final_evaluation(state: EssayState):
    prompt = f"""
Based on the following feedback:

Language:
{state['language_feedback']}

Depth of Analysis:
{state['analysis_feedback']}

Clarity of Thought:
{state['clarity_feedback']}

Write a short summary feedback.
"""

    overall_feedback = model.invoke(prompt).content
    avg_score = sum(state["individual_scores"]) / len(state["individual_scores"])

    return {"overall_feedback": overall_feedback, "avg_score": round(avg_score, 2)}


graph = StateGraph(EssayState)

graph.add_node("evaluate_language", evaluate_language)
graph.add_node("evaluate_analysis", evaluate_analysis)
graph.add_node("evaluate_thought", evaluate_thought)
graph.add_node("final_evaluation", final_evaluation)

graph.add_edge(START, "evaluate_language")
graph.add_edge(START, "evaluate_analysis")
graph.add_edge(START, "evaluate_thought")

graph.add_edge("evaluate_language", "final_evaluation")
graph.add_edge("evaluate_analysis", "final_evaluation")
graph.add_edge("evaluate_thought", "final_evaluation")

graph.add_edge("final_evaluation", END)

workflow = graph.compile()


def evaluate_essay(essay_text: str):
    initial_state = {"essay": essay_text}
    return workflow.invoke(initial_state)
