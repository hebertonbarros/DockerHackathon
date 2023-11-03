import React, { useEffect, useState } from "react";
import Papa from "papaparse";
import axios from "axios";
import backgroundImage from "./assets/background.png";
import TextOutput from "./TextOutput";
import SortIcon from "@mui/icons-material/Sort";

const LogClassifier = () => {
  const [showOutputArea, setShowOutputArea] = useState(false);
  const [showTextBox, setShowTextBox] = useState(false);
  const [displayData, setDisplayData] = useState([]);
  const [sortData, setSortData] = useState([]);
  const [showSortData, setShowSortData] = useState(false);
  const [inputData, setInputData] = useState([]);

  const levelOrder = ["CRITICAL", "ERROR", "WARNING", "DEBUG", "INFO"];


  useEffect(() => {
    if (inputData.length > 0) {
      fetchData();
    }
  }, [inputData]);

  useEffect(() => {
    if (showOutputArea) {
      const timer = setTimeout(() => {
        setShowTextBox(true);
      }, 5000);

      // Clear the timeout to prevent it from firing if the component unmounts
      return () => clearTimeout(timer);
    }
  }, [showOutputArea]);

  async function readCSVFile(file) {
    return new Promise((resolve, reject) => {
      Papa.parse(file, {
        complete: (result) => {
          resolve(result.data);
        },
        header: true, // Set this to true if the CSV file has a header row
        skipEmptyLines: true,
        error: (error) => {
          reject(error.message);
        },
      });
    });
  }

  const fetchData = async () => {
    try {
      // Send a GET request to the Flask API endpoint
      // const response = await axios.get("http://127.0.0.1:3010/api/analyzeLogs");
      const response = await axios.post(
        "http://3.143.226.233:3010/api/analyzeLogs",
        { log_data: inputData }
      );

      // Access the JSON data from the response
      const data = response.data.result;

      // Use the data as needed
      console.log("Data from Flask API:", JSON.parse(data));
      setDisplayData(JSON.parse(data));

      // You can perform further actions with the data here
    } catch (error) {
      // Handle any errors that may occur during the request
      console.error("Error fetching data:", error);
    }
  };

  async function handleFileUpload(event) {
    const file = event.target.files[0];

    try {
      const csvData = await readCSVFile(file);
      console.log("CSV Data:", csvData);
      setInputData(csvData);
      setShowOutputArea(true);
      // You can now use 'csvData' in your React component or process it as needed.
    } catch (error) {
      console.error("Error reading CSV file:", error);
    }
  }

  const handleSortLogs = () => {

    // Sort the logList by level using the specified order
    const sortedData = displayData.sort((a, b) => {
      const levelA = levelOrder.indexOf(a.predicted_sentiment);
      const levelB = levelOrder.indexOf(b.predicted_sentiment);

      return levelA - levelB;
    });
    setSortData(sortedData)
  };

  return (
    <>
      <div
        style={{
          position: "relative",
          height: "100vh",
          width: "100vw",
          display: "flex",
          alignContent: "center",
          justifyContent: "center",
          alignItems: "center",
          backgroundImage: `url(${backgroundImage})`,
          backgroundRepeat: "no-repeat",
          backgroundSize: "cover",
          paddingLeft: "2%",
          color: "#D5D7DF",
        }}
      >
        {/* Header */}
        <div
          style={{
            width: "30%",
            position: "absolute",
            left: showOutputArea ? "60px" : "50%",
            transform: showOutputArea ? "translateX(0)" : "translateX(-50%)",
            transition: "left 0.9s, transform 0.9s",
            paddingRight: showTextBox ? "20%" : "0",
          }}
        >
          <h2>Docker Log Sentiment Analyzer 🚀</h2>
          <input
            type="file"
            accept=".csv"
            onChange={handleFileUpload}
            style={{
              border: "1px solid #D5D7DF",
              padding: "10px",
              borderRadius: "10px",
            }}
          />
        </div>
        <br />

        {/* Log output area */}
        {showOutputArea ? (
          <div
            style={{
              width: "60%",
              height: "90vh",
              fontFamily: "monospace",
              color: "white",
              border: "1px solid #D5D7DF",
              borderRadius: "10px",
              position: "absolute",
              right: "60px",
              overflow: "scroll",
              opacity: showTextBox ? 1 : 0,
              transition: "opacity 1s",
            }}
          >
            <SortIcon
              sx={{ padding: "2%", position: "absolute", float: "right" }}
              onClick={handleSortLogs}
            />
            <TextOutput data={showSortData ? sortData : displayData} />
          </div>
        ) : (
          <></>
        )}
      </div>
    </>
  );
};

export default LogClassifier;
