export interface Process {
  id: string;
  name: string;
  case_type: string;
  status: string;
}

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
  agent_name?: string;
}

export interface ChatResponseData {
  response: string;
  agent_name: string;
}

export async function fetchProcesses(): Promise<Process[]> {
  const res = await fetch("/api/chat?action=processes");
  if (!res.ok) throw new Error("Failed to fetch processes");
  return res.json();
}

export async function sendMessage(
  message: string,
  sessionId: string,
  processId: string
): Promise<ChatResponseData> {
  const res = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message,
      session_id: sessionId,
      user_id: "default_user",
      process_id: processId,
    }),
  });
  if (!res.ok) throw new Error("Failed to send message");
  return res.json();
}
