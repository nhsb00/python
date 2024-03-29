// Write an `Array.prototype.dups` method that will return an object containing 
// the indices of all duplicate elements. The keys are the duplicate elements; 
// the values are arrays of their indices in ascending order
//
// Example: 
// [1, 3, 4, 3, 0, 3, 0].dups => { 3: [1, 3, 5], 0: [4, 6] }

Array.prototype.dups = function () {
    const count = {};
    const dups = {};

    this.forEach((el, idx) => {
        count[el] = count[el] || [];
        count[el].push(idx);
    });

    const keys = Object.keys(count).filter(el => count[el].length > 1);
    keys.forEach((key) => {
        dups[key] = count[key];
    });

    return dups;
};
