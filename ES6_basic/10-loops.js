export default function appendToEachArrayValue(array, appendString) {
    array.forEach((item, index) => {
      array[index] = appendString + item;
    });
  
    return array;
  }
