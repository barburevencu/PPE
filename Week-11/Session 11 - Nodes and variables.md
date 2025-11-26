# JsPsych: timeline nodes and plugins

## Summary of previous session

## Objectives

Objectives:
- Learn how to easily adapt how a trial goes (adding a blank after a trial...)
- Get familiar with reading the (jspsych) documentation
- Learn to use timeline variables
- (bonus) learn how to provide feedback


## Reading documentation
### Refreshing our previous script

Last time, we created a simple letter recognition task (file [here](./scripts/rich-timeline-tree.html)), with a fixation cross before each trial. You should also have added a blank after each trial.

Now, we will try to do this using two trial parameters. Look up the `html-keyboard-response` plugin [documentation](https://www.jspsych.org/latest/plugins/html-keyboard-response/#parameters) to find the relevant parameters.

At first sight, nothing fits what we want. But we can have a look at [the parameters available to all plugins](https://www.jspsych.org/latest/overview/plugins/#parameters-available-in-all-plugins).

Here, you should spot `post_trial_gap`, which seems to do what we want. We can use it to replace the blank screen trial. There seems to be nothing we can do about fixation cross, however: it must remain a standalone trial.

![Documentation Sample](./images/post_trial_gap_documentation.png)
The details of the parameter we are interested in.

### How much should we use the documentation?

You may have noticed several interesting options while browsing the documentation. You are free to use them to improve your script, as they allow you to easily fine-tune your trials.

Sometimes, it is not obvious to find the behavior that you want to implement. In these cases, do not hesitate to use whatever solution/tricks you may find! The pre-coded functions are here to help you code faster (and with less risks of bugs), but a running code is always better than none! Of course, you should always have a quick look on the internet before giving up... :)

### Exercise (~15 minutes)

Ok, let's update our letter detection task. Now, the letter should be presented in either upper and lower case throughout the trials. Your job will be to only display the letter for a single second, and save the expected key as well as the actual response.

A possible solution [here](./scripts/letter_detection_with_params.html).

### Exercise++

Could you add a confidence slider after each answer, with the help of the documentation?

## Simplifying our timeline: variables

Our code is growing, yet our experiment stays, in fact, pretty simple. We can make everything much simpler using timeline variables. Timeline variables are well-explained in the [official jsPsych documentation](https://www.jspsych.org/latest/tutorials/rt-task/#part-6-timeline-variables).

Note that the `timeline` is played entirely for each timeline_variable! In the code below, you will have two trials.

```javascript
let timelineWithParameters = {
  timeline: [trial],
  timeline_variable: [{variable_name: value1}, {variable_name: value2}]
}
```

To access the variable in your trial, you will have to call `jsPsych.timelineVariable("variable_name")`, with `variable_name` being the name of your variable.

```javascript
let trial = {
  type: ...,
  stimulus: jsPsych.timelineVariable("stimulus"),
}
```

You can also specify whether the order has to be randomized, and how many time you should repeat each trial.

```javascript
let timelineWithParameters = {
  timeline: [trial],
  timeline_variable: [{variable: value1}, {variable: value2}]
  // Randomization and repetition
  randomize_order: true,
  repetitions: numberOfRepetitions;
}
```

### Exercise (~15 min)

#### Part 1

Can you now simplify our last task? A possible solution [here](./scripts/letter_detection_with_timeline_variables.html).

#### Part 2

If you run my solution (and perhaps yours), you may notice that identical trials can be presented twice in a row. Whether or not allowing this is good practice is still debated. Still, jsPsych provides you with a method to do that. Try to look up how to do it (hint: look into the `jsPsych.randomization` module). 

<!-- ## Providing feedback

### Modify the current trial

Suppose we want to provide feedback to the participant when they answer. We could do this by coloring the letter at the end of a trial: in green for a correct answer, in red for an incorrect answer.

One way to do it could be to display another trial after the actual one, with the stimulus as we like. But this isn't very elegant.

One other way is to update the trial

### Adding a feedback -->
