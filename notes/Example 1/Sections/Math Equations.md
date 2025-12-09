$\LaTeX$ is probably most known for its handling of math. The spacing in math equations and their general look is one of the main points Donald Knuth was focusing on when creating $\TeX$.

## Math with Default $\LaTeX$

Let's explore $\LaTeX$'s capabilities in the Results and Discussion section of our lab report. And let's first add the ninth paragraph of `lipsum` to make it look a little more like a real document:

```latex
\lipsum[9]
```

There are two math modes: inline and block math. To insert an inline math expression, put the expression inside the two dollar signs, like so:

```latex
Here is an inline math expression: $y = ax - 4$. Inline math is displayed as normal text.
```

The result:

![[Pasted image 20251209024618.png]]

You can notice that the math text looks odd compared to all the other text. This is because not all fonts support math, and when that is the case, $\TeX$ uses the default Computer Modern typeface for math expressions. For now, ignore it. We will fix it later.

To add a math block, use two dollar signs instead of one:

```latex
Here is a block equation:

$$
	g(x) = f_2(f_1(x)) = x^2 - 19
$$
```

Here is the result:

![[Pasted image 20251209025402.png]]

You can also use the `equation` environment, and the equation will be numbered. You can also add a label to the equation and reference it using the `\ref` or `\autoref` command:

```latex
Here is a block equation:

\begin{equation}
	g(x) = f_2(f_1(x)) = x^2 - \frac{19}{2} \times 2
	\label{eq:function}
\end{equation}

Look at \autoref{eq:function}.
```

The result:

![[Pasted image 20251209025837.png]]

This is pretty much everything you can do in default $\LaTeX$. And while this is everything you will probably need, we can still make our lives easier and equations prettier.

## AMS Math

The American Mathematical Society created their own extension of $\TeX$, AMS-TeX, which expands the mathematical functionality of the default $\TeX$. In $\LaTeX$, we can access that functionality using the `amsmath`, `amsfonts`, and `amssymb` packages. However, there are too many good tutorials on typesetting math in $\LaTeX$ for us to make yet another one that explains absolutely the same thing. Therefore, here are short tutorials we recommend reading:

- [Mathematical expressions](https://www.overleaf.com/learn/latex/Mathematical_expressions)
- [Subscripts and superscripts](https://www.overleaf.com/learn/latex/Subscripts_and_superscripts)
- [Brackets and Parentheses](https://www.overleaf.com/learn/latex/Brackets_and_Parentheses)
- [Matrices](https://www.overleaf.com/learn/latex/Matrices)
- [Fractions and Binomials](https://www.overleaf.com/learn/latex/Fractions_and_Binomials)
- [Aligning equations with amsmath](https://www.overleaf.com/learn/latex/Aligning_equations_with_amsmath)
- [Operators](https://www.overleaf.com/learn/latex/Operators)
- [Spacing in math mode](https://www.overleaf.com/learn/latex/Spacing_in_math_mode)
- [Integrals, sums and limits](https://www.overleaf.com/learn/latex/Integrals%2C_sums_and_limits)
- [Display style in math mode](https://www.overleaf.com/learn/latex/Display_style_in_math_mode)
- [List of Greek letters and math symbols](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols)
- [Mathematical fonts](https://www.overleaf.com/learn/latex/Mathematical_fonts)

But for now, skip them, because there is no need in memorizing everything you can do with math in $\LaTeX$ now - you will acquire that knowledge with time and practice. Just remember that you can always come here and see these references.

And just to give you an idea of what you can do, I include examples from my own projects below. Again, you don't have to learn every command I used right now, just look at what can be done with $\LaTeX$.

![[Pasted image 20251209032726.png]]

```latex
% apart from the amsmath package,
% you will need the chemformula package for the \ch command
\begin{equation*}
    \begin{gathered}
        \text{\small Protolysis} \\
        \begin{aligned}
            \ch{BX3 &-> [RNH2] B(NHR)3} \\
            \ch{BX3 &-> [H2O] B(OH)3} \\
            \ch{BX3 &-> [ROH] B(OR)3}
        \end{aligned}
    \end{gathered}
    \qquad\qquad\qquad
    \begin{gathered}
        \text{\small Complex formation} \\
        \begin{aligned}
            \ch{BX3 &-> [NR3] X3B-NR3} \\
            \ch{BX3 &-> [SR2] X3B-SR2} \\
            \ch{BX3 &-> [PR3] X3B-PR3}
        \end{aligned}
    \end{gathered}
\end{equation*}
```

![[Pasted image 20251209033143.png]]

```latex
% you will need the siunitx package
\begin{multline}
    \Delta H_\text{mix}/\unit{\joule\per\mole} = \chi_\text{DMSO} (1 - \chi_\text{DMSO}) \sum_{i = 0}^3 h_i \left(1 - 2 \chi_\text{DMSO} \right)^i, \\
    \begin{array}{ll}
        h_0 = \num{-11.30e3} & h_1 = \num{-6.47e3} \\
        h_2 = \num{1.48e3} & h_3 = \num{2.78e3}
    \end{array}
\end{multline}
```

![[Pasted image 20251209033747.png]]

```latex
% you will need the siunitx package
\begin{equation}
    \begin{aligned}
        \varepsilon_0 &= \frac{m}{A} = \frac{4 m}{\pi d^2} = \qty{1.21e-11}{\farad\per\meter} \\
        \Delta \varepsilon_0 &= \sqrt{ \left( \frac{\partial \varepsilon_0}{\partial m} \right)^2 \left(\Delta m\right)^2 + \left( \frac{\partial \varepsilon_0}{\partial d} \right)^2 \left(\Delta d\right)^2 } \\
                             &= \sqrt{ \left( \frac{4}{\pi d^2} \right)^2 \left(\Delta m\right)^2 + \left( -\frac{8 m}{\pi d^3} \right)^2 \left(\Delta d\right)^2 } \\
                             &= \qty{3.41e-13}{\farad\per\meter} \approx \qty{0.03e-11}{\farad\per\meter}
    \end{aligned}
\end{equation}
```

![[Pasted image 20251209034044.png]]

```latex
% you will need the siunitx package
\begin{multline}
    \Delta I_3 = \left[ \left( \frac{R_3 + R_4}{(R_2 + R_3 + R_4)^2} \right)^2 \left( \Delta R_2 \right)^2
                 + \left( -\frac{R_2}{(R_2 + R_3 + R_4)^2} \right)^2 \left( \Delta R_3 \right)^2 \right. \\
                 + \left. \left( -\frac{R_2}{(R_2 + R_3 + R_4)^2} \right)^2 \left( \Delta R_4 \right)^2
                 + \left( \frac{R_2}{R_2 + R_3 + R_4} \right)^2 \left( \Delta I_\text{s} \right)^2 \right]^{1/2} \\
                 = \qty{0.06}{\milli\ampere}
\end{multline}
```

## Fixing the Typeface Issue

The best way you can fix the issue we've encountered in the beginning, is to use a typeface that supports math. Using the default Computer Modern typeface is fine - I actually find it very appealing. But if you want to use something else, you can find what you need by clicking "Fonts with math support" on the main page of the [LaTeX Font Catalogue](https://tug.org/FontCatalogue/). Luckily, there is a [version of TeX Gyre Schola](https://tug.org/FontCatalogue/scholax/) that supports math.

---

Back to [[Example 1 - Creating Simple Documents]]