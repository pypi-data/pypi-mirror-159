# FlowhHash

Python3 hashing algorythm where the digest is executed as control flow instructions.

## Story

Hashing algorythms are defined by the following 2 properties:
* All of the digest is utilized in the hashing process
* Small changes to the input data will result in wildly different results

I noticed that one way to achive the second property is to let the digest determine the flow of the hashing process.
The first property however would require that all data had the ability to change the flow of the hashing process.
This is potentially self destructive, as letting all data change the flow of the hashing process could result in data being skipped over, and hence left out of the hash.

At which point I had the following idea:

What if the act of changing the flow of the hashing process could be used to interact with the data?

This library is an implimentation of that idea using a "mutating goto" that mutates and collects the data that it passes through, incorporating them into the hash.