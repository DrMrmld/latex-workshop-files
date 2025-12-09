At this point of the tutorial, your `main.tex` file probably has around 100 lines in it. Mine has exactly 100. This is not a lot. However, you might work on larger projects or collaborate with other people later on, and you will find the tips from this part helpful. Also, applying them to smaller projects still makes your life easier.

We will be working with the file tree a lot, so go ahead and open it right now.

## Preamble

Our preamble currently takes up about 20% of the available space, so let's move it into a separate file. At the top of your file tree, click "New file" and create a file named `preamble.tex`:

![[Pasted image 20251209015225.png]]

Make sure that the "img" folder isn't selected when you do that. If it is, the new file will be created in that folder. But you can fix that easily by simply dragging the file into the space near the `main.tex` file.

Now, go to the `main.tex` file and remove all the preamble and paste it into the newly created `preamble.tex` file:

```latex
% preamble.tex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{tgschola}

\usepackage{lipsum}
\usepackage{graphicx}

\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=cyan
}
```

The point of moving the preamble is to remove the parts of the document you rarely use, which will make it easier to navigate in your code. After importing the packages you need, most of the time, you don't even look at that part of the file. This is also the reason why I prefer not to put the title data into a separate file - I like when it is more accessible in case I need to make a little change.

You'll notice that compiling the document now returns a lot of errors. This is because Overleaf reads and compiles only the `main.tex` file. To include the content of the `preamble.tex` file, we can use the `\input` command like so:

```latex
\documentclass[a4paper, 11pt]{article}
\input{preamble}

\title{Lab Report 1. Learning to Make Documents with \LaTeX}
\author{John Doe}
\date{November 19, 2025}


\begin{document}
...
```

As with the `\includegraphics` command, we don't need to specify the extension of the file.

Now, recompiling yields the document we had before.

## Moving Sections into Separate Files

Just as with the preamble, we can move the sections' content into separate files. Create a folder named "sections" in the main directory of your project. We'll now combine the Results section with the Discussion section, so create the following files inside of that folder:
`introduction.tex`, `procedure.tex`, `results-and-discussion.tex`, and `conclusion.tex`.

If you did everything correctly, your project's file tree should look like this:

![[Pasted image 20251209020519.png]]

I'll transfer the corresponding parts of the `main.tex` file to the newly created ones:

```latex
% introduction.tex

\section{Introduction}

\subsection{First Subsection}

\lipsum[1-2]

\subsection{Second Subsection}

\lipsum[3-5]
```

```latex
% procedure.tex

\section{Procedure}

\autoref{fig:glassware} shows \href{https://www.youtube.com/watch?v=rTgj1HxmUbg}{glassware} that is completely unnecessary for our experiment and, hence, won't be used.

\begin{figure}[htbp]
    \centering
    \includegraphics[height = 9cm]{img/glassware}
    \caption{Glassware that won't be used in this experiment.}
    \label{fig:glassware}
\end{figure}

\sffamily\large
Lorem ipsum dolor sit amet, \textrm{consectetuer} adipiscing elit. Ut purus elit, vestibulum ut, placerat ac, adipiscing vitae, felis.

\ttfamily\small
Curabitur \textsf{dictum gravida} mauris.

\normalfont\normalsize
\texttt{Nam arcu libero}, nonummy eget, consectetuer\footnote{According to the DuckDuckGo AI Assist, this word translates to `to pursue' or `to follow' from Latin.} id, vulputate a, magna. Donec vehicula augue eu neque

\bfseries
Nam dui ligula, fringilla a, euismod sodales, sollicitudin vel, wisi.

\itshape
Morbi auctor lorem non justo.

\normalfont
Nam lacus libero, pretium at\footnote{The quick brown fox jumps over the sleazy dog.}, lobortis vitae, ultricies et, tellus.

To make a great cup of loose-leaf tea:

\begin{enumerate}
	\item Prepare everything
		\begin{enumerate}
			\item Warm your teapot by rinsing with hot water
			\item Measure water for one cup and pick your tea
		\end{enumerate}
		
	\item Brew the tea
		\begin{enumerate}
			\item Measure and add leaves
			\item Pour and steep
		\end{enumerate}
		
	\item Serve and adjust
\end{enumerate}

\noindent
What you will need:

\begin{itemize}
	\item Loose-leaf tea
	\item Teapot, mug, or infuser
	\item Kettle (for heating water)
	\item Fresh water
\end{itemize}
```

```latex
% results-and-discussion.tex

\section{Results and Discussion}
```

```latex
% conclusion.tex

\section{Conclusion}
```

And now the `main.tex` file looks like this:

```latex
\documentclass[a4paper, 11pt]{article}
\input{preamble}

\title{Lab Report 1. Learning to Make Documents with \LaTeX}
\author{John Doe}
\date{November 19, 2025}


\begin{document}

\maketitle

\tableofcontents

\input{sections/introduction}
\input{sections/procedure}
\input{sections/results-and-discussion}
\input{sections/conclusion}

\end{document}
```

If you want any section to appear on a separate page, use the `\include` command instead. At any point in the file, if you want to create a page break, you can use either `\clearpage` or `\newpage`, whichever is best suited in your case.

Now, your project is much easier to navigate. If you want to import any package, you can do that in the `preamble.tex` file. If you want to update any of the sections, you can quickly find the file and the place you are looking for. And, most importantly, if you decide to collaborate with someone, that person will find it quite easy to navigate in the unknown project.

---

Back to [[Example 1 - Creating Simple Documents]]