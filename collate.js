const fs = require("fs");

function dont_have(str, arr) {
  for (const i of arr) {
    if (str.includes(i)) return false;
  }
  return true;
}

function split_and_merge_single(group, spliter) {
  let ret = [];
  for (const i of group) {
    ret.push(...i.split(spliter));
  }
  return ret;
}

function split_and_merge(group, spliters) {
  let ret = group;
  for (const i of spliters) {
    ret = split_and_merge_single(ret, i);
  }
  return ret;
}

function dedup(arr) {
  return arr.filter((v, i) => arr.indexOf(v) === i);
}

function process_title(str) {
  let ret = [str];
  // Filter contents
  ret = ret.filter((x) => dont_have(x, ["○", "〇"]));
  // Split contents
  ret = split_and_merge(ret, [
    ":",
    "(",
    ")",
    "（",
    "）",
    "【",
    "】",
    "『",
    "』",
  ]);
  // Remove contents after slash, sorry Fate
  ret = ret.map((x) => x.replace(/\/.*/, ""));
  // Remove "·"
  ret = ret.map((x) => x.replace(/·/g, ""));
  // Strip space
  ret = ret.map((x) => x.trim());
  // Remove empty contents
  ret = ret.filter((x) => x !== "");
  // Remove short contents
  ret = ret.filter((x) => x.length > 2);
  // Dedup
  ret = dedup(ret);

  return ret;
}

(() => {
  let results = [];
  const list = fs.readFileSync("titles.txt").toString().split("\n");
  console.log(`Read ${list.length} lines`);
  for (const i of list) {
    results.push(...process_title(i));
  }
  console.log(`Got ${results.length} lines`);
  results = dedup(results);
  console.log(`Got ${results.length} lines after dedup`);
  fs.writeFileSync("results.txt", results.join("\n"));
})();
