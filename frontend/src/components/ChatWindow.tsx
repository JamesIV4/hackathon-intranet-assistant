"use client";
import { useEffect, useRef, useState } from "react";
import { get, set } from "idb-keyval";
import { motion } from "framer-motion";

export default function ChatWindow({ convId }: { convId: string | null }) {
  const [messages, setMessages] = useState<
    { role: "user" | "bot"; content: string }[]
  >([]);
  const wsRef = useRef<WebSocket>(null);

  // load history
  useEffect(() => {
    if (convId) get(convId).then((h) => h && setMessages(h));
    else setMessages([]);
  }, [convId]);

  // open ws once
  useEffect(() => {
    wsRef.current = new WebSocket("ws://localhost:8000/ws");
    return () => wsRef.current?.close();
  }, []);

  const send = (text: string) => {
    setMessages((m) => [...m, { role: "user", content: text }]);
    wsRef.current?.send(text);
  };

  useEffect(() => {
    wsRef.current!.onmessage = (e) =>
      setMessages((m) => [...m, { role: "bot", content: e.data }]);
  }, []);

  // persist
  useEffect(() => {
    if (convId) set(convId, messages);
  }, [messages]);

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.map((m, i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={m.role === "user" ? "text-right" : "text-left"}
          >
            <div className="inline-block px-3 py-2 rounded-lg bg-zinc-800">
              {m.content}
            </div>
          </motion.div>
        ))}
      </div>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          const t = (e.target as any).msg.value.trim();
          if (t) {
            send(t);
            (e.target as any).msg.value = "";
          }
        }}
        className="p-4 border-t border-zinc-700"
      >
        <input
          name="msg"
          className="w-full bg-zinc-800 p-3 rounded-lg"
          placeholder="Ask me about the wiki…"
          autoComplete="off"
        />
      </form>
    </div>
  );
}
