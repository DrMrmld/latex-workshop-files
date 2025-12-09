## Other Things You Can Do

What I like about $\LaTeX$ the most is that you get to make something more than just an assignment, something more than just an article. As Donald Knuth put it, you go the extra distance to make a paper of the finest quality - a piece of art, really. And in the end, you get to be a little proud of your work and enjoy just how it looks.

I learned $\LaTeX$ about 5 years ago and still sometimes get fascinated by some new features I discover. So here are some bonus things you might find great about $\LaTeX$.

### PGF and TikZ

Check out the [`tikz` package](https://www.ctan.org/pkg/pgf), with which you can make high-quality illustrations in your paper. Here is a somewhat simple example (you'll need the `siunitx` package, too):

```latex
\begin{tikzpicture}[scale = 2.5]
    % axes
    \draw[<->] (3.5, 1.4) -- (4, 1.5) -- (3.9, 2);
    \node at (4, 2) {\scriptsize{$y$}};
    \node at (3.5, 1.3) {\scriptsize{$x$}};

    % the surface
    \draw (0, 0) -- (5, 0) -- (5, 1) -- cycle;

    % the cart
    \draw (1.2, 0.34) circle (0.1);
    \draw (1.7, 0.44) circle (0.1);
    \draw[fill=white] (1, 0.3) -- (1.9, 0.48) -- (1.86, 0.68) -- (0.96, 0.5) -- cycle;
    \draw[->] (1.43, 0.49) -- (1.43, 0.23) node[anchor = west] {$M\vec{g}$};
    \draw[->] (1.88, 0.58) -- (2.13, 0.63) node[anchor = south east] {$\vec{T}$};
    \draw[->] (1.5, 1.1) -- (1.625, 1.125) node[anchor = south east] {$\vec{a}$};

    % the block
    \draw[very thick] (5, 1) -- (5.1, 1.1);
    \draw[fill = black] (5.15, 1.15) circle (0.1);

    % the string
    \draw (1.88, 0.58) -- (5.125, 1.245);
    \draw (5.25, 1.15) -- (5.25, 0.7);

    % the weight
    \draw (5.15, 0.7) rectangle (5.35, 0.4);
    \draw[->] (5.25, 0.55) -- (5.25, 0.3) node[anchor = west] {$m\vec{g}$};
    \draw[->] (5.25, 0.7) -- (5.25, 1) node[anchor = west] {$\vec{T}$};
    \draw[->] (5.5, 0.85) -- (5.5, 0.7225) node[anchor = south west] {$\vec{a}$};

    % the sensor
    \draw[fill=black] (0, 0.208) circle (0.03) node[anchor = east] {$S$};
    \draw[red, dashed, ->] (0, 0.208) -- (0.3, 0.268);

    % angles and dimensions
    \draw (0.5, 0) arc (0:11.31:0.5);
    \node at (0.6, 0.05) {\footnotesize{$\alpha$}};
    \node at (2.5, -0.2) {\small{$92.0\pm0.1~\unit{\cm}$}};
    \node at (4, 0.65) {\small{$93.1\pm0.1~\unit{\cm}$}};
\end{tikzpicture}
```

The output:

![[Pasted image 20251210023022.png]]

It's also vector graphics, the text is accessible, and, you have complete control over the text content of the illustration from $\LaTeX$, which allows you to have a consistent design across your document.

The `pgfplots` package allows you to make plots within $\LaTeX$ and preserve the overall aesthetic of the document[^1]:

![[Pasted image 20251210023910.png]]

![[Pasted image 20251210023959.png]]

### Chess Notation

The `xskak` package allows you to insert a full chessboard into your document with just three lines:

```latex
\newchessgame
\mainline{1.e4 e5 2.Nf3 Nc6 3.Bb5 a6}

\begin{center}
    \chessboard
\end{center}
```

The output:

![[Pasted image 20251210031329.png]]

More on that package on [Overleaf](https://www.overleaf.com/learn/latex/Chess_notation).

### Music Sheets

You can create music sheets using the [`musixtex` package](https://ctan.org/pkg/musixtex).

### Electric Circuits

If you're a physicist or in electrical engineering, you will probably find the `circuitikz` package helpful. Here is a [guide from Overleaf](https://www.overleaf.com/learn/latex/CircuiTikz_package).

### Code

If you need to add some code into your document, I recommend the `minted` package. And here is, as you might have guessed, a [guide from Overleaf](https://www.overleaf.com/learn/latex/Code_Highlighting_with_minted).

You can also find examples of its usage in the README file of the [lab report template](https://github.com/DrMrmld/lab-report-template) I've made some time ago.

## Getting Help

If you are stuck, you can get help

- from AI agents (ChatGPT, Claude, Gemini, etc.),
- on [TeX StackExchange](https://tex.stackexchange.com/) or other communities,
- on [Overleaf Learn](https://www.overleaf.com/learn),
- on [LaTeX-Tutorial.com](https://latex-tutorial.com/), and
- by reading documentations on the [Comprehensive TeX Archive Network](https://ctan.org/).

## Further Readings

If you are interested in learning more, you can check out

- "The Not So Short Introduction to $\LaTeX$" by Tobias Oetiker and other authors
- "$\LaTeX$. A Document Preparation System" by Leslie Lamport
- "$\LaTeX$ Cookbook" by Stefan Kottwitz (also, check out this [website](https://latex-cookbook.net/))

You can also explore the [LaTeX Project](https://latex-project.org/).

[^1]: You can, of course, achieve the same or at least very close results using almost any other software, but you'll find that with $\LaTeX$, you put much less effort and you are guaranteed that the fonts will match with the document's fonts.