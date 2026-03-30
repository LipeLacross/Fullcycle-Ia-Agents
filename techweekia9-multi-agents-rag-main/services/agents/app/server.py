from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types as genai_types

from agents.root_agent import root_agent
from app import db

app = FastAPI(title="Legal Agents API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ADK setup
APP_NAME = "legal_agents"
session_service = InMemorySessionService()
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)


class ChatRequest(BaseModel):
    message: str
    session_id: str
    user_id: str = "default_user"
    process_id: str


class ChatResponse(BaseModel):
    response: str
    agent_name: str


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """Send a message to the agent system."""

    # Validate process exists
    process = db.get_process(req.process_id)
    if not process:
        raise HTTPException(status_code=404, detail="Process not found")

    # Get or create session
    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=req.user_id,
        session_id=req.session_id,
    )

    if session is not None:
        # If process changed, force a new session
        if session.state.get("current_process_id") != req.process_id:
            session = None

    if session is None:
        session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=req.user_id,
            session_id=req.session_id,
            state={
                "current_process_id": req.process_id,
                "current_process_name": process["name"],
            },
        )

    # Run the agent
    content = genai_types.Content(
        role="user",
        parts=[genai_types.Part(text=req.message)]
    )

    final_response = ""
    agent_name = "orquestrador_juridico"

    async for event in runner.run_async(
        user_id=req.user_id,
        session_id=req.session_id,
        new_message=content,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            final_response = event.content.parts[0].text
            agent_name = event.author

    if not final_response:
        final_response = "Desculpe, não consegui processar sua solicitação."

    return ChatResponse(response=final_response, agent_name=agent_name)


@app.get("/processes")
async def list_processes():
    """List all available processes."""
    processes = db.list_processes()
    if processes is None:
        raise HTTPException(status_code=500, detail="Failed to fetch processes")
    return processes


@app.post("/ingest")
async def trigger_ingestion():
    """Trigger mock data ingestion."""
    from ingestion.ingest import ingest_mock_data
    result = ingest_mock_data()
    return {"status": "ok", "detail": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
