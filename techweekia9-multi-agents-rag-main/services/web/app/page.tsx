import Chat from "./components/Chat";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center">
      <div className="w-full max-w-3xl flex flex-col h-screen">
        <header className="p-4 border-b border-[rgb(50,50,50)]">
          <h1 className="text-xl font-bold text-white">Agentes Jurídicos</h1>
          <p className="text-sm text-gray-400">Sistema multi-agente de análise jurídica com IA</p>
        </header>
        <Chat />
      </div>
    </main>
  );
}
