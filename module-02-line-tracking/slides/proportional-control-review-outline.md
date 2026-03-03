# Proportional Control Review -- Slide Outline

**Purpose:** A visual review of proportional control concepts before moving into classes. Goal is to build deep intuition, not re-teach the code.

**Time:** ~20 minutes

---

## Slide 1: Title

**Proportional Control Review**

Before we move on, let's make sure we REALLY understand what proportional control is doing -- not just the code, but the idea.

---

## Slide 2: The Shower Analogy

**Proportional control is something you already do every day.**

**[Illustration: A person at a shower with a temperature dial. Three panels:]**

| Panel | Water temp | How you feel | What you do |
|---|---|---|---|
| 1 | Way too cold | Very uncomfortable | Turn the knob a LOT toward hot |
| 2 | A little too cold | Slightly uncomfortable | Turn the knob a LITTLE toward hot |
| 3 | Just right | Comfortable | Do nothing |

**The key idea:** How much you turn the knob depends on how far off the temperature is.

- **A little off? Small adjustment.**
- **Way off? Big adjustment.**

That is proportional control. The response is PROPORTIONAL to the error.

---

## Slide 3: The Same Idea, Applied to the Robot

**The robot does the same thing with the line.**

**[Illustration: Top-down view of a line with five robot positions labeled A through E, spread from far left of the line to far right:]**

```
  White surface          LINE          White surface
        A       B       C       D       E
      (far    (a bit  (on the  (a bit  (far
      left)    left)   edge)   right)  right)
```

| Position | Sensor reads | How far off? | What robot does |
|---|---|---|---|
| A (far left of line) | 0.1 | Very far | Steer HARD toward line |
| B (a little left) | 0.3 | A little | Steer gently toward line |
| C (on the edge) | 0.5 | Perfect | Drive straight |
| D (a little right) | 0.7 | A little | Steer gently away from line |
| E (far right of line) | 0.9 | Very far | Steer HARD away from line |

**Same principle as the shower:** bigger error = bigger correction.

---

## Slide 4: What is "Error"?

**Error = how far am I from where I want to be?**

```
error = setpoint - sensor_reading
```

**[Illustration: A number line from 0.0 to 1.0. The setpoint (0.5) is marked with a flag in the center. Arrows show the distance from various sensor readings to the setpoint:]**

```
0.0       0.2       0.4    0.5    0.6       0.8       1.0
 |----white----|---------|---*---|---------|----black----|
                          setpoint

  Sensor reads 0.2:  error = 0.5 - 0.2 = +0.3  (steer toward line -->)
  Sensor reads 0.5:  error = 0.5 - 0.5 =  0.0  (perfect, go straight)
  Sensor reads 0.8:  error = 0.5 - 0.8 = -0.3  (<-- steer away from line)
```

**Two things the error tells you:**
1. **The sign** (+/-) tells you WHICH DIRECTION to steer
2. **The size** (big/small) tells you HOW MUCH to steer

---

## Slide 5: What is Kp?

**Kp controls how aggressively the robot reacts.**

Think of Kp as the robot's personality:

**[Illustration: Three cartoon robots with personality labels:]**

| Kp value | Personality | Behavior |
|---|---|---|
| Low (0.1) | "Lazy robot" | Barely reacts, drifts off the line |
| Medium (0.5) | "Calm robot" | Smooth, steady corrections |
| High (2.0) | "Nervous robot" | Overreacts, zigzags wildly |

```
correction = error * Kp
```

**Same error, different Kp:**

| error | Kp = 0.1 | Kp = 0.5 | Kp = 2.0 |
|---|---|---|---|
| +0.3 | 0.03 (tiny steer) | 0.15 (moderate steer) | 0.60 (HUGE steer) |
| -0.3 | -0.03 (tiny steer) | -0.15 (moderate steer) | -0.60 (HUGE steer) |

**Kp is a volume knob for the correction.**

---

## Slide 6: What Does This Look Like on the Track?

**[Illustration: Three birds-eye-view paths around a curved line, each labeled:]**

**Path 1: Kp too low (0.1) -- "Lazy robot"**
```
Line:     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Robot:    ~~~~~~~~~~~~~~~
                         ~~~~~~~~  (drifts off, can't keep up with the curve)
```

**Path 2: Kp just right (0.5) -- "Calm robot"**
```
Line:     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Robot:    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  (smooth, stays on the line)
```

**Path 3: Kp too high (2.0) -- "Nervous robot"**
```
Line:     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Robot:    ~/\/\/\/\/\/\/\/\/\/\/\/\/\~  (zigzags back and forth across the line)
```

