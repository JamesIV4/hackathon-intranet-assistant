"use client";
import { useEffect, useState } from "react";
import { get, set, del, keys } from "idb-keyval";

export default function Sidebar({
  onSelect,
}: {
  onSelect: (id: string | null) => void;
}) {
  const [convs, setConvs] = useState<string[]>([]);

  useEffect(() => {
    keys().then((ids) => setConvs(ids.map(String)));
  }, []);

  return (
    <aside className="w-64 bg-zinc-900 p-4 flex flex-col gap-2 border-r border-zinc-700">
      <button onClick={() => onSelect(null)} className="btn-primary">
        ＋ New Chat
      </button>
      <ul className="flex-1 overflow-y-auto">
        {convs.map((id) => (
          <li key={id} className="group flex justify-between items-center">
            <button
              onClick={() => onSelect(id)}
              className="truncate text-left w-full py-1"
            >
              {id}
            </button>
            <button
              onClick={() =>
                del(id).then(() => setConvs((cv) => cv.filter((c) => c !== id)))
              }
              className="opacity-0 group-hover:opacity-100"
            >
              …
            </button>
          </li>
        ))}
      </ul>
    </aside>
  );
}
