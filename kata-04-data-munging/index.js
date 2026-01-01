const fs = require("fs");

// TODO: Write a program that reads the weather.dat file and output the day number (column one) with the smallest temperature spread
const filePath = "./weather.dat";

function findSmallestTemperatureSpread(filePath) {
  fs.readFile(filePath, "utf-8", (err, data) => {
    if (err) {
      console.log("Error Reading Data:", err);
    }

    // console.log("data", data)

    const rows = data.trim().split(/\r?\n/);

    // console.log("rows", rows.length);

    const parsedData = rows.map((row) => row.trim().split(/s+/));

    console.log("parsedData:", parsedData.map(col => col.slice(0, 2)));

    const firstCol =  parsedData.map(col => col.slice(0, 2));

    // console.log("firstCol", firstCol);
  });
}

findSmallestTemperatureSpread(filePath);
