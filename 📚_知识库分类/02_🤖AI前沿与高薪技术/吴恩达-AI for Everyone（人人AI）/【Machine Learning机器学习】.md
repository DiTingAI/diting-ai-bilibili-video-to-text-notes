# Machine Learning机器学习

> 来源：Week1-What is AI 1.Introduction简介
> 章节：P2

---

## P2 2.Machine Learning机器学习

### AI润色版
The rise of AI has been largely driven by one tool in AI called machine learning.

In this video, you learn what is machine learning so that by the end, you hopefully be able to start thinking how machine learning might be applied to your company or to your industry.

The most commonly used type of machine learning is the type of AI that learns A to B or input to output mappings.

And this is called supervised learning.

Let's see some examples.

If the input A is an email and the output B you want is this email spam 1 or 0, then this is the core piece of AI used to build a spam filter.

Or if the input A is an audio clip and the AI's job is to output the text transcript, then this is speech recognition.

More examples: if you want to input English and have it output a different language, Chinese, Spanish, something else, then this is machine translation.

Or the most lucrative form of supervised learning of this type may be online advertising.

Where all the large online ad platforms have a piece of AI that inputs some information about an ad and some information about you, and tries to figure out would you click on this ad or not.

And by showing you the ad so you're most likely to click on, this turns out to be very lucrative.

Maybe not the most inspiring application, but certainly having a huge economic impact today.

Or if you want to build a self-driving car, one of the key pieces of AI is an AI that takes input an image and some information from their radar or from othe
r sensors and outputs the position of other cars.

So your self-driving car can avoid the other cars.

Or in manufacturing, I've actually done a lot of work in manufacturing, where you take as input a picture of something you've just manufactured, such as a picture of a cell phone coming off an assembly line.

This is a picture of a phone, not a picture taken by a phone.

And you want to output: is there a scratch, is there a dent, or some other defect on this thing you've just manufactured?

And this is visual inspection, which is helping manufacturers reduce or prevent defects in the things that they're making.

This type of AI called supervised learning just learns input to output or A to B mappings.

And on one hand, input to output, A to B seems quite limiting.

But when you find the right application scenario, this can be incredibly valuable.

Now, the idea of supervised learning has been around for many decades, but it's really taken off in the last few years.

Why is this?

When my friends ask me, hey Andrew, why is supervised learning taking off now, there's a picture I draw for them, and I want to show you this picture now.

And you may be able to draw this picture for others that ask you the same question as well.

Let's say on the horizontal axis, you plot the amount of data you have for a task.

So for speech recognition, this might be the amount of audio data and transcripts you have.

In a lot of industries, the amount of data you have access to has really grow
n over the last couple of decades.

Thanks to the rise of the internet, the rise of computers.

A lot of what used to be, say, pieces of paper are now instead recorded on a digital computer.

So we've just been getting more and more and more data.

Now, let's say on the vertical axis, you plot the performance of an AI system.

It turns out that if you use a traditional AI system, then the performance would grow like this.

That as you feed it more data, this performance gets a bit better.

But beyond a certain point, it did not get that much better.

So as if your speech recognition system did not get that much more accurate or your online advertising system didn't get that much more accurate at showing the most relevant ads, even as you show the more data.

AI has really taken off recently due to the rise of neural networks and deep learning.

I'll define these terms more precisely in a later video.

So don't worry too much about what it means for now.

But with modern AI, with neural networks and deep learning, what we saw was that if you train a small neural network, then the performance kind of looks like this, whereas you feed it more data.

Performance keeps getting better for much longer.

And if you train a even slightly larger neural network, say a medium sized neural net, then the performance may look like that.

And if you train a very large neural network, then the performance just kind of keeps on getting better and better.

And for applications like speech rec
ognition, online advertising, building a self driving car, where having a high performance, highly accurate, say speech recognition system is important.

This has enabled these AI systems to get much better and make, say, speech recognition products much more acceptable to users, much more valuable to companies and to users.

Now here are a couple of implications of this figure.

If you want the best possible levels of performance, your performance to be up here, to hit this level of performance, then you kind of meet two things.

One is it really helps to have a lot of data.

So that's why sometimes you hear about big data, having more data almost always helps.

And the second thing is you want to be able to train a very large neural network.

And so the rise of fast computers, including Moore's Law, but also the rise of specialized processors, such as graphics processor units or GPUs, which you hear more about in the later video, has enabled many companies, not just the giant tech companies, but many, many other companies to be able to train large neural nets on a large enough amount of data in order to get very good performance and drive business value.

The most important idea in AI has been machine learning and specifically supervised learning, which means A to B or input-output mappings.

