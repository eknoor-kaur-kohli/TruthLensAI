const API_BASE = process.env.REACT_APP_API_BASE || "http://127.0.0.1:5001";

export async function analyzeText(text) {
  const resp = await fetch(`${API_BASE}/analyze`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({ text })
  });
  return resp.json();
}
