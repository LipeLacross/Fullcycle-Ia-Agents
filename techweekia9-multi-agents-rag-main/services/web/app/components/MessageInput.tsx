"use client";

import { useState } from "react";

interface Props {
  onSend: (message: string) => void;
  disabled: boolean;
  isLoading?: boolean;
}

export default function MessageInput({ onSend, disabled, isLoading }: Props) {
  const [input, setInput] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || disabled) return;
    onSend(input.trim());
    setInput("");
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 border-t border-[rgb(50,50,50)]">
      <div className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Digite sua pergunta sobre o processo..."
          disabled={disabled}
          className="flex-1 p-3 bg-[rgb(40,40,40)] border border-[rgb(60,60,60)] rounded-lg text-white placeholder-gray-500
                     focus:outline-none focus:ring-2 focus:ring-[#ffcd00]
                     disabled:opacity-50"
        />
        <button
          type="submit"
          disabled={disabled || !input.trim()}
          className="px-6 py-3 bg-[#ffcd00] text-black rounded-lg font-medium
                     hover:bg-yellow-300 disabled:opacity-40 disabled:cursor-not-allowed
                     transition-colors"
        >
          {isLoading ? "Enviando..." : "Enviar"}
        </button>
      </div>
    </form>
  );
}
