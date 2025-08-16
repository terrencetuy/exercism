/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(remainingTime) {
  switch(remainingTime) {
    case undefined:
      return 'You forgot to set the timer.';
    case 0:
      return 'Lasagna is done.';
  }
  return 'Not done, please wait.';
}

export function preparationTime(layers, avgPrepTimePerLayer=2) {
  return layers.length * avgPrepTimePerLayer;
}

export function quantities(layers) {
  return {
    noodles: 50 * layers.filter((layer) => layer === 'noodles').length,
    sauce: 0.2 * layers.filter((layer) => layer === 'sauce').length
  };
}

export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList[friendsList.length -1])
}

export function scaleRecipe(recipe, portions) {
  const scaledRecipe = {};
  for (const ingredient in recipe) {
    scaledRecipe[ingredient] = recipe[ingredient] * portions / 2;
  }
  return scaledRecipe;
}