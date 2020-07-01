# Cesar-s-Cipher
Solution to the second challenge of the Smartninja web development course. Python Flask (backend) + JS + Ajax + jQuery

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security.

My approach at first was flawed or not optimal should I say. I was reading about the time complexity concept in programming and I figured out that I nested 2 loops, which results in O(n²).

Now that's not too big of a problem in cases like this, where programs are not complex, but I still wanted to write code with best practices. I then decided to implement ord() and chr() functions, that are included in the default library of Python functions. If you want to know how these two work I have comments in the code, which are describing what they're doing.

I decided to do the front-end with JavaScript and handle requests with Ajax.

If you're interested to test the app, feel free to play around with it on heroku:

https://ccipher.herokuapp.com/
