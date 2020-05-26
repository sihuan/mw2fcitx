const axios = require("axios");
const fs = require("fs");

const words = [];

(async () => {
  let x = await axios.get(
    `https://zh.moegirl.org/api.php?action=query&list=allpages&format=json&aplimit=max`
  );
  while (1) {
    words.push(...x.data.query.allpages.map((x) => x.title));
    console.log(`Got ${words.length} entries`);
    fs.writeFileSync("titles.txt", words.join("\n"));
    if (x.data.continue) {
      console.log("Next:", x.data.continue.apcontinue);
      x = await axios.get(
        `https://zh.moegirl.org/api.php?action=query&list=allpages&format=json&aplimit=max&apcontinue=${encodeURIComponent(
          x.data.continue.apcontinue
        )}`
      );
    } else {
      break;
    }
  }
})();
