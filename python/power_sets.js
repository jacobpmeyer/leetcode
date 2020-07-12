function powerSets(array) {
  const subs = [[]];
  array.forEach((element, i) => {
    const end = subs.length;
    for (let i = 0; i < end; i++) {
      const currentSub = subs[i];
      subs.push(currentSub.concat([element]));
    }
  });
  return subs;
}
