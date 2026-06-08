function SearchBox({
  query,
  setQuery,
  runResearch,
  loading
}) {
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-6">
      <textarea
        rows={4}
        placeholder="Research any topic..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="
          w-full
          bg-transparent
          outline-none
          resize-none
          text-zinc-100
          placeholder:text-zinc-500
        "
      />

      <div className="flex justify-end mt-4">
        <button
          onClick={runResearch}
          disabled={loading}
          className="
            bg-blue-600
            hover:bg-blue-500
            transition
            px-6
            py-3
            rounded-2xl
            font-medium
            disabled:opacity-50
          "
        >
          {loading ? "Researching..." : "Start Research"}
        </button>
      </div>
    </div>
  );
}

export default SearchBox;