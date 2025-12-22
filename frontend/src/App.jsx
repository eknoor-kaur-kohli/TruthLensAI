import React from "react";
import "./styles.css";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Features from "./components/Features";
import Demo from "./components/Demo";
import Footer from "./components/Footer";

function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <Features />
      <Demo />
      <Footer />
    </>
  );
}

export default App;
