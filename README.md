## Building a simple Python App with Python IDLE & Visual Studio Code
This is a synposis of the talk given on 8/30, at the UMKC ACM meeting. Before we begin, a word from the speaker:

Before we begin, I'd like to thank everybody for attending. There were teething issues and I thank you for your patience. Still, the quality was far below my expectations and I apologize. If you found the content interesting, but the presentation otherwise, I am creating this synposis to provide a more compact resource that you may refer to. 

Looking forward, you can expect a synposis of talks and slide-decks & demo code made avalible in at least a week of advance. This info will give you a preview of the event, and better inform your decision to attend. If you are interested in attending future events, I encourage you to take a look.

Thank you for your time,

Noah

## Eightball

![Demo](https://github.com/noah-dev/acm_talk1/blob/master/idle_eightball_demo)

A Magic 8-ball is a toy used for fortune-telling; ask a question and then shake it. The Magic 8-ball will dispaly a response. For this simple Python app, we'll use that as the basis for learning Python IDLE and using it to build the app. We will also cover Visual Studio Code, an advanced editor with many useful features. 

If you'd like to see the demo code first, [take a look here](https://github.com/noah-dev/acm_talk1/blob/master/eightball.py).

For reference, please take a look at the [slides](https://github.com/noah-dev/acm_talk1/blob/master/talk_1.pptx).
Per the slides, there are many different tools you can use to build Python apps with. Even if you do not like these tools, you may gain exposure to new features, better informing you when search for other tools. 

## Python Integrated Development Learning Environment (IDLE)

There a many different ways to develop and run Python code. On windows, you could use the Notepad editor and run your code from terminal. But there are better, easier, and faster ways. In software development, IDE (Integrated Development Environment) are common place; among their features, they are able easily run code at the touch of a button. 

With Python, the Windows Installation includes the IDLE. Once installed, search for "Python" in the search bar. Select the item with "IDLE" (You can set a shortcut from the taskbar for easier access). Once open, you can immediatly enter and test code to see behavior. 

(If you wish to use Python from terminal, ensure the Add to Path checkbox is ticked during installation)

![IDLE](https://github.com/noah-dev/acm_talk1/blob/master/images/idle_if_elif.gif)

As shown above, variables can be assigned and we can create conditional block (if/elif) to create different behavior depending on the number variable. If we change the number variable, and re-run the conditional block (click on ran-code and press the Enter key) the behavior changes. 

For our eightball project, this will be one part of the code. But how do we assign a value to the number variable? We could ask the user to input a value, but the Magic 8-ball is a fortune-telling device. We can assign a hard value, but that would mean only a single response is given. 

What we need is a way to random generate numbers. To do that, we will import the random module and use the randint function. 

![Random (Psuedo-Random) Integar](https://github.com/noah-dev/acm_talk1/blob/master/images/idle_randint.gif)

As shown above, each time the randint function runs, it provides a different number. The two parameters, in the parnathesies, determine the range of numbers it will return. It is able to randomly pick one of these numbers: 1,2,3,4,5, or 6. 

**A word of caution:** Generating "true" random numbers is a very complicated topic. With the random module, and other random number generators, it generates psuedo-random numbers. These are numbers that appear to be random, but can be predicted. For an application like this, psuedo-random is good enough. For the sake of readability, I will use the word "random" in place of psudeo-random. 

Using the random number, we will provide an answer based on that. We will also use the input() function to prompt the user to type in a question. Just like the Magic 8-ball, we won't actually use the response when determining the answer. 

![Coding Demo](https://github.com/noah-dev/acm_talk1/blob/master/images/idle_eightball.gif)

We are also saving the code to a file, so that we do not lose it when we close the program or restart the computer. As demonstrate, the eightball app is able can provide different responses. Of course this is psuedorandom, so a response can appear twice in a row. 

With that, the simple Python app is complete. For the full code, [take a look here](https://github.com/noah-dev/acm_talk1/blob/master/eightball.py).

## Visual Studio Code

Python IDLE is nice for many things, and I have built entire projects with it. But at some point, with enough many files & folders, it would be nice to use a single window to manage the entire project. This is where programs like Visual Studio Code come to play. Visual Studio Code, unlike an IDE/IDLE, is an editor, whose primary prupose is to make file editing (like py files) better, easier, and quicker. Running Python code from Visual Studio Code (**VSC**) takes a few more steps, but can be done easily enough. 

Note: VSC is not the same as Visual Studio. Though they are both developed by Microsoft, VSC is an editor that can be extended with features, while Visual Studio is an IDE out of the box. Both of Pros & Cons

Once installed, you can use VSC to open a folder and view the different files & sub-folders within. To the left is a menu, that can show four different views. By default, the file view is open. Using the file view, we can add a new file, edit it, and do other operations like renaming. Similair operations can be done for folders. 

![VSC File Managment](https://github.com/noah-dev/acm_talk1/blob/master/images/vsc_file_managment.gif)

Out of the box, VSC has syntax highlighting, which color-codes different kinds of code; functions are painted in blue, statments in purple, and so on. But what if we want a different color pallete? No problem, We can add new new themes by installing extensions. Click on the 4th menu item to bring up the extensions view and search for "Dracula"

![VSC Theme Install](https://github.com/noah-dev/acm_talk1/blob/master/images/vsc_theme_install_apply)

As you can see, after installing & applying theme, we now have this purple on purple color scheme. If you want to see other avalible themes, searhc for "themes" instead of dracula. 

If you have a python file in the project folder, VSC may have given you a helpful pop-up, imploring you to install the Python extension. Search for "Python" from the extensions view. (Not gif below)

![VSC Python Ext.](https://github.com/noah-dev/acm_talk1/blob/master/images/vsc_python_extension)

Once installed, VSC gains a lot more features that can aid in Python development. For example, it comes with a linter. A linter will, after saving a python file, inspect the code and highlight any syntax errors it detects. (Sorta like how Microsoft Word has spell checker. )

![VSC Python Linter](https://github.com/noah-dev/acm_talk1/blob/master/images/vsc_python_linter)

I created a typo, and then saved the file. The linter, pylint, inspected the code and realized that "chooice" had never been defined before. It highlighted the code with red, and gave a message upon mouse over. 

Finally, if you want to run the code from VSC, there are several options; extensions, debugging, or terminal. I will be covering the terminal appraoch, but feel free to use any method you wish. During the installation of Python, it is important that it was added to path. Otherwise running from terminal will not work. (It can be added post-installation by going into windows environment variables)

Go to view, and bring up the integrated terminal. 

![VSC Terminal](https://github.com/noah-dev/acm_talk1/blob/master/images/vsc_terminal)

A menu pops up at the bottom, and automatically opens in the project path. Using the python command, we can run the eightball program. It prompts for user input, and we can get an answer. 

Note: What is being shown is PowerShell, not the CMD listed on the presentation/cheatsheet. Some command work in both. If you wish to use CMD, simply type "CMD" into the PowerShell terminal, and it will swtich over. CMD use to be the default Windows 10 terminal, until a recent update. 

## Conclusion

Thanks for sticking it out! I hope the images provide a clear picture of the concepts we have discussed. If you have any questions, feel free to reach out to me. (We'll hopefull have social media & a forum soon). 

As shown in the slides, there are many different alternatives to Python IDLE & VSC. For example: If you like VSC for it's file management & syntax highlighting, but wish Python code easier to run, take a look at PyCharm. 

We also discussed Git/GitHub, but we will save that topic for another day. 
