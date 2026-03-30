import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Agentes Jurídicos",
  description: "Sistema multi-agente para análise jurídica",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR">
      <body className="min-h-screen">{children}</body>
    </html>
  );
}
