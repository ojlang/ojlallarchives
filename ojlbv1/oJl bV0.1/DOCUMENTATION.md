The Open John Language
EN-US
(V0.1)


 Hello dear reader, I thank you in advance for reading this documentation! If you are here, it means you have decided to test JL, or simply get to know my project. This is a great reason for me to be happy. Thank you!

Written By: João Victor (John)

! This is a comment
I.0-Introduction:
I.1- What is oJl?

oJl (Open John Language) is a programming language developed with the purpose of being clear, simple, and accessible. Its syntax was designed to be close to a natural language, facilitating the reading and comprehension of the code, which makes it suitable for both beginners and experienced developers looking for productivity.
! As its name suggests, oJl is an open-source project; feel free to modify and study in depth how the project works.
	The main goal of oJl is to be intuitive and functional, without sacrificing efficiency. It is an experimental project in constant evolution, with the aim of offering a viable and friendly alternative in the programming language ecosystem.
	oJl is provided as open-source software, allowing the community to freely contribute with improvements, feature additions, and specific adaptations to their needs. The only requirement is the maintenance of credits to the original creator.
	In essence, oJl is not just a language, but a tool that seeks to be a partner to the programmer, simplifying the development process without compromising utility and robustness.

I.2- Why did I create oJl?

	Programming languages are fundamental tools that allow us to communicate with machines since the 20th century. Today there are countless options, each with its own proposal, but most of them present a complex syntax that can be challenging for both beginners and already experienced developers. Although this learning process is part of the journey, I believe it is possible to follow a different path.
	oJl was born from this purpose: to be welcoming, simple, and functional, allowing complex projects to be developed clearly and accessibly.
	I cannot fail to acknowledge that the creation of oJl also arose from a personal motivation: the desire to build something that had its own identity and could be recognized. I always admired the existing languages and their visual marks, and this inspiration, combined with my passion for design and logotypes, led me to idealize oJl. Even if it comes to be remembered as a “different” or even “strange” language, for me, the most important thing is that it carries personality and meaning.
	oJl is, therefore, both a technical and creative project that seeks to unite simplicity, identity, and innovation in a single language.


I.3- Language Goals

	As previously mentioned, JL was developed with the goal of being easy to learn and use. But the question arises: in which projects can the language be applied?
	oJl was designed to have a general focus, capable of being used in different types of projects, from the simplest to more complex applications. Although it is still in its initial phase and presents certain limitations, its proposal to be an open and flexible language allows anyone to adapt, expand, and create new versions according to their own needs and objectives.
	In summary, oJl seeks to be a versatile language that can evolve alongside its community, becoming increasingly useful and suitable for different development scenarios.


P.0 - First Steps:
P.1 - How to Install?
Installing JL is quick and simple. Just download the interpreter available on the project's official website.
	JL was developed in Python, so you need to have Python installed on your machine.
	After that, follow the steps:
> Download the interpreter
 Download the ojlreader.py file.

> Create your JL file
 Create a file with the .ojl extension (for example: my_code.ojl).

	> Execute your program
 To run the file, just open the interpreter with Python, passing the file as an argument:

 python3 ojlreader.py my_code.ojl

Done! Now you can write and execute your first programs in oJl.
! I also cannot ignore the fact that running programs written in oJl is a tedious process; I will start working on an IDE to make it easier to work with.

P.2 - System Requirements
JL was developed to be lightweight and accessible, capable of running on virtually any device that supports program installation.
Minimum Requirements
	> Any operating system capable of running Python 3.8 or higher

> Text editor for creating .ojl files

> Terminal or command prompt for running the programs

Notes
> JL does not require advanced hardware and can run on simple computers or virtual environments.

> As an experimental and open-source language, its compatibility can be expanded as the community contributes to the project.
P.3 - Your First Program
Now that JL is installed, we can create the first program. Traditionally, every programming language starts with the classic “Hello, World!”, and here will be no different.
1. Create a JL file
Open a text editor of your choice and save the file with the .ojl extension.
 Example: hello.ojl.
2. Write the code
Inside the file, insert the following line:
say "Hello, World!";

