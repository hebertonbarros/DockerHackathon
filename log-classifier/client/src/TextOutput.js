import React from "react";
// import Typewriter from "react-typewriter";
import Typewriter from "typewriter-effect";
import SearchRoundedIcon from '@mui/icons-material/SearchRounded';

function TextOutput({ data }) {
  const divStyle = { paddingBottom: "5px", display: "flex" };
  const spanStyle = { marginRight: "10px" };

  return (
    <div
      style={{
        padding: "5%",
      }}
    >
      {data?.map((item, index) => {
        console.log(item.predicted_sentiment, item.Log);
        if (item.predicted_sentiment.toLowerCase() === "error")
          return (
            <div style={divStyle}>
              <span style={{ fontFamily: "Apple Color Emoji" }}>
                <Typewriter
                  onInit={(typewriter) => {
                    typewriter.typeString("\u274C").start();
                  }}
                />
              </span>
              <span>
                <Typewriter
                  onInit={(typewriter) => {
                    typewriter.typeString(item.Log).start();
                  }}
                />
              </span>
            </div>
          );
        else if (item.predicted_sentiment.toLowerCase() === "critical")
          return (
            <div style={divStyle}>
              <span style={{ fontFamily: "Apple Color Emoji" }}>
                <Typewriter
                  onInit={(typewriter) => {
                    typewriter.typeString("\u2757").start();
                  }}
                />
              </span>
              <span>
                <Typewriter
                  onInit={(typewriter) => {
                    typewriter.typeString(item.Log).start();
                  }}
                />
              </span>
            </div>
          );
        else if (item.predicted_sentiment.toLowerCase() === "warning")
          return (
            <div style={divStyle}>
              <span style={{ fontFamily: "Apple Color Emoji" }}>
                <Typewriter
                  onInit={(typewriter) => {
                    typewriter.typeString("\u26A0").start();
                  }}
                />
              </span>
              <span>
                <Typewriter
                  onInit={(typewriter) => {
                    typewriter.typeString(item.Log).start();
                  }}
                />
              </span>
            </div>
          );
        else if (item.predicted_sentiment.toLowerCase() === "info")
          return (
            <div style={divStyle}>
              <span style={{ fontFamily: "Apple Color Emoji" }}>
                <Typewriter
                  onInit={(typewriter) => {
                    typewriter.typeString("\u2139").start();
                  }}
                />
              </span>
              <span>
                <Typewriter
                  onInit={(typewriter) => {
                    typewriter.typeString(item.Log).start();
                  }}
                />
              </span>
            </div>
          );
        else if (item.predicted_sentiment.toLowerCase() === "debug")
          return (
            <div style={divStyle}>
              <span>
                <SearchRoundedIcon />
              </span>
              <span>
                <Typewriter
                  onInit={(typewriter) => {
                    typewriter.typeString(item.Log).start();
                  }}
                />
              </span>
            </div>
          );
        return null;
      })}
    </div>
  );
}

export default TextOutput;

/**
 * 
 * if (item.sentiment === "error")
          return (
            <div key={index} style={{ color: "red" }}>
              {item.log}
            </div>
          );
        else if (item.sentiment === "info")
          return (
            <div key={index} style={{ color: "blue" }}>
              {item.log}
            </div>
          );
        else if (item.sentiment === "warning")
          return (
            <div key={index} style={{ color: "orange" }}>
              {item.log}
            </div>
          );
 */
