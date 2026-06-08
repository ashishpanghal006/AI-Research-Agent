import ReactMarkdown from "react-markdown";

function SectionCard({ title, content }) {
  if (!content) return null;

  return (
    <div
      className="
        bg-zinc-900
        border
        border-zinc-800
        rounded-3xl
        p-8
        mt-8
      "
    >
      <h2 className="text-3xl font-bold mb-6 text-white">
        {title}
      </h2>

      <div className="prose prose-invert max-w-none">
        <ReactMarkdown>
          {content}
        </ReactMarkdown>
      </div>
    </div>
  );
}

export default SectionCard;