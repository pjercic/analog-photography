# ⏱️ Darkroom Physics: Arithmetic vs. f/stop Printing

## 🌟 The Big Question
When you use a camera, you control light in "stops" (halving or doubling the light). But when you go into the darkroom to print your photo, you use a clock that counts in regular seconds (1, 2, 3, 4...). 

Why do we use the *geometry* of stops in the camera, but the *arithmetic* of a clock in the darkroom? The short answer is: we shouldn't! In this lesson, we will learn how to print photos using "f/stop timing" to gain perfect control over our final image.



---

## 1. The Problem with Normal Clocks (Arithmetic Timing)
Imagine you are making a **Test Strip** in the darkroom to figure out how long to expose your paper. 

Traditionally, a photographer covers the paper with cardboard and moves it every 5 seconds. The resulting strip shows exposures of:
**10s, 15s, 20s, 25s, 30s...**

This is called **Arithmetic Timing** because you are adding the exact same amount of time (+5 seconds) to each step. But there is a hidden math problem here:
* The jump from **10s to 15s** is a 50% increase in light (a massive visual jump).
* The jump from **25s to 30s** is only a 20% increase in light (a very tiny visual jump).

Because photographic paper reacts to light exponentially, your test strip will be a mess. The light end will have huge, blocky jumps in tone, while the dark end will look almost exactly the same from step to step!

---

## 2. The Solution: Geometric (f/stop) Timing
To fix this, we need to treat the darkroom timer just like a camera shutter. We need to increase the light by a constant *percentage* (a geometric series), rather than a constant amount of seconds.

Instead of adding 5 seconds, we add a **fraction of a stop** (like +1/3 of a stop) to each step. 
* To calculate a 1-stop increase, you multiply the time by 2.
* To calculate a 1/3-stop increase, you multiply the time by $2^{1/3}$ (which is about 1.26).

If we start at 10 seconds and increase by 1/3 of a stop each time, our timer sequence looks like this:
**10s, 12.6s, 15.9s, 20s, 25.2s, 31.7s...**



### Why is this better?
Because every single step on the test strip is exactly 26% more light than the last one, the visual difference between every gray band is perfectly even. It makes choosing your "Base Exposure" incredibly easy!

---

## 3. The Magic of the Printing Map
Once you find your Base Exposure (let's say it is 19 seconds), you usually need to make certain parts of the photo lighter (Dodging) or darker (Burning). 

**The Old Way:** "I will burn the sky for 5 seconds."
* *The problem:* If you decide to print the photo twice as big tomorrow, your Base Exposure will be much longer. That 5-second burn will no longer work; it will be too weak. You have to guess all over again!

**The f/stop Way:** "I will burn the sky for +1/3 of a stop."
* *The magic:* Because 1/3 of a stop is a percentage, it scales automatically! If you print the photo bigger tomorrow, you just look at your f/stop chart. A +1/3 stop burn will always darken the sky by the exact same visual amount, forever, no matter what size paper you use or what chemistry you buy.

By making a "Printing Map" using f/stop fractions instead of raw seconds, your darkroom notes become universal formulas.
