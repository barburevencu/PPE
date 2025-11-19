# Creating online experiments with JsPsych: the basics

[JsPsych](https://www.jspsych.org/) is a JavaScript-based library to create online experiments

## Why?

Similarly to Expyriment, JsPsych is specifically tailored for psychology experiments, providing you with a wide range of tools to save you some development time.

Also, JavaScript is a programming language commonly used by all browsers, which means that you don't have to worry about making your script run on different platforms. All that matters is the web browser*! Additionally, this means that your scripts are already prepared for online experiment: you simply have to open the file as a link in your web browser, as will participants.

> *Small caveat here: although the core of the language is common across browsers, some specific parts may not be compatible with all. Usually though, we don't have to worry about it.

![URL example](./images/URLexample.png "A url example")
The current page you are viewing is nothing but a file opened by your browser using the above path.

## How ?

Objectives :
- Get an idea of how a web experiment works
- Distinguish HTML and JavaScript
- Get familiar with the skeleton of jsPsych and the notion of timeline.
- We'll also introduce basic functionalities of JavaScript and HTML. Ultimately, you will have to know them or be able to find them online (which is an entirely valid strategy!). But this isn't exactly our main focus.

### Opening the experiment file as a web page

You can find a basic demo script [here](./scripts/jspsych-skeleton.html). Once downloaded, open it with a *web browser* (right click or equivalent on most system, and then "*open with...*"). You should see a word written at the center of the screen.

Now press any key. This should save your a file on your computer. This is your data file, but we won't be bothered with it right now.

Basically, what you did is how an online experiment is run : through their web browser, participants open a file on the big computer of the internet. And basically, any web page is a text file interpreted by your browser. And instead of using a *path* specifying where the file is on your computer, you use a URL (e.g. https.example.com/) to know where the file is on the internet.

This file was adapted from [jsPsych tutorials](https://www.jspsych.org/latest/tutorials/hello-world/)

### Opening the experiment file as a text script

You can now open the file with your preferred text editor. If you activated the display of file extensions (you should!), you should see that this is a *.HTML* file.

## Basic skeleton: the list-of-trials timeline.

We will dissect it in details together during the lecture.Tthe main take-away here is that you control your experiment via a timeline, which is a list of 'trials' ran in order.

### Exercise 1 (10 mn):

#### Instructions

Try to code a toy experiment in which participants have to press the key written on the screen. Give instructions and provide 6 trials with F & J keys.

#### Correction

We'll see for a correction in class.

You can find [here](./scripts/basic-keypress-experiment.html) a more elaborate version of the script. I use some features from JavaScript, which quickly come in handy, but you should be able to achieve the same result with what we saw before!

#### JavaScript basics:
- You can use several `<script>` tags at once, e.g., to dissociate helpers.
```html
<script>
// Run a first script
</script>
<script>
// Run a second script
</script>
```

- You can use functions : unlike in Python, you have to write their body between accolades `{}`, but don't need columns `:`.
```javascript
// This function returns the double of the number given in argument
function double(x){
  return 2 * x;
}
double(3);
```

- You can define `for` loops, either with a three-step instruction (`let x = start; x < stop ; x += 1`) or from a list (`let x of list`).
```javascript
// This will run the encapsulated time 5 times, with `i` as the index
for (let i = 0; i <= 5; i+=1){
  // Do stuff
}

// This will do something for each item x of list l.
for (let x of l){
  // Do stuff
}
```

- You can dynamically add items to lists (`push`, similar to Python's `append`).
```javascript
// Here, you add a 1 at the end of list l
l.push(1)
```

- You can create formattable strings with the oblique quote character `` ` ``: anything encapsulated within `${}` will be interpreted as javascript code.
```javascript
let language = "javascript";
`This file will be interpreted as ${language} code`.
```

You may also have noticed to important novelties: one in the specification of the trial's stimulus (`<p>`, ll. 39-44) and one when creating the trials (`jsPsych.randomization.repeat`, l. 25). We'll discuss these right below.

#### The `<p>` paragraph tag.

You can see that several groups of sentences are enclosed within a `<p></p>` tag. In HTML, tags define parts of the document, here a paragraph (hence the `<p>`). This are very useful to structure your document, and it helps jsPsych present it nicely (by physically separating paragraphs).

```html
<p>This is a first HTML paragraph!</p>
<p>And this is another one!</p>
```

##### `jsPsych.randomization.repeat`

 You can use `jsPsych.randomization.repeat` to create identical repetitions of an item in a list, which is very helpful to have several identical trials. You also get random shuffling at the time (try to think of how you can adapt this).

 ```javascript
 let l = [1, 2, 3, 4];
 let shuffledRepeated = jsPsych.randomization.repeat(l, 2);
 // Example of output: [1, 3, 2, 3, 4, 1, 4, 2]
 ```

**There are two important takeaways from this alternative correction.** First, jsPsych offers you a lot of tools that can save you some lines/time. Second, being able to write proper HTML code will help you tremendously in designing efficient stimuli.

## Organising events: nested timelines

### Exercice 2 (20 mins)

#### Instructions

You may have noticed that in our previous code, when two successive trials indicated the same letter, one could hardly see the difference. You will try to fix this by introducing blanks between two trials. Take your old code, and try to improve it as much as you can, without looking at the correction!

You will need the `trial_duration` parameter when defining a jsPsychHtmlKeyboardResponse. This parameter (used like `stimulus`) defines the maximum duration of a trial.

#### Correction

You can find a first solution [here](./scripts/rich-timeline-list.html). In this solution we simply add a blank screen trial after each stimulus presentation in the final timeline.

But this is not very convenient nor very elegant: we have to add the new trials after having randomized trial order, and we can not do it anymore. JsPsych provides you with a solution in the form of nested timelines:

```javascript
let nestedTrial = {
  timeline: [trial1, trial2]
};
```

This structure means that whenever you run the `nestedTrial` trial, you first run `trial1` and right after you run `trial2`. Try to implement this in an alternative solution to our problem. Solution [here](./scripts/rich-timeline-tree.html).

### Stroop task: defining HTML color

Your assignement for next week will be to code a small stroop task. You have to add a fixation cross before each trial, and (very short) blank after each. To change the color of a paragraph in HTML, you just have to specify it within the `<p>` paragraph tag:

```html
<p style='color: red'>This text is colored in red.</p>
```
