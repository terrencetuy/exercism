// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Calculates the total bird count.
 *
 * @param {number[]} birdsPerDay
 * @returns {number} total bird count
 */
export function totalBirdCount(birdsPerDay) {
  let birdCount = 0;
  for(let i = 0; i < birdsPerDay.length; i++){
    birdCount += birdsPerDay[i];
  }
  return birdCount;
}

/**
 * Calculates the total number of birds seen in a specific week.
 *
 * @param {number[]} birdsPerDay
 * @param {number} week
 * @returns {number} birds counted in the given week
 */
export function birdsInWeek(birdsPerDay, week) {
  const startDay = 7 * (week - 1);
  const endDay = 7 * week;

  let birdCount = 0
  for(let i = startDay; i < endDay; i++){
    birdCount += birdsPerDay[i];
  }
  return birdCount;
}

/**
 * Fixes the counting mistake by increasing the bird count
 * by one for every second day.
 *
 * @param {number[]} birdsPerDay
 * @returns {void} should not return anything
 */
export function fixBirdCountLog(birdsPerDay) {
  let birdCount = 0;
  for(let i = 0; i < birdsPerDay.length; i+=2){
    birdsPerDay[i]++;
  }
  return birdsPerDay;
}
