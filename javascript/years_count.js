// people is an array
const countYears = (people) => {
  const maxDeath = Math.max(...people.map((person) => person[1]));
  const minBirth = Math.min(...people.map((person) => person[0]));

  let years = {};
  people.forEach((person) => {
    if (!years[person[0]]) years[person[0]] = 0;
    years[person[0]]++;
    if (!years[person[1] + 1]) years[person[1] + 1] = 0;
    years[person[1] + 1]--;
  });

  let alivePeople = years[minBirth];
  let mostYears = [minBirth];

  console.log(maxDeath, minBirth);

  for (let i = minBirth + 1; i <= maxDeath + 1; i++) {
    // if (i === 1910) console.log("1910", "this is the log");

    if (years[i]) alivePeople += years[i];
    years[i] = alivePeople;
    const lastYear = mostYears[mostYears.length - 1];
    if (years[lastYear] < years[i]) mostYears = [i];
    if (years[lastYear] === years[i]) mostYears.push(i);
  }

  return mostYears;
};

console.log(
  countYears([
    [1910, 1950],
    [1900, 1951],
    [1955, 2000],
  ])
);
