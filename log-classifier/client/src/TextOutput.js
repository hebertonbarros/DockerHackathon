import React from "react";
// import Typewriter from "react-typewriter";
import Typewriter from "typewriter-effect";

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
        if (item.sentiment === "error")
          return (
            <div style={divStyle}>
              <span>
                <Typewriter
                  onInit={(typewriter) => {
                    typewriter.typeString("❌ ").start();
                    typewriter.typeString(item.log).start();
                  }}
                />
              </span>
            </div>
          );
        else if (item.sentiment === "warning")
          return (
            <div style={divStyle}>
              <Typewriter
                onInit={(typewriter) => {
                  typewriter.typeString("🛑 ").start();
                  typewriter.typeString(item.log).start();
                }}
              />
            </div>
          );
        else if (item.sentiment === "info")
          return (
            <div style={divStyle}>
              <Typewriter
                onInit={(typewriter) => {
                  typewriter.typeString("ℹ️ ").start();
                  typewriter.typeString(item.log).start();
                }}
              />
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
