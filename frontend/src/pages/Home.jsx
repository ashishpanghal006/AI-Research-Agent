import { useState } from "react";

import api from "../services/api";

import Header from "../components/Header";
import SearchBox from "../components/SearchBox";
import ProgressSteps from "../components/ProgressSteps";
import SectionCard from "../components/SectionCard";
import SourcesList from "../components/SourcesList";
import ReportActions from "../components/ReportActions";

function Home() {

  const [query, setQuery] = useState("");

  const [loading, setLoading] = useState(false);

  const [plan, setPlan] = useState("");

  const [analysis, setAnalysis] = useState("");

  const [report, setReport] = useState("");

  const [sources, setSources] = useState([]);

  const runResearch = async () => {

    if (!query) return;

    try {

      setLoading(true);

      setPlan("");
      setAnalysis("");
      setReport("");
      setSources([]);

      const response = await api.post(
        "/research",
        {
          query
        }
      );

      setPlan(response.data.plan);

      setAnalysis(response.data.analysis);

      setReport(response.data.report);

      setSources(response.data.sources);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="min-h-screen bg-black text-white">

      <div className="max-w-7xl mx-auto px-6 py-10">

        <Header />

        <SearchBox
          query={query}
          setQuery={setQuery}
          runResearch={runResearch}
          loading={loading}
        />

        <ProgressSteps
          loading={loading}
          report={report}
        />

        <SectionCard
          title="Research Plan"
          content={plan}
        />

        <SourcesList
          sources={sources}
        />

        <SectionCard
          title="Analysis"
          content={analysis}
        />

        <SectionCard
          title="Final Report"
          content={report}
        />

        <ReportActions
          report={report}
        />

      </div>

    </div>
  );
}

export default Home;