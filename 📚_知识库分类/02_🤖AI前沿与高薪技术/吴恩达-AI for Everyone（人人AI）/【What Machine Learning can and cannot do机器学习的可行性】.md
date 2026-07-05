# What Machine Learning can and cannot do机器学习的可行性

> 来源：Week1-What is AI 1.Introduction简介
> 章节：P6

---

## P6 6.What Machine Learning can and cannot do机器学习的可行性

### AI润色版
In this video and the next video, I hope to help you develop intuition about what AI can and cannot do.

In practice, before I commit to a specific AI project, I'll usually have either myself or engineers do technical diligence on a project to make sure that it is feasible.

This means looking at the data, looking at the input and output, A and B, and just thinking through if this is something AI can really do.

What I've seen, unfortunately, is that some CEOs can have an overinflated expectation of AI and can ask engineers to do things that today's AI just cannot do.

One of the challenges is that the media, as well as the academic literature, tends to only report on positive results or success stories using AI.

And we see a strain of success stories and no failure stories. People sometimes think AI can do everything.

And unfortunately, that's just not true.

So what I want to do in this and the next video is to show you a few examples of what today's AI technology can do, but also what it cannot do.

And I hope that this will help you hone your intuition about what might be more or less promising projects to select for your company.

Previously, you saw this list of AI applications, from spam protein, to speech recognition, to machine translation, and so on.

One imperfect rule of thumb you can use to decide what supervised learning may or may not be able to do is that pretty much anything you can do with a second of thought.

We can probably now or soon automate using supervised learning, using this input-to-output mapping.

So, for example, in order to determine the position of other costs, that's something that you can do with less than a second.

In order to tell if a phone is scratched, you can look at it and you can kind of tell in less than a second.

In order to understand, at least transcribe what was said, it doesn't take that many seconds of thought.

And while this is an imperfect rule of thumb, it maybe gives you a way to quickly think of some examples of tasks that AI systems can do.

Whereas in contrast, something that AI today cannot do would be to analyze a market and write a 50-page report.

A human cannot write a 50-page mark of analysis report in a second.

And it's very difficult, at least I don't know.

And I don't think any team in the world today knows how to get an AI system to do market research and run an extended market report either.

I found that one of the best ways to hone intuition is to look at concrete examples.

So let's take a look at a specific example relating to customer support automation.

Let's say you run a website that sells things, so an e-commerce company, and you have a customer support division that gets an email like this.

The tutorial arrived two days late, so I wasn't going to give it to my niece for her birthday.

Can I return it?

If what you want is an AI system that looks at this and decides this is a refund request, so let me route it to my refund department,

then I would say you have a good chance of building an AI system to do that.

The AI system would take as input the customer text with the customer email you,

and it would output, is this a refund request, or is this a shipping problem, or is it a other request,

in order to route this email to the most appropriate part of your customer support center.

So the input A is a text, and the output B is one of these three outcomes.

Is it a refund, or a shipping problem, or a shipping query, or is it a different request?

So this is something that AI today can do.

Here's something AI today cannot do, which is if you want the AI to input an email and automatically generate a response like,

oh, sorry to hear that.

I hope your niece had a good birthday.

Yes, we can help her and so on.

So for an AI to output a complicated piece of text like this today is very difficult by today's standards of AI.

And in fact, to even empathize about the birthday of your niece, that is very difficult to do for every single possible type of email you might receive.

Now, what would happen if you were to use a machine learning tool, like a deep learning algorithm, to try to do this anyway?

So let's say you try to get an AI system to input the user's email and output a two to three paragraph empathetic and appropriate response.

And let's say that you have a modest size data set, you're like a thousand examples of user emails and appropriate responses.

It turns out if you run an AI system on this type of data on a small data set, like a thousand examples, this may be the performance you get,

which is if a user emails my box is damaged, they'll say thank you for your email.

And it says whether I review, thank you for your email.

What's your time policy?

Thank you for your email.

But the problem with building this type of AI is that with just a thousand examples, there's just not enough data for an AI system to learn how to write to the three paragraph appropriate and empathetic responses.

So it may end up just generating the same very simple response like thank you for your email, no matter what the customer is sending you.

Another thing that could go wrong, another way for an AI system to fail is if it generates gibberish such as when am I box arriving?

And it says thank yes, now you're kind of gibberish.

And this is a hard enough problem that even with 10,000 or 100,000 email examples, I don't know if that would be enough data for an AI system to do this well.

The rules for what AI can and cannot do are not hard and fast.

And I usually end up having to ask engineering teams to sometimes spend a few weeks doing deep technical diligence to decide for myself if the project is feasible.

But to hone your intuitions to help you quickly filter feasible and not feasible projects, here are a couple other rules of thumb about what makes a machine learning problem easier or more likely to be feasible.

One, learning a simple concept is more likely to be feasible.

Well, what does a simple concept mean?

There's no formal definition of that.

But if it's something that takes you less than a second of mental thought or very, very small number of seconds of mental thought to come up with a conclusion, then that would lead to what it being a simple concept.

So you're looking outside the window of a self-driving car to spot the other cars.

That would be a relatively simple concept.

Whereas how to write an empathetic response to a complicated user complaints, that would be less of a simple concept.

Second, a machine learning problem is more likely to be feasible if you have lots of data available.

And here data means both the input A and the output B that you want the AI system to have in your A to B input output mapping.

So, for example, in the customer support application, the input A would be examples of emails from customers and B could be labeling each of these customer emails as to whether it is a refund request or a shipping query or some other problem, one of three outcomes.

And if you have thousands of emails with both A and B, then the odds of you being able to build a machine learning system to do that would be pretty good.

AI is the new electricity and is transforming every industry.

But it's also not magic and we can't do everything under the sun.

I hope that this video started to help you hone your intuitions about what it can and cannot do and increase the odds of your selecting feasible and valuable projects for maybe your teams to try working on.

In order to help you continue developing your intuition, I would like to show you more examples of what AI can and cannot do.

Let's go into the next video.

---
