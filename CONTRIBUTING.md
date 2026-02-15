# Contributing to the Analog Open Science Academy

Thank you for helping us build the ultimate open-source photography curriculum! Whether you are a student, a chemistry teacher, or a photographer, we need your expertise.

## 🎓 How to Contribute
1.  **Fork** this repository.
2.  **Clone** your fork to your machine.
3.  **Create a Branch** for your changes (`git checkout -b feature/new-lesson-name`).
4.  **Push** to your fork and submit a **Pull Request**.

## 📂 Directory Standards
Please place your content in the correct academic level:
* `01_primary` - No dangerous chemicals, simple physics.
* `02_secondary` - Basic algebra, household chemistry (Vitamin C, Coffee).
* `03_high_school` - Calculus/Trig allowed, standard darkroom chemistry.
* `04_university` - Advanced synthesis, raw chemical handling, critical theory.

## 📝 Style Guide

### 1. Mathematics
We use **LaTeX** for all formulas. Please enclose math in `$` or `$$`.
* *Incorrect:* E = I * t
* *Correct:* `$E = I \times t$`

### 2. Chemical Safety (MSDS)
**Crucial:** If your lesson involves chemistry, you must include a Safety Warning block at the top.

```markdown
> ⚠️ **SAFETY WARNING**
> This experiment uses **Silver Nitrate**.
> * Wear gloves and eye protection.
> * Do not pour waste down the drain without neutralization.