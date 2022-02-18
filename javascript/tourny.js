function tournamentWinner(competition, results) {
  const records = {}
  let winner = competition[0][0]
  for (let i = 0; i < results.length; i++) {
    const home = competition[i][1]
    const away = competition[i][0]
    if (records[home] === undefined) records[home] = 0;
    if (records[away] === undefined) records[away] = 0;

    let currentChamp = ""
    if (results[i] === 1) {
      records[away]++
			currentChamp = away
    } else {
      records[home]++
      currentChamp = home
    }

    if (records[currentChamp] >= records[winner]) {
      winner = currentChamp
    }
  }
  return winner
}
