"use client";

import { useState, useCallback, useRef, useEffect } from "react";
import ProcessSelector from "./ProcessSelector";
import MessageList from "./MessageList";
import MessageInput from "./MessageInput";
import type { ChatMessage } from "@/lib/api";

export default function Chat() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [processId, setProcessId] = useState("");
  const [sessionId, setSessionId] = useState(() => crypto.randomUUID());
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleProcessChange = useCallback((newProcessId: string) => {
    setProcessId(newProcessId);
    setSessionId(crypto.randomUUID());
    setMessages([]);
  }, []);

  const handleSend = useCallback(
    async (message: string) => {
      if (!processId) return;

      const userMsg: ChatMessage = { role: "user", content: message };
      setMessages((prev) => [...prev, userMsg]);
      setIsLoading(true);

      try {
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

        if (!res.ok) throw new Error("Request failed");

        const data = await res.json();
        const assistantMsg: ChatMessage = {
          role: "assistant",
          content: data.response,
          agent_name: data.agent_name,
        };
        setMessages((prev) => [...prev, assistantMsg]);
      } catch {
        setMessages((prev) => [
          ...prev,
          { role: "assistant", content: "Erro ao processar a mensagem. Tente novamente." },
        ]);
      } finally {
        setIsLoading(false);
      }
    },
    [processId, sessionId]
  );

  return (
    <>
      <div className="p-4 border-b border-gray-800">
        <ProcessSelector selectedId={processId} onSelect={handleProcessChange} />
      </div>
      <MessageList messages={messages} isLoading={isLoading} />
      <div ref={messagesEndRef} />
      <MessageInput onSend={handleSend} disabled={isLoading || !processId} isLoading={isLoading} />
    </>
  );
}
