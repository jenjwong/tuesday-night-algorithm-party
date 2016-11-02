
/*
 * Write a function that accepts a 2-dimensional array (that is, an array containing many same-length arrays),
 * and prints out every value found, but in a spiral from the upper left in to the center
 * Please write some form of specs, tests, or assertions for your code, and check as many edge cases as you can think of
 *
 * example:
    spiralTraversal([
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]);
    returns [1, 2, 3, 6, 9, 8, 7, 4, 5]
 */

 const spiralTraversal = function(matrix){

   const results = [];
   let startRowIndex = 0;
   let endRowIndex = matrix.length-1;
   let startColIndex = 0;
   let endColIndex = matrix[0].length-1;

   while (startRowIndex <= endRowIndex && startColIndex <= endColIndex) {

     for (let i = startColIndex; i <= endColIndex; i++) {
       results.push(matrix[startRowIndex][i]);
     }
     startRowIndex++;

     for (let j = startRowIndex; j <= endRowIndex; j++) {
       results.push(matrix[j][endColIndex]);
     }
     endColIndex--;

     if (startRowIndex <= endRowIndex) {
       for (let k = endColIndex; k >= startColIndex; k--) {
         results.push(matrix[endRowIndex][k]);
       }
       endRowIndex--;
     }

     if (startColIndex <= endColIndex) {
       for (let m = endRowIndex; m >= startRowIndex; m--) {
         results.push(matrix[m][startColIndex]);
       }
       startColIndex++;
     }

   }

   return results;
   };

 // spiralTraversal([
 //   [1,2,3],
 //   [4,5,6],
 //   [7,8,9]
 // ]);

spiralTraversal([
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [7,8,9],
  [7,8,9]
]);
//
// //
// // spiralTraversal([
// //   [1, 2, 3, 4],
// //   [5, 6, 7, 8],
// //   [9, 10, 11, 12],
// //   [13, 14, 15, 16],
// // ]);
//
