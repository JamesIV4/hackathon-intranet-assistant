"use client";

import Sidebar from "@/components/Sidebar";
import ChatWindow from "@/components/ChatWindow";
import { useState } from "react";
export default function Page() {
  const [conv, setConv] = useState<string | null>(null);

  return (
    <div className="flex h-screen text-zinc-200 bg-zinc-950">
      <Sidebar onSelect={setConv} />
      <ChatWindow convId={conv} />
    </div>
  );
}
