import { NextRequest, NextResponse } from "next/server";

const AGENTS_API_URL = process.env.AGENTS_API_URL || "http://localhost:8000";

export async function GET() {
  const res = await fetch(`${AGENTS_API_URL}/processes`);
  const data = await res.json();
  return NextResponse.json(data);
}

export async function POST(request: NextRequest) {
  const body = await request.json();

  const res = await fetch(`${AGENTS_API_URL}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    const error = await res.text();
    return NextResponse.json({ error }, { status: res.status });
  }

  const data = await res.json();
  return NextResponse.json(data);
}