The command say ; is responsible for displaying messages, performing a role similar to print in other programming languages.
3. Execute the program
In the terminal, use the interpreter to run the created file:
python3 lexer.py hello.ojl

4. Expected Result
If everything was configured correctly, the program will display the following output:
Hello, World!

M.0 - The Manual
M.1 - Syntax
	The syntax of oJl aims to be simple and understandable, resembling a conversation. The syntax of oJl has evolved over time, being more and more polished to be more "clean," simpler, something that is not too daunting—oJl seeks to be practical.

! Out of curiosity, I will show the evolution of the language's syntax. The project initially started with a somewhat strange syntax; the idea was for it to be like a "text-based Scratch." oJl worked with blocks. Here is a simple "Hello World":
when_tcs{       < The "when" block with the "tcs" extension means "the code start," which is somewhat self-explanatory ("when the code starts..."). I strongly believe this is a good idea, but the fewer things, the better, right?
 	say = “Hello World”       < Say "Hello World"
}       < Block closure

I decided to change it because it looks like a somewhat "polluted" language. Of course, oJl has had many modifications and identities, but it was modified for ease and simplicity.
	oJl has a simple manual to explain its functionalities and capabilities so far. Here is "the oJl bible," your manual that will explain how to develop your code. The manual is in the next topic.
M.2 - The oJl Bible

M.2.1. Comments

Comments are used to add notes to the code that the interpreter ignores. In OJL, any text after an exclamation point `!` is considered a comment.

! This is a full-line comment.
var name = "John"; ! This is an end-of-line comment.



M.2.2. Variables

Variables are used to store data. OJL supports numbers and text (strings).

> Declaration
Use the keyword `var`.

! Declaring a text variable
var message = "Hello, world!";

! Declaring a numeric variable
var age = 25;

> Usage
To use the value of a variable, place a dollar sign `$` before its name.

say $message;

M.2.3. The `say` Command (Output)

The `say` command is used to print values to the screen. It can print literal text or the value of variables.

say "This is a literal text.";
say $age;





M.2.4. The `calc` Command (Calculations)

The `calc` command performs a mathematical operation and stores the result in a variable. The syntax is `calc [expression] -> [destination_variable];`.

- Supports the 4 basic operations: `+`, `-`, `*`, `/`.
- Supports only one operation at a time.
- Variable names in the expression do not need the `$`.

var x = 10;
var y = 5;
var result = 0;

calc x + y -> result; ! result now holds 15
say $result;

M.2.5. Control Structures (The `if` Command)

The `if` command executes a block of code only if a condition is true.

IMPORTANT: The entire `if` command, including its condition and body, must be on a single line.

- The condition uses a single equal sign `=` for comparison.
- The body of the `if` is defined within parentheses `()`.

var score = 10;
if $score = 10 (say "Congratulations, maximum score!";);

M.2.6. Functions

Functions allow code to be grouped for reuse.

IMPORTANT: The entire function definition must be on a single line.

> Definition
The syntax is `f function_name (function_body);`.

f greeting (say "Hello!";say "Welcome to OJL!";);

> Call
To execute a function, the syntax is `f function_name;`.

f greeting;


M.3 - Need help?
	
	Found an error? Want to suggest something?
https://docs.google.com/forms/d/e/1FAIpQLSeLlWwxam5vtrnn6Onjt6RYGyQ-1BeLNBIVEg8ArTUKQCI94g/viewform?usp=header
Tell us here.

F.0 - Final Considerations

	
We have reached the end of this documentation. If anything was poorly explained, if any explanation was missing, or if you still have questions, do not hesitate to ask!
	I am happy to know that you have made it this far. I hope that this documentation, simple as it is, can be useful to you. I hope oJl is a good project for people. I am available to hear your ideas so that this can become an incredible project for everyone. Follow us on GitHub for more information.

Thank you! ;D

oJl is an open-source project created by João Victor.
Documentation Version: oJl Bible V0.1 PT-BR
Current oJl Version: betaV0.1
GitHub Page: https://github.com/ojlang
My Page: https://github.com/PernilongoKiller
 
---------------------------------------------------------------------------------------------------------------------------------
Note: This documentation was translated using Artificial Intelligence.


