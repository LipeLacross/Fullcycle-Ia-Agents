"use client";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { ChatMessage } from "@/lib/api";

interface Props {
  messages: ChatMessage[];
  isLoading?: boolean;
}

const agentColors: Record<string, string> = {
  agente_pesquisa: "bg-green-900 text-green-300",
  agente_jurisprudencia: "bg-purple-900 text-purple-300",
  agente_analise: "bg-orange-900 text-orange-300",
  orquestrador_juridico: "bg-[#ffcd00] text-black",
};

export default function MessageList({ messages, isLoading }: Props) {
  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4">
      {messages.length === 0 && (
        <p className="text-center text-gray-400 mt-10">
          Selecione um processo e envie uma pergunta para começar.
        </p>
      )}
      {messages.map((msg, i) => (
        <div
          key={i}
          className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
        >
          <div
            className={`max-w-[80%] rounded-lg p-3 ${
              msg.role === "user"
                ? "bg-[#ffcd00] text-black"
                : "bg-[rgb(40,40,40)] text-white"
            }`}
          >
            <div className={`prose prose-sm max-w-none ${msg.role === "user" ? "prose-neutral" : "prose-invert"}`}>
              <ReactMarkdown remarkPlugins={[remarkGfm]}>{msg.content}</ReactMarkdown>
            </div>
            {msg.agent_name && (
              <span
                className={`inline-block mt-2 px-2 py-0.5 rounded text-xs ${
                  agentColors[msg.agent_name] || "bg-gray-700 text-gray-300"
                }`}
              >
                {msg.agent_name}
              </span>
            )}
          </div>
        </div>
      ))}
      {isLoading && (
        <div className="flex justify-start">
          <div className="bg-[rgb(40,40,40)] text-gray-400 rounded-lg p-3 flex items-center gap-2 text-sm">
            <span className="animate-pulse">●</span>
            <span className="animate-pulse delay-75">●</span>
            <span className="animate-pulse delay-150">●</span>
            <span className="ml-1">Carregando...</span>
          </div>
        </div>
      )}
    </div>
  );
}
