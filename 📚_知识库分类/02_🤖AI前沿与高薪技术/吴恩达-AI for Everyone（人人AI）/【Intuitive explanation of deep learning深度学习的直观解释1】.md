# Intuitive explanation of deep learning深度学习的直观解释1

> 来源：Week1-What is AI 1.Introduction简介
> 章节：P8

---

## P8 8.Intuitive explanation of deep learning深度学习的直观解释1

### AI润色版
The terms deep learning and neural network are used almost interchangeably in AI.

And even though they're great for machine learning, there's also been a bit of hype and a bit of mystique about them.

This video will demystify deep learning so that you have a sense of what deep learning and neural networks really are.

Let's use an example from demand prediction.

Let's say you run a website that sells t-shirts and you want to know based on how you price the t-shirts, how many units you expect to sell, how many t-shirts you expect to sell.

You might then create a dataset like this where the higher the price of the t-shirt, the lower the demand.

So you might fit a straight line to this data showing that as the price goes up, the demand goes down.

Now demand can never go below zero so maybe you say that the demand will flatten out at zero and be at a certain point.

You expect pretty much no one to buy any t-shirts.

It turns out this blue line is maybe the simplest possible neural network.

You have as input the price A and you want it to output the estimated demand B.

So the way you would draw this as a neural network is that the price would be input to this little round thing there and this little round thing outputs the estimated demand.

In the terminology of AI, this little round thing here is called a neuron or sometimes is called an artificial neuron and all it does is compute this blue curve that I've drawn here on the left.

This is maybe the simplest possible neural network with a single artificial neuron that just inputs the price and outputs the estimated demand.

If you think of this orange circle, this artificial neuron as a little Lego brick, all that the neural network is is if you take a lot of these Lego bricks and stack them on top of each other until you get a big pile, a big network of these neurons.

Let's look at a more complex example.

Suppose that instead of knowing only the price of the t-shirts, you also have the shipping cost that the customers will have to pay to get the t-shirts.

Maybe you spend more or less on marketing in a given week and you can also make the t-shirt out of a thick, heavy, expensive cotton or a much cheaper, more lightweight material.

These are some of the factors that you think will affect the demand for your t-shirts.

Let's see what a more complex neural network might look like.

You know that your customers care a lot about affordability.

So let's say you have one neuron and let me draw this one in blue whose job it is to estimate the affordability of the t-shirts.

And because affordability is mainly a function of the price of the shirts and of the shipping cost.

A second thing that will affect the demand for your t-shirts is awareness.

How much are consumers aware that you're selling this t-shirt?

So the main thing that affects awareness is going to be your marketing.

So let me draw here a second artificial neuron that inputs your marketing budget, how much you spent on marketing and outputs how aware consumers are of your t-shirt.

Finally, the perceived quality of your product will also affect demand and perceived quality would be affected by marketing.

If the marketing tries to convince people this is a high quality t-shirt and sometimes the price of something also.

Affects perceived quality.

So I'm going to draw here a third artificial neuron that inputs price, marketing and material and tries to estimate the perceived quality of your t-shirts.

Finally, now that the earlier neurons, these three blue neurons have figured out how affordable, how much consumer awareness and what's the perceived quality.

You can then have one more neuron over here that takes as input these three factors and outputs the estimated demand.

So this is a neural network and its job is to learn to map from these four inputs.

That's the input A to the output B to demand.

So it learns this input output or A to B mapping.

This is a fairly small neural network with just four artificial neurons.

In practice, neural networks used today are much larger with easily thousands, tens of thousands or even much larger than that numbers of neurons.

Now, there's just one final detail of this description that I want to clean up, which is that in the way of describing neural network, it was as if you had to figure out that the key factors are affordability, awareness and perceived quality.

One of the wonderful things about using neural networks is that to train a neural network, in other words, to build a machine learning system using a neural network.

All you have to do is give it the input A and the output B and it figures out all of the things in the middle by itself.

So to build a neural network, what you would do is feed it lots of data with the input A and have a neural network that just looks like this with a few blue neurons feeding to a yellow output neuron.

And then you have to give it data with the demand B as well.

And it's the software's job to figure out what these blue neurons should be computing so that it can completely automatically learn the most accurate possible function mapping from the input A to the output B.

And it turns out that if you give this enough data and train a neural network that is big enough, this can do an incredibly good job mapping from inputs A to outputs B.

So that's a neural network.

It's a group of artificial neurons, each of which computes a relatively simple function, but when you stack enough of them together like LEGO bricks, they can compute incredibly complicated functions that give you very accurate mappings from the input A to the output B.

Now, in this video, you saw an example of neural networks applied to demand prediction.

Let's go into the next video to see a more complex example of neural networks applied to face recognition.

---
