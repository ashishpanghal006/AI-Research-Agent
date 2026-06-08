import {
  ExternalLink
} from "lucide-react";

function SourcesList({ sources }) {
  if (!sources?.length) return null;

  const uniqueSources = Array.from(
    new Map(
      sources.map((item) => [item.url, item])
    ).values()
  );

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
        Sources Used
      </h2>

      <div className="space-y-4">
        {uniqueSources.map((source, index) => (
          <a
            key={index}
            href={source.url}
            target="_blank"
            rel="noreferrer"
            className="
              flex
              items-center
              justify-between
              bg-zinc-950
              border
              border-zinc-800
              rounded-2xl
              p-4
              hover:border-blue-500
              transition
            "
          >
            <div>
              <p className="text-zinc-100 font-medium">
                {source.title}
              </p>

              <p className="text-zinc-500 text-sm truncate max-w-xl">
                {source.url}
              </p>
            </div>

            <ExternalLink className="text-zinc-500" />
          </a>
        ))}
      </div>
    </div>
  );
}

export default SourcesList;