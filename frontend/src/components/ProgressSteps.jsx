import {
  CheckCircle2,
  Loader2
} from "lucide-react";

const steps = [
  "Planning",
  "Researching",
  "Analyzing",
  "Writing Report"
];

function ProgressSteps({ loading, report }) {
  return (
    <div className="grid md:grid-cols-4 gap-4 mt-8">
      {steps.map((step, index) => (
        <div
          key={step}
          className="
            bg-zinc-900
            border
            border-zinc-800
            rounded-2xl
            p-4
          "
        >
          <div className="flex items-center gap-3">
            {loading ? (
              <Loader2 className="animate-spin text-blue-500" />
            ) : report ? (
              <CheckCircle2 className="text-green-500" />
            ) : (
              <div className="w-5 h-5 rounded-full border border-zinc-600" />
            )}

            <span className="text-zinc-200 font-medium">
              {step}
            </span>
          </div>
        </div>
      ))}
    </div>
  );
}

export default ProgressSteps;