What enables it to work really well is data.

In the next video, let's take a look at what is data and what data you might already have and how to think about feeding this into AI systems
.

Let's go on to the next video.

---


---

### 📖 英文原版

## P2 2.Machine Learning机器学习

### AI润色版
The rise of AI has been largely driven by one tool in AI called machine learning.

In this video, you learn what is machine learning so that by the end, you hopefully be able to start thinking how machine learning might be applied to your company or to your industry.

The most commonly used type of machine learning is the type of AI that learns A to B or input to output mappings.

And this is called supervised learning.

Let's see some examples.

If the input A is an email and the output B you want is, is this email spam 1.0? Then this is the core piece of AI used to build a spam filter.

Or if the input A is an audio clip and the AI's job is output the text transcript, then this is speech recognition.

More examples, if you want to input English and have it output a different language, Chinese, Spanish, something else, then this is machine translation.

Or the most lucrative form of supervised learning of this type of machine learning may be online advertising.

Where all the large online ad platforms have a piece of AI that inputs some information about an ad and some information about you.

And tries to figure out would you click on this ad or not.

And by showing you the ad so you're most likely to click on, this turns out to be very lucrative.

Maybe not the most inspiring application, but certainly having a huge economic impact today.

Or if you want to build a self-driving car, one of the key pieces of AI is an AI that takes as input an image and some information from their radar or from other sensors and outputs the position of other cars.

So your self-driving car can avoid the other cars.

Or in manufacturing, I've actually done a lot of work in manufacturing where you take as input a picture of something you've just manufactured, such as a picture of a cell phone coming off an assembly line.

This is a picture of a phone, not a picture taken by a phone.

And you want to output, is there a scratch, is there a dent, or some other defect on this thing you've just manufactured?

And this is visual inspection, which is helping manufacturers reduce or prevent defects in the things that they're making.

This type of AI called supervised learning just learns input to output or A to B mappings.

And on one hand, input to output, A to B seems quite limiting.

But when you find the right application scenario, this can be incredibly valuable.

Now, the idea of supervised learning has been around for many decades, but it's really taken off in the last few years.

Why is this?

When my friends ask me, hey Andrew, why is supervised learning taking off now?

There's a picture I draw for them, and I want to show you this picture now.

And you may be able to draw this picture for others that ask you the same question as well.

Let's say on the horizontal axis, you plot the amount of data you have for a task.

So for speech recognition, this might be the amount of audio data and transcripts you have.

In a lot of industries, the amount of data you have access to has really grown over the last couple of decades.

Thanks to the rise of the internet, the rise of computers.

A lot of what used to be, say, pieces of paper are now instead recorded on a digital computer.

So we've just been getting more and more and more data.

Now, let's say on the vertical axis, you plot the performance of an AI system.

It turns out that if you use a traditional AI system, then the performance would grow like this.

That as you feed it more data, this performance gets a bit better.

But beyond a certain point, it did not get that much better.

So as if your speech recognition system did not get that much more accurate or your online advertising system didn't get that much more accurate at showing the most relevant ads, even as you show the more data.

AI has really taken off recently due to the rise of neural networks and deep learning.

I'll define these terms more precisely in a later video.

So don't worry too much about what it means for now.

But with modern AI, with neural networks and deep learning, what we saw was that if you train a small neural network, then the performance kind of looks like this, whereas you feed it more data.

Performance keeps getting better for much longer.

And if you train a even slightly larger neural network, say a medium sized neural net, then the performance may look like that.

And if you train a very large neural network, then the performance just kind of keeps on getting better and better.

And for applications like speech recognition, online advertising, building a self-driving car, where having a high performance, highly accurate, say speech recognition system is important.

This has enabled these AI systems to get much better and make, say, speech recognition products much more acceptable to users, much more valuable to companies and to users.

Now here are a couple of implications of this figure.

If you want the best possible levels of performance, your performance to be up here, to hit this level of performance, then you kind of meet two things.

One is it really helps to have a lot of data.

So that's why sometimes you hear about big data, having more data almost always helps.

And the second thing is you want to be able to train a very large neural network.

And so the rise of fast computers, including most law, but also the rise of specialized processors, such as graphics processor units or GPUs, which you hear more about in the later video, has enabled many companies, not just the giant tech companies, but many, many other companies to be able to train large neural nets on a large enough amount of data in order to get very good performance and drive business value.

The most important idea in AI has been machine learning and specifically supervised learning, which means A to B or input-output mappings.

What enables it to work really well is data.

In the next video, let's take a look at what is data and what data you might already have and how to think about feeding this into AI systems.

Let's go on to the next video.

---
