# Workflow of a Machine Learning project机器学习项目的工作流程

> 来源：Week1-What is AI 1.Introduction简介
> 章节：P11

---

## P11 2.Workflow of a Machine Learning project机器学习项目的工作流程

### AI润色版
Machine learning algorithms can learn input to output or A to B mappings.

So how do you build a machine learning project?

In this video, you learn what is the workflow of machine learning projects.

Let's take a look.

As a running example, I'm going to use speech recognition.

So some of you may have an Amazon Echo or a Google Home or Apple Siri device or a Baidu Dura OS device in your homes.

Some years back, I've done some work on Google's speech recognition system.

And it also led Baidu's Dura OS project.

And today I actually have a Amazon Echo in my kitchen.

So every time I'm boiling an egg, I will say Alexa set timer for three minutes.

And then it lets me know when the three minutes are up and my eggs are ready.

So how do you build a speech recognition system that can recognize when you say Alexa or Hey Google or Hey Siri or Hello Baidu?

Let's go through the key steps of the machine learning project.

And just for simplicity, I'm going to use Amazon Echo or detecting the Alexa keyword as this running example.

If you want to build an AI system or build a machine learning system to figure out when a user has said the word Alexa, the first step is to collect data.

So that means you go around and get some people to say the word Alexa for you, and you record the audio of that.

And you'll also get a bunch of people to say other words like Hello or say lots of other words and record the audio of that as well.

Having collected a lot of audio data, a lot of these audio clips of people saying either Alexa or saying other things.

Step two is to then train the model.

And this means you will use a machine learning algorithm to learn an input to output or A to B mapping where the input A would be an audio clip.

And in the case of the first audio clip above, hopefully it will tell you that the user said Alexa.

And in the case of audio clip two shown on the right, hopefully the system will learn to recognize that the user has said Hello.

Whenever an AI team starts to train the model, meaning to learn the A to B or input output mapping, what happens pretty much every time is the first attempt doesn't work well.

And so invariably, the team will need to try many times or in AI we call this iterate many times.

You have to iterate many times until hopefully the model looks like it's good enough.

The third step is to then actually deploy the model.

And what that means is you put this AI software into an actual smart speaker and ship it to either a small group of test users or to a large group of users.

What happens in a lot of AI products is that when you ship it, you see that it starts getting new data and it may not work as well as you had initially hoped.

So for example, I am from the UK, so I'm going to pick on the British, but let's say you had trained your speech recognition system on American accented speakers and you then ship this smart speaker to the UK and you start having British accented people say Alexa.

Then you may find that it doesn't recognize this speech as well as you had hoped.

And when that happens, hopefully you can get data back of cases such as maybe British accented speakers was not working as well as you're hoping and it uses data to maintain and to update the model.

So to summarize, the key steps of a machine learning project are to collect data, to train the model, the A to B mapping, and then to deploy the model.

And throughout these steps, there is often a lot of iteration, meaning fine-tuning or adapting the model to work better or getting data back even after you've shipped it to hopefully make the product better, which may or may not be possible depending on whether you're able to get data back.

Let's look at these three steps and see how they apply on the different projects on building a key component of a self-driving car.

So remember the key steps of collect data, train model, and deploy model since we'll revisit these three steps on the next slide.

Let's say you're building a self-driving car.

One of the key components of a self-driving car is a machine learning algorithm that takes as input, say a picture of what's in front of your car and tells you where are the other cars.

So what's the first step of building this machine learning system?

Hopefully you remember from the last slide that the first step was to collect data.

So if you go instead of a machine learning algorithm that can take as input and image and output the position of other cars, the data you would need to collect would be both images as well as position of other cars that you want the AI system to output.

So let's say you start off with a few pictures like this.

These are the inputs A to the machine learning algorithm.

You need to also tell it what is the output B you would want.

And so for each of these pictures, you would draw a rectangle around the cars in the picture that you wanted to detect.

And on this slide, I'm hand drawing these rectangles, but in practice, you would use some software that lets you draw perfect rectangles rather than these hand drawn ones.

And then having created this data set, what was the second step?

Hope you remember that the second step was to train the model.

Now, invariably, when your AI engineers start training a model, they'll find initially that it doesn't work that well.

For example, given this picture, maybe the software, the first few tries, things that that is a car.

And it's only by iterating many times that you hopefully get a better result by figuring out that that is where the car actually is.

Finally, what was the third step?

It was to deploy the model.

Of course, in the self-driving world, it's important to treat safety as number one and deploy model or to test the model only in ways that can preserve safety.

But when you put the software in cars on the road, you may find that there are new types of vehicles, say golf cars, that the software isn't detecting very well.

And so you would get data back, say pictures of these golf cars, use the new data to maintain and update the model so that hopefully you can have your AI software continually get better and better to the point where you end up with a software that can do a pretty good job detecting other cars from pictures like these.

In this video, you learn what are the key steps of a machine learning project, which are to collect data, to train the model, and then to deploy the model.

Next, let's take a look at what are the key steps or what is the workflow of a data science project.

Let's go on to the next video.

---
