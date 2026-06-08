import { BrainCircuit } from "lucide-react";

function Header() {
  return (
    <div className="flex items-center gap-3 mb-10">
      <div className="bg-blue-600 p-3 rounded-2xl">
        <BrainCircuit className="w-6 h-6 text-white" />
      </div>

      <div>
        <h1 className="text-4xl font-bold text-white">
          AI Research Agent
        </h1>

        <p className="text-zinc-400 mt-1">
          Multi-Agent Research System powered by LangGraph
        </p>
      </div>
    </div>
  );
}

export default Header;