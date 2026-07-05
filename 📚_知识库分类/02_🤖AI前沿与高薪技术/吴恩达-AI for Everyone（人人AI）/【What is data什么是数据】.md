# What is data什么是数据

> 来源：Week1-What is AI 1.Introduction简介
> 章节：P3

---

## P3 3.What is data什么是数据

### AI润色版
You may have heard that data is really important for building AI systems, but what is data really? Let's take a look。

Let's look at an example of a table of data, which we also call a data set。

If you're trying to figure out how to price houses that you're trying to buy or sell, you might collect a data set like this, and this can be just a spreadsheet, like an Excel spreadsheet of data, where one column is the size of the house, say in square feet or square meters, and the second column is the price of the house。

And so if you're trying to build an AI system or a machine learning system to help you set prices for houses, or figure out that the house is priced appropriately, you might decide that the size of the house is A and the price of the house is B, and have an AI system learn this input to output, or A to B mapping。

Now, rather than just pricing a house based on the size, you might say, well, let's also collect data on the number of bedrooms of this house。

In that case, A can be both of these first two columns, and B can be just the price of the house。

So given a table of data, given a data set, it's actually up to youup to your business use caseto decide what is A and what is B。

Data is often unique to your business。

And this is an example of a data set that a real estate agency might have if they're trying to help price houses。

And it's up to you to decide what is A and what is B, and how to choose these definitions of A and B to make it valuable for your bu
siness。

As another example, if you have a certain budget and you want to decide what is the size of house you can afford, then you might decide that the input A is how much does someone spend, and B is just the size of the house in square feet。

And that would be a totally different choice of A and B that tells you, given a certain budget, what's the size of the house you should be maybe looking at。

Here's another example of a data set。

Let's say that you want to build an AI system to recognize cats in pictures。

I'm not sure why you might want to do that, but maybe have a fun mobile app and you want to tag all the pictures of cats。

So you might collect the data sets where the input A is a set of different images, and the output B are labels that says first picture's a cat, there's not a cat, there's a cat, there's not a cat, and have an AI input a picture A and output B is it a cat or notso you can tag all the cat pictures on your photo feed, or on your mobile app。

In machine learning tradition, there's actually a lot of cats in machine learning。

I think some of this started when I was leading the Google Brain Team, and we published the results with a somewhat infamous Google cat, where an AI system learned to detect cats from watching YouTube videos。

But since then, there's been a tradition of using cats as a running example when talking about machine learning。

We've apologized to all the dog lovers out there. I love dogs, too。

So data is important, but how do you 
get data? How do you acquire data?

Well, one way to get data is manual labeling。

For example, you might collect a set of pictures like these over here, and then you might either yourself or have someone else go through these pictures and label each of them。

So the first one is a cat, second one is not a cat, third one is a cat, fourth one is not a cat, and by manually labeling each of these images, you now have a data set for building a cat detector。

To do that, you actually need more than four pictures。

You might need hundreds of thousands of pictures, but manual labeling is a tried-and-true way of getting a data set where you have both A and B。

Another way to get a data set is from observing user behaviors, or other types of behaviors。

So for example, let's say you run a website that sells things online, so an e-commerce, or an electronic commerce website, where you offer things to users at different prices, and you can just observe if they buy your product or not。

So just through the act of either buying or not buying your product, you may be able to collect a data set like this。

We can store the user ID, the time the user visited your website, the price you offer the product to the users, as well as whether or not they purchased it。

And so just by using your website, users can generate this data from you。

This was an example of observing user behaviors。

We can also observe behaviors of other things, such as machines。

If you run a large machine in a factory, a
nd you want to predict if a machine is about to fail or have a fault, then just by observing the behavior of a machine, you can then record a data set like this。

There's a machine ID, there's a temperature of the machine, there's a pressure within the machine, and then did the machine fail or not?

And if your application predictive maintenance, say you want to figure out if a machine is about to fail, then you could, for example, choose this as the input A, and choose that as the output B to try to figure out if a machine is about to fail, in which case you might do maintenance, preventative maintenance on the machine。

