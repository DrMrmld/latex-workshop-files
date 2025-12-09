## Basic Tables

Let's go to the Results and Discussion section (`results-and-discussion.tex` file), which currently contain only the following lines:

```latex
\section{Results and Discussion}

\lipsum[9]
```

Let's add a simple table that looks something like this:

| **Header 1** | **Header 2** | **Header 3** |
| ------------ | ------------ | ------------ |
| Item 1       | Item 2       | Item 3       |
| Item 4       | Item 5       | Item 6       |

We can do that by using the `tabular` environment of $\LaTeX$:

```latex
\begin{tabular}{lll}
	\textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
	Item 1 & Item 2 & Item 3 \\
	Item 4 & Item 5 & Item 6
\end{tabular}
```

The required argument of the `tabular` environment contains the alignments of each column. `l` stands for "left", `r` - for "right", and `c` for "center". The `&` symbols signify the end of cells, and the `\\` command signifies the end of line.

Here is the output:

![[Pasted image 20251209150436.png]]

The table currently looks a bit odd because, just as with figures, $\LaTeX$ interprets this table as a giant letter. And there are also no lines separating the cells as one would expect.

Just as with figures, there is the `table` environment that will allow $\LaTeX$ to take control of positioning the table and allow us to add captions and labels:

```latex
\begin{table}[htbp]
	\begin{tabular}{lcr}
		\textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
		Item 1 & Item 2 & Item 3 \\
		Item 4 & Item 5 & Item 6
	\end{tabular}
	\caption{Example table.}
	\label{tab:example}
\end{table}

\autoref{tab:example} is an example table.
```

Here is the result:

![[Pasted image 20251209151317.png]]

You can add vertical separators using the `|` symbol in the argument of the `tabular` environment and the `\hline` command between the table rows. Also, if there are many columns with the same alignment, you can use the `*{number}{alignment}` notation.

```latex
\begin{table}[htbp]
    \centering
	\begin{tabular}{|l|c|r|}
    \hline
		\textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
    \hline
		Item 1 & Item 2 & Item 3 \\
    \hline
		Item 4 & Item 5 & Item 6 \\
    % note that you need to add the endline here
    % if you want the horizontal separator
    \hline
	\end{tabular}
	\caption{Example table.}
    \label{tab:example}
\end{table}

\noindent
\autoref{tab:example} is an example table. And \autoref{tab:long} is a longer table.

\begin{table}[htbp]
    \small\centering
	\begin{tabular}{l*{5}{|l}}
		\textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3}  & \textbf{Header 4} & \textbf{Header 5}  & \textbf{Header 6} \\
    \hline
		Item 1 & Item 2 & Item 3 & Item 4 & Item 5 & Item 6 \\
    \hline
		Item 8 & Item 9 & Item 10 & Item 11 & Item 12 & Item 13 \\
	\end{tabular}
	\caption{Longer table.}
	\label{tab:long}
\end{table}
```

Here is the result:

![[Pasted image 20251209152031.png]]

You can also notice that the padding in the cells is very small. To change that, you can go to the `preamble.tex` file to change your preamble and insert the following line:

```latex
\renewcommand{\arraystretch}{1}
```

This command scales the cells of the table by the indicated amount. Recompiling the document now won't make any changes. But you can play with that number and find what scaling factor you like best. For me, it is 1.3, so I'll put that. Here is the result:

![[Pasted image 20251209152511.png]]

## Prettier Tables

You can use the `p` alignment option to set a specific width to a cell:

```latex
\begin{table}[htbp]
    \centering
	\begin{tabular}{|p{5cm}|c|r|}
    \hline
		\textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
    \hline
		Item 1 & Item 2 & Item 3 \\
    \hline
		Item 4 & Item 5 & Item 6 \\
    \hline
	\end{tabular}
	\caption{Example table.}
    \label{tab:example}
\end{table}
```

Here is the result:

![[Pasted image 20251209153038.png]]

However, some might find it now convenient to change the alignment to centered or left, so you can import the `array` package that extends the table functionality in $\LaTeX$. Now, you can use the `w` alignment option to set a specific alignment (`l`, `c`, `r`) **and** the width:

```latex
\begin{table}[htbp]
    \centering
	\begin{tabular}{|l|w{c}{5cm}|r|}
    \hline
		\textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
    \hline
		Item 1 & Item 2 & Item 3 \\
    \hline
		Item 4 & Item 5 & Item 6 \\
    \hline
	\end{tabular}
	\caption{Example table.}
    \label{tab:example}
\end{table}
```

Here is the result:

![[Pasted image 20251209153323.png]]

> [!info]
> 
> You can also check out the `tabularx` package if you want to control the overall width of your table and not just the widths of specific columns.
> 
> You can also check out this [guide on Overleaf Learn](https://www.overleaf.com/learn/latex/Tables) to learn other features you might need in the future.

To make the table prettier, we can also import the `booktabs` package that will allow us to use the `\toprule`, `\midrule`, and `\bottomrule` commands instead of the plain `\hline` one:

```latex
\begin{table}[htbp]
    \centering
	\begin{tabular}{lw{c}{5cm}r}
		\toprule
			\textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
		\midrule
			Item 1 & Item 2 & Item 3 \\
			Item 4 & Item 5 & Item 6 \\
		\bottomrule
	\end{tabular}
	\caption{Example table.}
    \label{tab:example}
\end{table}
```

Here is the result:

![[Pasted image 20251209153930.png]]

You can also put the caption before the `tabular` environment if you need the caption to be above the table.

Here is an example of a table from one of my lab reports:

![[Pasted image 20251209154314.png]]

---

Back to [[Example 1 - Creating Simple Documents]]