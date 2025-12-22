import React, { useEffect } from "react";
import * as THREE from "three";

export default function Hero() {
  useEffect(() => {
    const canvas = document.getElementById("background-canvas");
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);

    const geometry = new THREE.BufferGeometry();
    const particleCount = 100;
    const positions = new Float32Array(particleCount * 3);
    for (let i = 0; i < particleCount * 3; i++) {
      positions[i] = (Math.random() - 0.5) * 20;
    }
    geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    const material = new THREE.PointsMaterial({ color: 0x64ffda, size: 0.05 });
    const particles = new THREE.Points(geometry, material);
    scene.add(particles);

    camera.position.z = 5;
    function animate() {
      requestAnimationFrame(animate);
      particles.rotation.x += 0.001;
      particles.rotation.y += 0.002;
      renderer.render(scene, camera);
    }
    animate();

    const handleResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    };
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <section className="hero" id="home">
      <canvas id="background-canvas"></canvas>
      <div className="hero-content">
        <h1>See Through the Noise</h1>
        <p>
          Advanced AI-powered fact-checking and truth verification. Cut through misinformation with precision and clarity.
        </p>
        <div className="cta-container">
          <a href="#demo" className="btn btn-primary">🔍 Try Truth Lens</a>
          <a href="#features" className="btn btn-secondary">✨ Learn More</a>
        </div>
      </div>
    </section>
  );
}
