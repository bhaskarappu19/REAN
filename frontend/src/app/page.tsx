"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {

  const [file, setFile] = useState<File | null>(null);

  const [result, setResult] = useState<any>(null);

  const uploadResume = async () => {

    if (!file) {
      alert("Please select a PDF");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

      const res = await axios.post(
        "https://rean-backend-27g4.onrender.com/upload",
        formData
      );

      setResult(res.data);

    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="p-10">

      <h1 className="text-4xl font-bold mb-5">
        AI Resume Analyzer
      </h1>

      <input
        type="file"
        onChange={(e) => {
          if (e.target.files) {
            setFile(e.target.files[0]);
          }
        }}
      />

      <button
        onClick={uploadResume}
        className="bg-black text-white px-4 py-2 ml-4"
      >
        Upload Resume
      </button>

      {result && (
        <div className="mt-10">

          <h2 className="text-2xl font-bold">
            ATS Score: {result.ats_score}/100
          </h2>

          <div className="mt-5">
            <h3 className="font-bold">
              Skills Found
            </h3>

            <ul>
              {result.skills_found.map(
                (skill: string, index: number) => (
                  <li key={index}>
                    ✅ {skill}
                  </li>
                )
              )}
            </ul>
          </div>

          <div className="mt-5">
            <h3 className="font-bold">
              Missing Skills
            </h3>

            <ul>
              {result.missing_skills.map(
                (skill: string, index: number) => (
                  <li key={index}>
                    ❌ {skill}
                  </li>
                )
              )}
            </ul>
          </div>

          <div className="mt-5">
            <h3 className="font-bold">
              Suggestions
            </h3>

            <ul>
              {result.suggestions.map(
                (item: string, index: number) => (
                  <li key={index}>
                    • {item}
                  </li>
                )
              )}
            </ul>
          </div>

        </div>
      )}

    </div>
  );
}