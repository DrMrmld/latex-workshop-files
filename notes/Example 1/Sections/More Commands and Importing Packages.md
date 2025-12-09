## Adding Sections and Subsections

Let's explore other commands. We can create sections using the `\section` command. We can also create `\subsection`s and `\subsubsection`s, as we will see later.

First, add a section title before the "Hello World" line.

```latex
\section{Introduction}

Hello World
```

If you compile the document now, you'll see that a section title was added with its number. Also, the appropriate styles were applied to that title automatically, so we didn't have to worry about making the title bold and setting a larger font size.

Let's add several other sections that we will develop later:

```latex
\section{Introduction}

Hello World

\section{Results}

\section{Discussion}

\section{Conclusion}
```

Now, I'll demonstrate how helpful the automatic numbering of the sections is. If you compiled your document, you should see 4 section titles. However, we forgot to include the "Procedure" section (or "Methods" in some cases) right before the "Results" section. If we were using an editor that doesn't automatically number the sections, we would have to manually edit the numbers of the three sections that follow the "Procedure" section. But in this case, we can just add `\section{Procedure}` where we want, and the numbering will be done for us.

Your `main.tex` file should now look like this:

```latex
\documentclass{article}

\begin{document}

\section{Introduction}

Hello World

\section{Procedure}

\section{Results}

\section{Discussion}

\section{Conclusion}

\end{document}
```

You can also remove the numbering by using the `\section*` command instead of the `\section` command. I will leave it as it is.

## Optional Arguments of the Commands

Up until now, we've seen commands that require only one argument to be passed. However, there are also optional argument to most commands in $\LaTeX$. For instance, the `\documentclass` command accepts one optional command, which is the list of so-called options that we want to use with a given document class.

We've seen that $\LaTeX$ applies different styles (font size, in particular) automatically. However, these sizes aren't completely fixed - they are derived from the "normal" font size (the size of the body text) which is 10pt by default.

10pt seems too small for me, and I want to make it 11pt. For that, I pass the option `11pt` to the `\documentclass` command as follows:

```latex
\documentclass[11pt]{article}
```

If you compile the document now, you'll see that the text got slightly bigger.

Also, in $\LaTeX$, the paper's size is letter by default. We can change it to A4 by passing the `a4paper` option:

```latex
\documentclass[11pt, a4paper]{article}
```

The paper's size and layout in general is better manipulated using the [`geometry` package](https://ctan.org/pkg/geometry), but we won't be covering it for now.

## Making the Title

To make the title, we can use the built-in `\maketitle` command in $\LaTeX$. But first, we need to add the title info using the following three commands, which are self-explanatory:

```latex
\title{Lab Report 1. Learning to Make Documents with \LaTeX}
\author{John Doe}
\date{November 19, 2025}
```

Note that these commands must be used in the preamble of the document. The preamble is everything before the start of the `document` environment.

```latex
\documentclass[11pt, a4paper]{article}

\title{Lab Report 1. Learning to Make Documents with \LaTeX}
\author{John Doe}
\date{November 19, 2025}

\begin{document}
...
```

Now, in the `document` environment, before the `\section{Introduction}` line, add the following line:

```latex
\maketitle
```

If you've done everything correctly, you should see a nicely formatted title before the Introduction section of our lab report:

![[Pasted image 20251208030157.png]]

If you want the title to be a separate page, add the `titlepage` option to the `\documentclass` command like so:

```latex
\documentclass[a4paper, 11pt, titlepage]{article}
```

But I won't be using it in this tutorial.

## Adding the Table of Contents

You can also add the table of contents with just one line of code:

```latex
\tableofcontents
```

Put it right after the `\maketitle` command, and you will get the following output:

![[Pasted image 20251208030250.png]]

It looks boring at the moment, but it will get better in the course of this tutorial.

## Adding Dummy Text into Our Document

It is hard to judge the looks of a document when it only has about 10 words in it. Let's add some text to make it easier for us.

For that, we will import our first package - `lipsum`. In the preamble of your `main.tex` file, add the following line:

```latex
\usepackage{lipsum}
```

The `\usepackage` command allows us to import packages created by other people and enhance the functionality of $\LaTeX$ in that way.

The main command offered by this package is `\lipsum`. Remove the "Hello World" line and put `\lipsum` in its place.

```latex
\lipsum
```

After compiling your document, you'll see that a lot of text has been added. You can see that the text starts with "lorem ipsum", which is why the package is called that way.

But the 7 paragraphs that the `\lipsum` command adds by default is too many for me, so I will make it less by using its optional argument, in which I can specify the range of the paragraphs to print in my document.

```latex
\lipsum[1-5]
```

In fact, I will use the `\subsection` command to split the introduction into two subsections as follows:

```latex
...

\section{Introduction}

\subsection{First Subsection}

\lipsum[1-2]

\subsection{Second Subsection}

\lipsum[3-5]

...
```

You can also notice that the table of contents has been automatically updated to include the added subsections.

## Importing Other Packages

You might be wondering where do we learn about different packages, what commands they offer, and what options can we use them with. The answer is - anywhere on the internet, because these packages are made by people and people publish them for others to use.

However, there is a huge archive that contains information about practically every $\LaTeX$ package, called the [Comprehensive TeX Archive Network](https://ctan.org/). On CTAN, you can browse packages or find the documentation of the package you are trying to use. For instance, here is the page of the [`lipsum` package](https://ctan.org/pkg/lipsum).

## Changing the Typeface

To make our document look even better, I want to change the typeface (font family) from the default Computer Modern to something else. But before that, I want to make a quick note about the following two packages:

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
```

In short, just use them in all your documents because they will make sure that the input and the output is interpreted and printed correctly. I usually add them right after the `\documentclass` command.

Now, to set a certain typeface, we can just add the package corresponding to the typeface that we want to use. For that, we can go to the [LaTeX Font Catalogue](https://tug.org/FontCatalogue/) and choose any font we like. For this tutorial, I recommend [TeX Gyre Schola](https://tug.org/FontCatalogue/texgyreschola/).

Under the "Usage" heading on that page, you will see the piece of code that you can just copy and paste into your preamble:

```latex
\usepackage{tgschola}
\usepackage[T1]{fontenc}
```

As you could have noticed, the second line is already added, so we only need to add the first line. Recompile your document to see the new typeface applied:

![[Pasted image 20251208030449.png]]

> [!info]
> 
> We are currently using the `pdfLaTeX` engine to compile our document, as you can see from the Compiler Settings in Overleaf. As far as I know, the method of changing the font family we just learned is the only way you can change the typeface when using `pdfLaTeX`. But with the [`XeLaTeX` engine](https://en.wikipedia.org/wiki/XeTeX), you can use TrueType and OpenType fonts.

---

At this point, your `main.tex` file should look like this:

```latex
\documentclass[a4paper, 11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{tgschola}

\usepackage{lipsum}

\title{Lab Report 1. Learning to Make Documents with \LaTeX}
\author{John Doe}
\date{November 19, 2025}


\begin{document}

\maketitle

\tableofcontents

\section{Introduction}

\subsection{First Subsection}

\lipsum[1-2]

\subsection{Second Subsection}

\lipsum[3-5]

\section{Results}

\section{Discussion}

\section{Conclusion}

\end{document}
```

Back to [[Example 1 - Creating Simple Documents]]