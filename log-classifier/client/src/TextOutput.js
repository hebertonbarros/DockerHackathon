import React, { useEffect, useState } from "react";
// import Typewriter from "react-typewriter";
import Typewriter from "typewriter-effect";
import SearchRoundedIcon from "@mui/icons-material/SearchRounded";
import SortIcon from "@mui/icons-material/Sort";

const TextOutput = (incomingData) => {
  const divStyle = { paddingBottom: "5px", display: "flex" };
  const spanStyle = { marginRight: "10px" };

  const [data, setData] = useState([]);
  const levelOrder = ["CRITICAL", "ERROR", "WARNING", "DEBUG", "INFO"];

  useEffect(() => {
    console.log("in here");
    console.log(incomingData);
    setData(incomingData.data);
  }, [incomingData]);

  console.log(data);

  const handleSortLogs = () => {
    console.log("clicked");
    // Sort the logList by level using the specified order
    const sortedData = [...data].sort((a, b) => {
      const levelA = levelOrder.indexOf(a.predicted_sentiment);
      const levelB = levelOrder.indexOf(b.predicted_sentiment);

      return levelA - levelB;
    });
    console.log(sortedData);
    setData(sortedData);
  };

  return (
    <>
      <SortIcon
        sx={{ padding: "2%", position: "absolute", float: "right" }}
        onClick={handleSortLogs}
      />
      <div
        style={{
          padding: "5%",
          marginTop: "30px"
        }}
      >
        {data.length > 0 &&
          data?.map((item, index) => {
            console.log(item.predicted_sentiment, item.Log);
            if (item.predicted_sentiment.toLowerCase() === "error")
              return (
                <div style={divStyle}>
                  <span style={{...spanStyle, fontFamily: "Apple Color Emoji" }}>
                    {"\u274C"}
                  </span>
                  {item.Log}
                </div>
              );
            else if (item.predicted_sentiment.toLowerCase() === "critical")
              return (
                <div style={divStyle}>
                  <span style={{...spanStyle, fontFamily: "Apple Color Emoji" }}>
                    {"\u2757"}
                  </span>
                  {item.Log}
                </div>
              );
            else if (item.predicted_sentiment.toLowerCase() === "warning")
              return (
                <div style={divStyle}>
                  <span style={{...spanStyle, fontFamily: "Apple Color Emoji" }}>
                    {"\u26A0"}
                  </span>
                  {item.Log}
                </div>
              );
            else if (item.predicted_sentiment.toLowerCase() === "info")
              return (
                <div style={divStyle}>
                  <span style={{...spanStyle, fontFamily: "Apple Color Emoji" }}>
                    {"\u2139"}
                  </span>
                  {item.Log}
                </div>
              );
            else if (item.predicted_sentiment.toLowerCase() === "debug")
              return (
                <div style={divStyle}>
                  <SearchRoundedIcon /> {item.Log}
                </div>
              );
            return null;
          })}
      </div>
    </>
  );
};

export default TextOutput;
