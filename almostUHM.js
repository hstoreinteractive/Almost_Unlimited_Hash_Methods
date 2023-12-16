import { createHash } from 'crypto';

function generateHashFunction(method) {
    return (string) => {
        let hash = createHash(method).update(string, 'utf-8');
        return hash.digest('hex');
    };
}

const hash_methods = [
    generateHashFunction("sha224"),
    generateHashFunction("sha256"),
    generateHashFunction("sha384"),
    generateHashFunction("sha512"),
];

function randomize(n) {
    const hashed_value = hash_methods[3](n.toString());
    var hashed_value_split = hashed_value.match(/.{1,10}/g).map(e => parseInt(e,16));
    return hashed_value_split.reduce((a, b) => a+b) % 2147483647;
}

function generatePrecidualHashFunction(seed) {
    seed = randomize(seed);
    function prodedualHashFunction(string) {
        const combined_string = string + seed.toString();
        const method = hash_methods[seed % (hash_methods.length - 1)];
        const hashed = method(combined_string);
        return hashed;
    }
    return prodedualHashFunction;
}

var seed = 1234
var string = "Hello World!"
var hash_method = generatePrecidualHashFunction(seed)
var hash = hash_method(string)
console.log(hash)