**The goal of tuning:** Find the Kp where the robot follows smoothly without oscillating.

---

## Slide 7: The Four Steps -- Every Single Loop

**The control loop does the same four steps, hundreds of times per second:**

**[Illustration: Circular flow diagram with four boxes connected by arrows, labeled 1-2-3-4 and looping back to 1:]**

```
    +---> 1. READ SENSOR ----> 2. CALCULATE ERROR ---+
    |         (where am I?)      (how far off am I?)  |
    |                                                  |
    +--- 4. SET MOTORS <---- 3. CALCULATE CORRECTION --+
         (adjust steering)     (how much do I fix?)
```

**Trace it with real numbers:**

```
1. Read sensor:          sensor_value = 0.2
2. Calculate error:      error = 0.5 - 0.2 = +0.3
3. Calculate correction: correction = 0.3 * 0.5 = 0.15
4. Set motors:           arcade(0.3, 0.15)
                         --> left motor = 0.45, right motor = 0.15
                         --> robot steers right, toward the line
```

**Then it does it again. And again. And again. Hundreds of times per second.**

---

## Slide 8: Let's Trace It Together

**Work through these as a class. For each row, calculate error, correction, and what each motor gets.**

Settings: `setpoint = 0.5`, `Kp = 0.5`, `base_effort = 0.3`

| sensor_value | error = 0.5 - sensor | correction = error * 0.5 | arcade(0.3, correction) | Left motor | Right motor | Which way? |
|---|---|---|---|---|---|---|
| 0.5 | ? | ? | ? | ? | ? | ? |
| 0.2 | ? | ? | ? | ? | ? | ? |
| 0.8 | ? | ? | ? | ? | ? | ? |
| 0.1 | ? | ? | ? | ? | ? | ? |
| 0.6 | ? | ? | ? | ? | ? | ? |

**Answers (reveal one at a time):**

| sensor_value | error | correction | Left motor | Right motor | Which way? |
|---|---|---|---|---|---|
| 0.5 | 0.0 | 0.0 | 0.30 | 0.30 | Straight |
| 0.2 | +0.3 | +0.15 | 0.45 | 0.15 | Steer right (toward line) |
| 0.8 | -0.3 | -0.15 | 0.15 | 0.45 | Steer left (away from line) |
| 0.1 | +0.4 | +0.20 | 0.50 | 0.10 | Steer hard right |
| 0.6 | -0.1 | -0.05 | 0.25 | 0.35 | Gentle steer left |

---

## Slide 9: Two Sensors -- Even Simpler

**With two sensors, the error calculation gets easier:**

```
error = left_sensor - right_sensor
```

**No setpoint needed!**

**[Illustration: Top-down view of a line with two sensors straddling it, three positions:]**

```
Position 1: Centered          Position 2: Drifted left       Position 3: Drifted right
   [L]  LINE  [R]                [L]  LINE       [R]            [L]       LINE  [R]
   0.5        0.5                0.8        0.2                 0.2             0.8
   error = 0.0                   error = +0.6                   error = -0.6
   "Go straight"                 "Steer left to fix"            "Steer right to fix"
```

**Why is this better than one sensor?**
- One sensor: follows the EDGE of the line, can only see one side
- Two sensors: follows the CENTER of the line, can see BOTH sides

---

## Slide 10: The Big Picture -- Why This Matters

**Proportional control is not just a robotics trick. It is everywhere:**

| System | Setpoint | Sensor | Correction |
|---|---|---|---|
| Shower temperature | Desired temp | Your skin | Turn the knob |
| Cruise control | Set speed | Speedometer | Throttle up/down |
| Line-following robot | 0.5 (edge) | Reflectance sensor | Steer left/right |
| Thermostat | 72 degrees F | Thermometer | Heat on/off |

**The same pattern every time:**
1. Measure where you are
2. Calculate how far off you are (error)
3. Respond proportionally

**You now understand one of the most important ideas in engineering.**

---

## Slide 11: Quick Check -- Can You Answer These?

1. The sensor reads 0.3 and the setpoint is 0.5. What is the error? Is it positive or negative? Which way should the robot steer?

2. Two students both have error = 0.3. Student A uses Kp = 0.2, Student B uses Kp = 1.0. Whose robot steers harder? Whose robot is more likely to oscillate?

3. Your robot is zigzagging wildly across the line. Should you increase or decrease Kp?

4. Your robot slowly drifts off the line on curves. Should you increase or decrease Kp?

5. Why can't we use `straight()` and `turn()` for line following? What makes `arcade()` different?

**Discuss with a partner, then we will go through them together.**
