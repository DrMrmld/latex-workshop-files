## Code Structure

A $\LaTeX$ code consists of plain text and commands. To the first approximation, commands can be viewed as functions in ordinary programming.

The first command we will look at is the `\documentclass` command. It accepts one (required) argument - the name of the document class. Because we will be writing a lab report in this tutorial, I find it most appropriate to use the built-in `article` document class. At this point, your `main.tex` file should be absolutely empty. Add the first line to it:

```latex
\documentclass{article}
```

By setting the class of the document to `article`, we can now use certain commands specific to that class. We'll see these commands during the course of this tutorial.

## Environments in $\LaTeX$

In $\LaTeX$, there are different environments for different purposes. Different environments are have unique styles and can behave uniquely. For instance, when writing an article, one would put the abstract inside the `abstract` environment, a quote - inside the `quote` environment, and so on.

The first environment we will see is the `document` environment. This environment is a required environment for any document. Your code won't compile without it. To signify the beginning and the end of any environment, the `\begin` and `\end` commands are used in $\LaTeX$.

You can now write "Hello World" inside of the `document` environment, and press Recompile (`Ctrl`+`Enter`) to see the results. At this point, your `main.tex` file should look like this:

```latex
\documentclass{article}

\begin{document}

Hello World

\end{document}
```

You can also see that there is a "1" at the bottom of the page. This is because the pages of the `article` document class are automatically numbered by default.

![[Pasted image 20251129202404.png]]

---

Back to [[Example 1 - Creating Simple Documents]]