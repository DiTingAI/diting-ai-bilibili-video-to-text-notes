# Intuitive explanation of deep learning深度学习的直观解释2

> 来源：Week1-What is AI 1.Introduction简介
> 章节：P9

---

## P9 9.Intuitive explanation of deep learning深度学习的直观解释2

### AI润色版
In the last video, you saw how a neural network can be applied to demand prediction, but how can a neural network look at a picture and figure out what's in the picture, or listen to an audio clip and understand what is said in an audio clip?

Let's take a look at a more complex example of applying a neural network to face recognition.

Say you want to build a system to recognize people from pictures. How can a piece of software look at this picture and figure out the identity of the person in it?

Let's zoom into a little square like that to better understand how a computer sees pictures. Where you and I see a human eye, a computer instead sees that.

It sees this grid of pixel brightness values that tells it for each of the pixels in the image. How bright is that pixel?

If it were a black and white or a gray scale image, then each pixel would correspond to a single number telling you how bright that pixel is.

If it is a color image, then each pixel would actually have three numbers corresponding to how bright the red, green, and blue elements of that pixel are.

So the neural network's job is to take as input a lot of numbers like these and tell you the name of the person in the picture.

In the last video, you saw how a neural network can take as input four numbers corresponding to the price, shipping cost, amount of marketing, and the cloth material of a t-shirt and output demand.

In this example, the neural network just has to input a lot more numbers corresponding to all of the pixel brightness values of this picture.

If the resolution of this picture is 1000 pixels by 1000 pixels, then that's a million pixels.

So if it were a black and white or a gray scale image, this neural network would take as input a million numbers corresponding to the brightness of all one million pixels in this image.

Or if it was a color image, it would take as input three million numbers corresponding to the red, green, and blue values of each of these one million pixels in this image.

Similar to before, you will have many, many of these artificial neurons computing various values.

And it's not your job to figure out what these neurons should compute.

The neural network will figure it out by itself.

But typically, when you give it an image, the neurons in the earlier parts of the neural network will learn to detect edges in pictures.

And then a little bit later, it will learn to detect parts of objects.

So it may learn to detect eyes and noses and the shape of cheeks and the shape of mouths.

And then the later neurons further to the right will learn to detect different shapes of faces.

And it will finally put all this together to output the identity of the person in the image.

And again, part of the magic of neural networks is that you don't really need to worry about what it is doing in the middle.

All you need to do is give it a lot of data of pictures like this A as well as the correct identity B.

And the learning algorithm will figure out by itself what each of these neurons in the middle should be computing.

Congratulations on finishing all the videos for this week.

You now know how machine learning and data science work.

I look forward to seeing you in next week's videos as well, where you learn how to build your own machine learning or data science project.

See you next week.

---
