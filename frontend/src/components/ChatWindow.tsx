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
    if (convId) {
      get(convId).then((h) => h && setMessages(h));
    } else {
      setMessages([]);
    }
  }, [convId]);

  // open WS with debug logs
  useEffect(() => {
    const host = window.location.hostname;
    const protocol = window.location.protocol === "https:" ? "wss" : "ws";
    const socket = new WebSocket(`${protocol}://${host}:8000/ws`);

    socket.onopen = () => console.log("[WS] open");
    socket.onmessage = (e) => {
      console.log("[WS] message", e.data);
      setMessages((m) => [...m, { role: "bot", content: e.data }]);
    };
    socket.onclose = (e) => console.log("[WS] closed", e);
    socket.onerror = (e) => console.error("[WS] error", e);

    wsRef.current = socket;
    return () => {
      console.log("[WS] closing");
      socket.close();
    };
  }, []);

  const send = (text: string) => {
    console.log("[send] readyState", wsRef.current?.readyState);
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      console.log("[send] sending", text);
      setMessages((m) => [...m, { role: "user", content: text }]);
      wsRef.current.send(text);
    } else {
      console.warn("[send] WS not open, reconnecting...");
      const host = window.location.hostname;
      const protocol = window.location.protocol === "https:" ? "wss" : "ws";
      const socket = new WebSocket(`${protocol}://${host}:8000/ws`);

      socket.onopen = () => {
        console.log("[reconnect] open, sending", text);
        setMessages((m) => [...m, { role: "user", content: text }]);
        socket.send(text);
      };
      socket.onmessage = (e) => {
        console.log("[reconnect] message", e.data);
        setMessages((m) => [...m, { role: "bot", content: e.data }]);
      };
      socket.onclose = (e) => console.log("[reconnect] closed", e);
      socket.onerror = (e) => console.error("[reconnect] error", e);

      wsRef.current = socket;
    }
  };

  // persist chats
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
