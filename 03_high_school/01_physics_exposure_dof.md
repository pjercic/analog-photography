# 🧮 Physics: The Reciprocity Law & Depth of Field

> **Level:** 3 (High School)
> **Topic:** Optics, Algebra, and Exposure Mechanics
> **Prerequisite:** Level 2 (Lenses & The Latent Image)

## 🌟 The Big Question
Up until now, we have treated light as a magical element that simply enters a hole and makes a picture. But in professional photography, light is a measurable quantity. 

How do we perfectly balance the *amount* of light hitting the film with the *geometry* of the lens to create both a perfect exposure and a perfectly sharp image? To do this, we must turn to algebra.

---

## 1. The Reciprocity Law ($E = I \times t$)
In 1862, scientists Robert Bunsen and Henry Roscoe discovered that the photochemical effect of light is directly proportional to the total energy absorbed. In photography, this is known as the **Reciprocity Law**.

The fundamental equation of photographic exposure is:
$$E = I \times t$$

* **$E$** = Exposure (The total amount of light that hits the film).
* **$I$** = Intensity (How wide the lens opening is, controlled by the **Aperture**).
* **$t$** = Time (How long the light is allowed in, controlled by the **Shutter Speed**).

### The Bucket Analogy
Think of Exposure ($E$) as filling a bucket to the very brim with water.
* **Intensity ($I$)** is the width of the hose.
* **Time ($t$)** is how long you leave the water running.

If you want to fill the bucket perfectly, you have choices that are *reciprocal* (inversely proportional):
1. Use a very wide hose (high $I$) and turn the water on for a short time (low $t$).
2. Use a tiny straw (low $I$) and turn the water on for a long time (high $t$).

In photography, if you cut the size of your lens opening in half, you must double your shutter speed time to get the exact same exposure.



---

## 2. When Physics Breaks: The Schwarzschild Effect
The Reciprocity Law works perfectly for fractions of a second (e.g., 1/125s, 1/500s). But what happens if you take a photograph of the stars at night, and your exposure takes 5 minutes?

Astronomer Karl Schwarzschild discovered that at very low light intensities over long times, **the law fails**. The silver halide crystals on the film become inefficient at trapping photons. A 10-second metered exposure might actually require 25 seconds of real time to properly expose!

To correct this **Reciprocity Failure**, photographers use an exponential formula:
$$t_c = t_m^p$$

* **$t_c$** = Corrected Time (The actual time you must leave the shutter open).
* **$t_m$** = Metered Time (The time your light meter tells you, assuming perfect physics).
* **$p$** = The Schwarzschild Factor (A constant unique to every film emulsion, usually between 1.2 and 1.5).

*(Note: You can run the Python simulation for this in our Jupyter Notebook: `01_physics_reciprocity.ipynb`)*

---

## 3. The Geometry of Sharpness: Depth of Field
When we adjust our Aperture ($I$) to change the exposure, we accidentally change the physics of our lens focus. 

Only one exact mathematical plane in front of the camera is truly in focus. However, human eyes are imperfect. There is a "zone" in front of and behind the focus plane that looks *acceptably sharp*. We call this the **Depth of Field (DoF)**.

### The Circle of Confusion ($c$)
If a point of light is slightly out of focus, it spreads out into a blurry circle on the film. The maximum size this circle can be before the human eye registers it as "blurry" is called the **Circle of Confusion ($c$)**. For standard 35mm film, $c \approx 0.03$ mm.



### The Hyperfocal Distance ($H$)
Photojournalists and landscape photographers often need to know exactly how to set their lens so that *everything* from the foreground to infinity is sharp. This magic distance is called the **Hyperfocal Distance**.

We calculate it using this formula:
$$H = \frac{f^2}{N \cdot c}$$

* **$H$** = Hyperfocal Distance (in millimeters).
* **$f$** = Focal length of the lens (e.g., 50mm).
* **$N$** = The Aperture f-number (e.g., f/8 or f/16).
* **$c$** = Circle of Confusion (e.g., 0.03mm).

**The Rule:** If you focus your lens exactly at distance $H$, everything from half of $H$ all the way to Infinity ($\infty$) will be in focus!

---

## 4. The Artistic Trade-Off
A photographer is constantly doing algebra in their head to make artistic choices.

1. **Sports Photographer:** Needs to freeze a fast-moving athlete. They must use a very fast Time ($t = 1/1000$s). To satisfy $E = I \times t$, they must use a massive Aperture ($I$). A massive aperture creates a very shallow Depth of Field, blurring the background.
2. **Landscape Photographer:** Needs the mountains and the foreground flowers to be sharp. They calculate $H$ and use a tiny Aperture (like f/22). To satisfy $E = I \times t$, they must use a very long Time ($t = 2$ seconds), requiring a heavy tripod so the camera doesn't shake.

*(Note: You can calculate exact focus zones using our Python DoF calculator in `02_physics_dof.ipynb`)*

---

## 📝 Discussion Questions
1. If your light meter tells you the perfect exposure is Aperture f/8 and Time 1/60s, but you want to freeze a moving car by changing your Time to 1/250s (two stops faster), what must you do to your Aperture to maintain the same Exposure ($E$)?
2. Look at the Hyperfocal Distance equation. If you use a telephoto lens with a very large focal length ($f$), what happens to $H$? Does it become easier or harder to keep everything in focus?
3. In digital photography, sensors do not suffer from the Schwarzschild Effect (Reciprocity Failure). How does this give digital astrophotography a mathematical advantage over analog astrophotography?