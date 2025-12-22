import React, { useState } from "react";
import { analyzeText } from "../api";
import ResultsCard from "./ResultsCard";

export default function Demo() {
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function handleAnalyze() {
    if (!input) return;
    setLoading(true);
    try {
      const data = await analyzeText(input);
      setResult(data);
    } catch (err) {
      alert("Error: " + err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="demo" id="demo">
      <div className="container">
        <div className="demo-container">
          <h2 className="section-title">Try Truth Lens Now</h2>
          <p>Enter any claim or news article to see Truth Lens in action.</p>
          <div className="input-container">
            <textarea
              className="demo-input"
              rows="4"
              placeholder="Paste text here..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
            ></textarea>
          </div>
          <button className="analyze-btn" onClick={handleAnalyze} disabled={loading}>
            {loading ? "🔄 Analyzing..." : "🔍 Analyze with Truth Lens"}
          </button>
          {result && <ResultsCard data={result} />}
        </div>
      </div>
    </section>
  );
}