The third and very common way of acquiring data is to download it from a website, or to get it from a partner。

Thanks to the open internet, there's just so many data sets that you can download freely, ranging from computer vision, or image data sets, to self-driving car data sets, to speech recognition data sets, to medical imaging data sets, to many, many more。

And so if your application needs a type of data to just download off the web, keeping in mind licensing and copyright, then that could be a great way to get started on an application。

And finally, if you work with a partner, say you're working with a factory, then they may already have collected a big data set of machines and temperatures and pressure into the machine's fail or not that they could give to you。

Data is important, but it's also a little bit overhyped, and sometimes misused。

Let 
me describe to you two of the most common misuses, or the bad ways of thinking about data。

When I speak of CEOs of large companies, a few of them have actually said to me, hey Andrew, give me three years to build up my IT team。

We're collecting so much data。

And then after three years, I'll have this perfect data set and then we'll do AI then。

It turns out that's a really bad strategy。

Instead, what I recommend to every company is once you start to collecting some data, go ahead and start showing it, or feeding it to an AI team。

Because often the AI team can give feedback to your IT team on what types of data to collect and what types of IT infrastructure to keep on building。

For example, maybe an AI team can look at your factory data and say, hey, you know what?

If you can collect data from this big manufacturing machine, not just once every 10 minutes, but instead once every one minute, then we could do a much better job building a preventative maintenance system for you。

So there's often this interplay of this back and forth between IT and AI teams。

And my advice is usually try to get feedback from AI earlier because it can help you guide the development of your IT infrastructure。

Second, misuse of data。

Unfortunately, I've seen some CEOs read about the importance of data in the news, and then say, hey, I have so much data。

Surely an AI team can make it valuable。

And unfortunately, this doesn't always work out。

More data is usually better than less data, but
I wouldn't take it for granted just because you have many terabytes or gigabytes of data that an AI team can magically make that valuable。

So my advice is don't throw data in AI team and assume it will be valuable。

In fact, in one extreme case, I saw one company go and acquire a whole string of other companies in medicine on the thesis on the hypothesis that their data would be very valuable。

And now a couple years later, far as I know, the engineers have not yet figured out how to take all this data and actually create value all of it。

So sometimes it works and sometimes it doesn't, but I would not overinvest in just acquiring data for the sake of data until unless you're also getting an AI team to take a look at it, because they can help guide you to think through what is the data that is actually the most valuable。

Finally, data is messy。

You may have heard the phrase garbage in, garbage out。

And if you have bad data, then the AI will learn inaccurate things。

Here are some examples of data problems。

Let's say you have this data set of size of houses, number of bedrooms and the price。

You can have incorrect labels or just incorrect data。

For example, this house is probably not going to sell for 0.001 thousand dollars, just the one dollar。

Or data can also have missing values, such as we have here a whole bunch of unknown values。

And so your AI team will need to figure out how to clean up the data or how to deal with these incorrect labels and or missing values
。

And there are also multiple types of data。

For example, sometimes you hear about images, audio and text。

These are types of data that humans find very easy to interpret。

There's a term for this。

This is called unstructured data。

And there's a certain types of AI techniques that could work with images to recognize cats, audio to recognize speech, or text to understand if an email was spam。

And then there are also data sets like the one on the right。

This is an example of structured data。

And that basically means data that lives in a giant spreadsheet。

And the techniques for dealing with unstructured data are a little bit different than the techniques for dealing with structured data。

But AI techniques can work very well for both of these types of data, unstructured data and structured data。

In this video, you learned what is data and you also saw how not to misuse data。

For example, by over investing in an IT infrastructure in the hope that it will be useful for AI in the future。

But we're actually checking that it really will be useful for the AI applications you want to build。

And finally, you saw data is messy。

But a good AI team will be able to help you deal with all of these problems。

Now, AI has a complicated terminology where people throw around terms like AI, machine learning, data science。

