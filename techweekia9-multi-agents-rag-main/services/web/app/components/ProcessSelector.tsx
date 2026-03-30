"use client";

import { useEffect, useState } from "react";
import type { Process } from "@/lib/api";

interface Props {
  selectedId: string;
  onSelect: (processId: string) => void;
}

export default function ProcessSelector({ selectedId, onSelect }: Props) {
  const [processes, setProcesses] = useState<Process[]>([]);

  useEffect(() => {
    fetch("/api/chat?action=processes")
      .then((res) => res.json())
      .then(setProcesses)
      .catch(console.error);
  }, []);

  return (
    <select
      value={selectedId}
      onChange={(e) => onSelect(e.target.value)}
      className="w-full p-2 bg-[rgb(40,40,40)] border border-[rgb(60,60,60)] rounded-lg text-sm text-white
                 focus:outline-none focus:ring-2 focus:ring-[#ffcd00]"
    >
      <option value="">Selecione um processo...</option>
      {processes.map((p) => (
        <option key={p.id} value={p.id}>
          {p.name} ({p.case_type})
        </option>
      ))}
    </select>
  );
}
