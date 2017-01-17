// Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
const isPermutation = (string1, string2) => {
  const obj1 = {};
  for (let i = 0; i < string1.length; i++) {
    obj1[string1[i]] = obj1[string1[i]] + 1 || 1;
  }

  const obj2 = {};
  for (let i = 0; i < string2.length; i++) {
    obj2[string2[i]] = obj2[string2[i]] + 1 || 1;
  }

  for (let i = 0; i < string1.length; i++) {
    if (obj1[string1[i]] !== obj2[string1[i]]) {
      return false;
    }
  }

  return string1.length === string2.length;
};

// linear time and linear space
// assumes whitepaces and case sensitivity are significant

console.log(isPermutation('abc', 'bca')) // true
console.log(isPermutation('aaa', 'ccc')) // false
console.log(isPermutation('a', 'aa')) // false
console.log(isPermutation('', '')) // true