What I want to do in the next video is share with you what these terms actually mean so that you can confidently and accurately talk about these concepts with
 others。

Let's go on to the next video。

---


---

### 📖 英文原版

## P3 3.What is data什么是数据

### AI润色版
You may have heard that data is really important for building AI systems, but what is data really? Let's take a look.

Let's look at an example of a table of data, which we also call a

data set. If you're trying to figure out how to price houses that you're trying to buy or sell,

you might collect a data set like this and this can be just a spreadsheet, like an Excel spreadsheet of data,

where one column is the size of the house, say in square feet or square meters, and the second column is the price of the house.

And so if you're trying to build an AI system or a machine learning system to help you set prices for houses or figure out

that the house is priced appropriately, you might decide that the size of the house is A and

the price of the house is B and have an AI system

learn this input to output or A to B mapping.

Now, rather than just pricing a house based on the size, you might say,

well, let's also collect data on the number of bedrooms of this house. In that case, A can be both of these

first two columns and B can be

just the price of the house.

So given a table of data, given a data set, it's actually up to you, up to your business use case to decide

what is A and what is B.

Data is often unique to your business.

And this is an example of a data set that a real estate agency might have if they're trying to help price houses.

And it's up to you to decide what is A and what is B, and how to choose these definitions of A and B

to make it valuable for your business. As another example, if you have a certain budget and you want to decide

what is the size of house you can afford, then you might decide that the input A is how much does someone spend and

B is

just the size of the house in square feet.

And that would be a totally different choice of A and B that tells you, given a certain budget,

what's the size of the house you should be maybe looking at. Here's another example of a data set.

Let's say that you want to build an AI system to recognize cats in pictures.

I'm not sure why you might want to do that, but maybe have a fun mobile app and you want to tag all the pictures of cats.

So you might collect the data sets where the input A is

set of different images and the output B are labels that says

first picture's a cat, there's not a cat, there's a cat, there's not a cat, and have an AI input a picture A and

output B, is it a cat or not, so you can tag all the cat pictures on your photo feed or on your mobile app.

In machine learning tradition, there's actually a lot of cats in machine learning.

I think some of this started when I was leading the Google Brain Team and we published the results with a

somewhat infamous Google cat, where an AI system learned to detect cats from watching YouTube videos.

But since then, there's been a tradition of using cats as a running example when talking about machine learning.

We've apologized to all the dog lovers out there. I love dogs, too.

So data is important, but how do you get data? How do you acquire data?

Well, one way to get data is manual labeling. For example, you might collect a set of pictures like these over here and

then you might either yourself or have someone else go through these pictures and label each of them.

So the first one is a cat, second one is not a cat, third one is a cat, fourth one is not a cat, and

by manually labeling each of these images, you now have a data set for building a cat detector.

To do that, you actually need more than four pictures.

You might need hundreds of thousands of pictures, but manual labeling is a tried-and-true way of getting a data set

where you have both A and B.

Another way to get a data set is from observing user behaviors or other types of behaviors.

So for example, let's say you run a website that sells things online, so an e-commerce or an electronic commerce website

where you offer things to users at different prices and you can just observe if they buy your product or not.

So just through the act of either buying or not buying your product, you may be able to collect a data set like this.

We can store the user ID, the time the user visited your website, the price you offer the product to the users,

as well as whether or not they purchased it.

And so just by using your website, users can generate this data from you.

This was an example of observing user behaviors.

We can also observe behaviors of other things, such as machines.

If you run a large machine in a factory and you want to predict if a machine is about to fail or have a fault,

then just by observing the behavior of a machine, you can then record a data set like this.

There's a machine ID, there's a temperature of the machine, there's a pressure within the machine,

and then did the machine fail or not?

And if your application prevents the maintenance, say you want to figure out if a machine is about to fail,

then you could, for example, choose this as the input A and choose that as the output B to try to figure out

if a machine is about to fail, in which case you might do maintenance, preventative maintenance on the machine.

The third and very common way of acquiring data is to download it from a website or to get it from a partner.

