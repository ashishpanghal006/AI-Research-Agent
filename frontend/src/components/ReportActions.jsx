import { Copy } from "lucide-react";

function ReportActions({ report }) {
  if (!report) return null;

  const copyReport = async () => {
    await navigator.clipboard.writeText(report);

    alert("Report copied");
  };

  return (
    <div className="flex justify-end mt-6">
      <button
        onClick={copyReport}
        className="
          flex
          items-center
          gap-2
          bg-zinc-800
          hover:bg-zinc-700
          px-5
          py-3
          rounded-2xl
          transition
        "
      >
        <Copy size={18} />

        Copy Report
      </button>
    </div>
  );
}

export default ReportActions;