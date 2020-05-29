var substringMatcher = function (strs) {
  return function findMatches(q, cb) {
    var matches, substringRegex;

    // an array that will be populated with substring matches
    matches = [];

    // regex used to determine if a string contains the substring `q`
    substrRegex = new RegExp(q, "i");

    // iterate through the pool of strings and for any string that
    // contains the substring `q`, add it to the `matches` array
    $.each(strs, function (i, str) {
      if (substrRegex.test(str)) {
        matches.push(str);
      }
    });

    cb(matches);
  };
};

var nodes = [
  "Balmora",
  "Gnisis",
  "Vivec",
  "Molag Mar",
  "Suran",
  "Tel Mora",
  "Seyda Neen",
  "Vulkhel Guard",
  "Khenarthi's Roost",
  "Skywatch",
  "Haven",
  "Daggerfall",
  "Stros M'Kai",
  "Betnikh",
  "Wayrest",
  "Sentinel",
  "Bleakrock Isle",
  "Davon's Watch",
  "Dhalmora",
  "Alten Corimont",
  "Windhelm",
  "Abah's Landing",
  "Woodhearth",
  "Anvil",
  "Shimmerene",
  "Murkmire",
  "Mournhold",
  "Elden Root",
  "Rawl'kha",
  "Vulkwasten",
  "Shornhelm",
  "Stormhold",
  "Evermore",
  "Riften",
  "Sadrith Mora",
  "Alinor",
  "Orsinium",
  "Belkarth",
];

// constructs the suggestion engine
var nodes = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.whitespace,
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  // `states` is an array of state names defined in "The Basics"
  local: nodes,
});

$("#bloodhound .typeahead").typeahead(
  {
    hint: true,
    highlight: true,
    minLength: 1,
  },
  {
    name: "nodes",
    source: nodes,
  }
);
