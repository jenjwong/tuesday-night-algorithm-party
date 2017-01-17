// KEY CONCEPTS
// strings are immutable
// strings cannot use array methods

// URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
// EXAMPLE
// Input: "Mr John Smith " J 13 Output: "Mr%20J ohn%20Smith"

// linnear time and linear space

// trim string
  // create variable to hold URLify-ed
  // loop over string
    // if space add %20
    // if character add character to URLify-ed

// return string


const bestURL = 'www.jen wong is cool.com     ';  // www.jen%20wong%20is%20cool.com

const URLify = (string) => {
  const trimmedString = string.trim();
  let URLifyString = '';
  for (let i = 0; i < trimmedString.length; i++) {
    if (trimmedString[i] === ' ') {
      URLifyString += '%20'
    } else {
      URLifyString += trimmedString[i];
    }
  }
  return URLifyString;
};

console.log(URLify(bestURL))
