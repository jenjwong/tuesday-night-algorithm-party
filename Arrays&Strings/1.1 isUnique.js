 
 // Is Unique: Implement an algorithm to determine if a string has all unique characters. 
 // What if you cannot use additional data structures? 
 
 
 // linear time and linear space complexity
 
 const isUnique = (string) => {
   let lettersFound = {};
   
   for (let i = 0; i < string.length; i++) {
     if (lettersFound[string[i]]) {
       return false;
     }
     lettersFound[string[i]] = true;
   }
   return true;
 };
 
 
 isUnique('abc') // true
 isUnique('aaa') // false
 isUnique('') // true
 isUnique('Aa') // true
 
 
 
 // quadratic time and constant space complexity
 
 const isUnique = (string) => {
  for (let i = 0; i < string.length; i++) {
    for (let j = 0; j < string.length; j++) {
      if (string[i] === string[j] && i !== j) {
        return false;
      }
    }
  }
  return true;
};


isUnique('abc') // true
isUnique('aab') // false
isUnique('') // true
isUnique('Aa') // true


 