Thanks to the open internet, there's just so many data sets that you can download freely,

ranging from computer vision or image data sets, to self-driving car data sets, to speech recognition data sets,

to medical imaging data sets, to many, many more.

And so if your application needs a type of data to just download off the web,

keeping in mind licensing and copyright, then that could be a great way to get started on an application.

And finally, if you work with a partner, say you're working with a factory,

then they may already have collected a big data set of machines and temperatures and pressure

into the machine's fail or not that they could give to you.

Data is important, but it's also a little bit overhyped and sometimes misused.

Let me describe to you two of the most common misuses or the bad ways of thinking about data.

When I speak of CEOs of large companies, a few of them have actually said to me,

hey Andrew, give me three years to build up my IT team.

We're collecting so much data.

And then after three years, I'll have this perfect data set and then we'll do AI then.

It turns out that's a really bad strategy.

Instead, what I recommend to every company is once you start collecting some data,

go ahead and start showing it or feeding it to an AI team.

Because often the AI team can give feedback to your IT team on what types of data to collect

and what types of IT infrastructure to keep on building.

For example, maybe an AI team can look at your factory data and say,

hey, you know what?

If you can collect data from this big manufacturing machine, not just once every 10 minutes,

but instead once every one minute, then we could do a much better job

building a preventative maintenance system for you.

So there's often this interplay of this back and forth between IT and AI teams.

And my advice is usually try to get feedback from AI earlier

because it can help you guide the development of your IT infrastructure.

Second, misuse of data.

Unfortunately, I've seen some CEOs read about the importance of data in the news

and then say, hey, I have so much data.

Surely an AI team can make it valuable.

And unfortunately, this doesn't always work out.

More data is usually better than less data,

but I wouldn't take it for granted just because you have many

terabytes or gigabytes of data that an AI team can magically make that valuable.

So my advice is don't throw data in AI team and assume it will be valuable.

In fact, in one extreme case, I saw one company go and acquire a whole string

of other companies in medicine on the thesis on the hypothesis

that their data would be very valuable.

And now a couple years later, far as I know,

the engineers have not yet figured out how to take all this data

and actually create value all of it.

So sometimes it works and sometimes it doesn't,

but I would not overinvest in just acquiring data for the sake of data

unless you're also getting an AI team to take a look at it

because they can help guide you to think through what is the data

that is actually the most valuable.

Finally, data is messy.

You may have heard the phrase garbage in, garbage out.

And if you have bad data, then the AI will learn inaccurate things.

Here are some examples of data problems.

Let's say you have this data set of size of houses, number of bedrooms and the price.

You can have incorrect labels or just incorrect data.

For example, this house is probably not going to sell for 0.001 thousand dollars,

just the one dollar.

Or data can also have missing values such as we have here a whole bunch of

unknown values.

And so your AI team will need to figure out how to clean up the data

or how to deal with these incorrect labels and or missing values.

And there are also multiple types of data.

For example, sometimes you hear about images, audio and text.

These are types of data that humans find very easy to interpret.

There's a term for this.

This is called unstructured data.

And there's a certain types of AI techniques that could work with images to recognize

cats, audio to recognize speech or text to understand if an email was stamped.

And then there are also data sets like the one on the right.

This is an example of structured data.

And that basically means data that lives in a giant spreadsheet.

And the techniques for dealing with unstructured data are a little bit

different than the techniques for dealing with structured data.

But AI techniques can work very well for both of these types of data,

unstructured data and structured data.

In this video, you learned what is data and you also saw how not to misuse data.

For example, by over investing in an IT infrastructure

in the hope that it will be useful for AI in the future.

But we're actually checking that it really will be useful for the AI applications

you want to build.

And finally, you saw data is messy.

But a good AI team will be able to help you deal with all of these problems.

Now, AI has a complicated terminology where people throw around terms like AI,

machine learning, data science.

What I want to do in the next video is share with you what these terms actually mean

so that you can confidently and accurately talk about these concepts with others.

Let's go on to the next video.

---
