# Almost Unlimited Hash Methods
__For all your Hashing requirements__

## What is this?
> This Project is a generator for Hash Methods
> 
> Just in case sha224, sha256, sha384, sha512... aren't enough
>
> This Project provides 2,147,483,647 diffrent Hash Methods based on an id instead of a name

## How do I Use it:
> > - ## Download the script for you're framework:
> > > ### Python
> > > ```bash
> > > wget https://raw.githubusercontent.com/hstoreinteractive/Almost_Unlimited_Hash_Methods/main/almostUHM.py -O almostUHM.py
> > > ```
> >
> > > ### JavaScript
> > > ```bash
> > > wget https://raw.githubusercontent.com/hstoreinteractive/Almost_Unlimited_Hash_Methods/main/almostUHM.js -O almostUHM.js
> > > ```
>
> > - ## Use in you're script:
> > > ### Python
> > > ```python
> > > from almostUHM import generatePrecidualHashFunction
> > >
> > > seed = 1234 # Define a seed to be used
> > > string = "Hello World!" # Define a sting to be encrypted
> > > hash_function = generatePrecidualHashFunction(seed) # Generate the Hash Function corresponding to the seed
> > > hashed_string = hash_function(string) # Generate the Hash of the String using the newly generated Hash Function
> > >
> > > print(hashed_string) # Results: d82958749b16f31578c38cccd6ccb00ccd21878de323da92be5fd46e88543d7f
> > > ```
> >
> > > ### JavaScript
> > > ```javascript
> > > const { generatePrecidualHashFunction } = require("./almostUHM.js")
> > >
> > > const seed = 1234 // Define a seed to be used
> > > const string = "Hello World!" // Define a sting to be encrypted
> > > const hash_function = generatePrecidualHashFunction(seed) // Generate the Hash Function corresponding to the seed
> > > const hashed_string = hash_function(string) // Generate the Hash of the String using the newly generated Hash Function
> > >
> > > console.log(hashed_string) // Results: d82958749b16f31578c38cccd6ccb00ccd21878de323da92be5fd46e88543d7f
> > > ```
> >
> > > ### JavaScript (Module)
> > > ```javascript
> > > import { generatePrecidualHashFunction } from "./almostUHM.js"
> > >
> > > const seed = 1234 // Define a seed to be used
> > > const string = "Hello World!" // Define a sting to be encrypted
> > > const hash_function = generatePrecidualHashFunction(seed) // Generate the Hash Function corresponding to the seed
> > > const hashed_string = hash_function(string) // Generate the Hash of the String using the newly generated Hash Function
> > >
> > > console.log(hashed_string) // Results: d82958749b16f31578c38cccd6ccb00ccd21878de323da92be5fd46e88543d7f
> > > ```
>
