import React from "react";

export default function ResultsCard({ data }) {
  const { claim, result } = data;
  return (
    <div className="result-container" style={{ display: "block" }}>
      <h3>Analysis Results:</h3>
      <p><strong>Claim:</strong> {claim}</p>
      <p><strong>Verdict:</strong> {result.verdict} ({Math.round(result.confidence*100)}%)</p>
      <div>
        <strong>Evidence:</strong>
        <ul>
          {(result.evidence || []).map((e) => (
            <li key={e.id}>
              <a href={e.url} target="_blank" rel="noreferrer">{e.url}</a>
              <div>{e.excerpt}</div>
            </li>
          ))}
        </ul>
      </div>
      <div>
        <strong>Micro-lesson:</strong> {result.micro_lesson}
      </div>
    </div>
  );
}
