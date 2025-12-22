import React, { useRef } from "react";
import useFadeInOnScroll from "../hooks/useFadeInOnScroll";

export default function Features() {
  const featureRefs = [useRef(), useRef(), useRef(), useRef(), useRef(), useRef()];
  
  featureRefs.forEach((ref, i) => useFadeInOnScroll(ref, i * 0.2));

  return (
    <section className="features" id="features">
      <div className="container">
        <h2 className="section-title fade-in fade-delay-1">Powerful Truth Detection</h2>
        <div className="features-grid">
          {featureRefs.map((ref, i) => (
            <div className="feature-card fade-delay-1" key={i} ref={ref}>
              <div className="feature-icon">{["🧠","⚡","🌐","📊","🔒","🎯"][i]}</div>
              <h3>{["AI-Powered Analysis","Real-Time Verification","Multi-Source Cross-Check","Detailed Reports","Privacy First","Context Aware"][i]}</h3>
              <p>{[
                "Advanced machine learning detects inconsistencies.",
                "Instant fact-checking with confidence scores.",
                "Checks across trusted sources for accuracy.",
                "Receive transparent reports with citations.",
                "Your data is processed securely and never stored.",
                "Understands nuance for better truth detection."
              ][i]}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
