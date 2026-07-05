# More examples of  Machine Learning can and cannot do机器学习的可行性事例

> 来源：Week1-What is AI 1.Introduction简介
> 章节：P7

---

## P7 7.More examples of  Machine Learning can and cannot do机器学习的可行性事例

### AI润色版
One of the challenges of becoming good at recognizing what AI can and cannot do is that it does take seeing a few examples of

Concrete successes and failures of AI and if you work on an average of say one new AI project per year

Then to see three examples would take you three years of work experience and that's just a long time

What I hope to do both in the previous video and in this video is to quickly show you a few examples of AI

Successive failures of what it can and cannot do so that in a much shorter time

You can see multiple concrete examples to help hone your intuition and select valuable projects

So let's take a look at a few more examples. Let's say you're building a self-driving car

Here's something that AI can do pretty well, which is to take a picture of what's in front of your car and

Maybe just using a camera

Maybe using other sensors as well such as radar or LiDAR and then to figure out

What is the position or where are the other cars?

So this would be an AI where the input A is a picture of what's in front of your car

Or maybe both a picture as well as radar and other sensor readings and the output B is

Where are the other cars and today the self-driving car industry has figured out how to collect enough data and has pretty good

Algorithms for doing this reasonably well. So that's what AI today can do

Here's the example of something that today's AI cannot do or at least would be very difficult using today's AI

Which is input a picture and outputs the intention or whatever the human is trying to gesture as your car

So here's a construction worker holding out a hand to ask your car to stop

Here's a hitchhiker trying to wave a car over

Here's a bicyclist raising the left hand to indicate that they want to turn left

And so if you were to try to build a system to learn an A to B mapping where the input A is a short video of a

Human gesturing at your car and the output B is what's the intention or what does this person want?

That today is very difficult to do

Part of the problem is that the number of ways people gesture at you is very very large

Imagine all the hand gestures someone could conceivably use ask you to slow down or go or stop

The number of ways that people could gesture at you is just very very large and

So it's difficult to collect enough data from enough

Thousands or tens of thousands of different people

Gesturing at you and all of these different ways to capture the richness of human gestures

So learning from a video to what this person wants is actually a somewhat complicated

Concept in fact even people have a hard time figuring out sometimes what someone waving at your car wants and then second

Because this is a safety critical application

You would want an AI that is extremely accurate in terms of figuring out

Does the construction worker want you to stop or does he or she want you to go and that makes it harder for an AI system as well

And so today if you collect just say ten thousand pictures of other cars

Many teams will be able to build an AI system that at least has a basic capability at detecting other cars in contrast

Even if you collect

Pictures or videos of ten thousand people it's quite hard to track down ten thousand people waving at your car

Even with that data set

I think it's quite hard today to build an AI system to recognize human intention from the gestures and the very high level of

Accuracy needed in order to drive safely around these people

So that's why today many self-driving car teams have some components for detecting other cars

And they do rely on that technology to drive safely

But very few self-driving car teams are trying to count on an AI system to recognize a huge

Diversity of human gestures and counting just on that to drive safely around people. Let's look at one more example

Say you want to build an AI system to look at X-ray images and diagnose pneumonia

So all of these are chest X-rays

So the input A could be the X-ray image and the output B

Can be the diagnosis. Does this patient have pneumonia or not?

So that's something that AI can do something that AI cannot do

Would be to diagnose pneumonia from ten images of a medical textbook chapter

Explaining pneumonia a human can look at a small set of images

Maybe just a few dozen images and read a few paragraphs from medical textbook and start to get a sense

But I actually don't know given a medical textbook

What is A and what is B or how to really pose as an AI problem to that

Know how to write a piece of software to solve if all you have is just ten images and a few paragraphs of text

But explain what pneumonia and a chest X-ray looks like whereas a young medical doctor might learn quite well reading a medical

Textbook and just looking at you know, maybe dozens of images in

Contrasts an AI system isn't really able to do that today

To summarize here are some of the strengths and weaknesses of machine learning

Machine learning tends to work well when you're trying to learn a simple concept

Such as something that you could do with less than a second of mental thought and

When there's lots of data available

Machine learning tends to work poorly when you're trying to learn a complex concept from small amounts of data a

Second underappreciated weakness of AI is that it tends to do poorly when it's also performed on new types of data

That's different than the data. It has seen in your data set. Let me explain with an example

Say you built a supervised learning system that uses A to B to learn to diagnose pneumonia

From images like these. These are you know, pretty high quality chest X-ray images

But now let's say you take this AI system and apply it at a different hospital or a different medical center

Where maybe the X-ray technician somehow strangely had the patients always lie at an angle or

Sometimes there are these defects not sure you can see the little scratches in the image these little other objects lying on top of the patients

If the AI system has learned from data like that on your left may be taken from a

High-quality medical center and you take this AI system and apply it to a different medical center

That generates images like those on the right then this performance will be quite poor as well

A good AI team would be able to

Ameliorate or to reduce some of these problems

But doing this is not that easy and this is one of the things that AI is actually much weaker than humans

If a human has learned from images on the left

They're much more likely to be able to adapt to images like those on the right as they figure out that the patients just lying at an angle

But an AI system can be much less robust than human doctors in

Generalizing or figuring out what to do with new types of data like this

I hope these examples are helping you hone your intuitions about what AI can and cannot do in case of boundary between what it can and cannot do

It still seems fuzzy to you. Don't worry. This completely normal completely. Okay. In fact, even today

I still can't look at the project and immediately tell if something is feasible or not and I often still need

Weeks of small numbers of weeks of technical diligence before forming strong conviction about whether something is feasible or not

But I hope that these examples can at least help you start imagining some things in your company that might be feasible and might be worth exploring more

The next two videos after this are optional and are a non-technical description of whether neural networks and what is deep learning

Please be free to watch those and then next week will go much more deeply into the process of what building an AI project

Would look like look forward to seeing you next week

---
