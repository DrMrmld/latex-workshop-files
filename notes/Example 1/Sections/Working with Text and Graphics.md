## Adding Images

For this part, first download [this image of chemical glassware](https://github.com/DrMrmld/latex-workshop-files/blob/main/example-1-materials/img/glassware.jpg).

Then, open the file tree in Overleaf (the left side panel), and click "New Folder" at the top of the panel to create a new folder. Name the folder "img", it will contain all the images we will be using in this tutorial.

After you've created the "img" folder, we need to add the image into that folder. There are two ways we can do this: either

- open the file tree in Overleaf, click on the "img" folder, click "Upload" at the top of the file tree panel, and find the image file on your computer; or
- just open the folder containing the image on your computer and drag the image file from it into the "img" folder in Overleaf.

If you've done everything correctly, your file tree should look like this:

![[Pasted image 20251208031831.png]]

Now, to add the image into the document, go to your `main.tex` file and add the `graphicx` package in the preamble:

```latex
\usepackage{graphicx}
```

This package will allow us to add the image using the `\includegraphics` command. The command accepts only one required argument - the path to the file. Now, under the Procedure section, add the following line:

```latex
\includegraphics{img/glassware}
```

and compile your document. With the `\includegraphics` command, you don't need to specify the file extension (`.jpg`), and, sometimes, it might even lead to errors.

You will notice that the size of the image is too large. We can fix that by specifying the width of the image using the optional argument of the `\includegraphics` command:

```latex
\includegraphics[width = \textwidth]{img/glassware}
```

The `\textwidth` command contains the horizontal length of the text in your document, so now, if you recompile the document, you will see that the image's width is exactly the width of the text in the Introduction section.

I now realize that the image is too tall, so it's better to control its size by its height. Let's set it to 9 cm:

```latex
\includegraphics[height = 9cm]{img/glassware}
```

I removed the width option, even though it wasn't necessary, because I wanted $\LaTeX$ to preserve the aspect ratio of the image. Here is the result:

![[Pasted image 20251208033033.png]]

> [!info]
> 
> There is still a lot that `\includegraphics` can do. For instance, you can set an `angle` option to be equal to some numeric value - the angle in degrees - and it will rotate the image to that angle. You can explore more by reading the [documentation of the `graphicx` package](https://ctan.org/pkg/graphicx).
> 
> Another thing to note is that with the `graphicx` package, you can insert images in PDF format, which will make the text on the image accessible in the document. You can try that with [this file](https://github.com/DrMrmld/latex-workshop-files/blob/main/example-1-materials/img/plt.pdf).

Currently, $\LaTeX$ sees this image as a giant letter. You can verify that by typing some text after it to see that it will print it to the right of the image. You can also put a paragraph before the image to see that $\LaTeX$ will indent the image just as it indents normal text:

![[Pasted image 20251208033351.png]]

We can, of course, leave it like that, but it would make it a pain working with the placement of the image and its caption, when we add one. To make $\LaTeX$ treat it as an image and take control of beautifully placing it, we should put the `\includegraphics` command into the `figure` environment:

```latex
\begin{figure}
	\includegraphics[height = 9cm]{img/glassware}
\end{figure}
```

We can position the image using an optional argument of the `figure` environment:

```latex
\begin{figure}[ht]
	\includegraphics[height = 9cm]{img/glassware}
\end{figure}
```

The following options can be provided:

- `h` for "here",
- `t` for "top",
- `b` for "bottom",
- `p` to place it on a separate page, and
- any combination of the four.

The combination used above will be interpreted as "place the image *here*, and if you won't be able to, then place it *on top*". I usually put `htbp` in all of my images.

> [!info]
> 
> $\LaTeX$ beginners notice very quickly that putting `h` in the `figure` or similar environments doesn't always put the figure where you wanted it to. This is because $\LaTeX$ evaluates all possible options of placing the figure, assigns them a certain level of "badness", and chooses the one that results in the lowest "badness". If such option isn't the "here" option, it will place the figure somewhere else.
> 
> In such cases, you can put `h!`, where the `!` will mean "important", which will increase the badness levels of other placement options. If that doesn't help, you can import the `float` package and put `H`, which will definitely work.

We can center the figure by adding `\centering` just before the `\includegraphics` command:

```latex
\begin{figure}[htbp]
	\centering
	\includegraphics[height = 9cm]{img/glassware}
\end{figure}
```

> [!info]
> 
> The `\centering` command changes the text alignment in the environment, and, because an image is just a giant letter, it is centered. Whenever you use `\centering`, it will affect all the text that comes after it until the end of the environment. For instance, putting `\centering` right after `\begin{document}` will center all text in your document. Other alignment options are `\raggedleft` and `\raggedright`.
> 
> Even though $\LaTeX$ justifies text by default, there is no command like `\centering` to turn it on after setting some other alignment. There are also some limitations in the built-in alignment options, for instance, with word splitting. You can fix all that by importing the `ragged2e` package and using the commands and environments offered by it.

We can use the `\caption` command to add a caption to the figure, which will always follow the figure, unlike in most word editors:

```latex
\begin{figure}[htbp]
	\centering
	\includegraphics[height = 9cm]{img/glassware}
	\caption{Glassware that won't be used in this experiment.}
\end{figure}
```

Add the following text before the figure to reference it in our lab report:

```latex
Figure 1 shows glassware that is completely unnecessary for our experiment and, hence, won't be used.
```

The result:

![[Pasted image 20251208040056.png]]

The figures are numbered automatically, which means you don't have to worry about manually changing the numbering if you add another figure before it. However, if we reference the figure the way we just did, we **will** have to do a lot of manual and error-prone work if we add a figure before it. To avoid that, we can give the figure a label using the `\label` command and use the it to reference the figure:

```latex
Figure \ref{fig:glassware} shows glassware that is completely unnecessary for our experiment and, hence, won't be used.

\begin{figure}[htbp]
    \centering
    \includegraphics[height = 9cm]{img/glassware}
    \caption{Glassware that won't be used in this experiment.}
    \label{fig:glassware}
\end{figure}
```

The label can be anything you want, but I prefer to put a prefix - `fig:` for figures, `tab:` for tables, `eq:` for equations, and so on - and a short name.

If you recompile your document now, you won't see any changes, but if the number of this figure changes, so will the reference to it, automagically.

## Creating Hyperlinks

When you reference an image, you can make the reference a link, so that the reader can click on the link and go to the figure, table, equation, or something else that you are referencing. To do that, just import the `hyperref` package:

```latex
\usepackage{hyperref}
```

If you recompile your document now and click on the "1" in your reference in the text, you will be sent to the place in the document where that image is. The same happened to your table of contents - now you can go to sections just by clicking on their label in the table of contents.

You can notice, however, that all the links now have red borders, which doesn't look good:

![[Pasted image 20251208041618.png]]

This is done by the `hyperref` package to highlight the links. To fix that, put the following piece of code right after the line where the `hyperref` package is imported:

```latex
\hypersetup{colorlinks=true}
```

This enables using colors to highlight the links. You will see that all your links became red because this is the default color for this type of links. You can change that like so:

```latex
\hypersetup{
    colorlinks=true,
    linkcolor=blue
}
```

> [!info]
> 
> There is a limited number of built-in colors in $\LaTeX$. To get more color options or create custom ones using RGB, HSV, or HEX codes, you can use the [`xcolor` package](https://ctan.org/pkg/xcolor).

You can notice that only the "1" in "Figure 1" became a link, because "Figure" is an ordinary text.

![[Pasted image 20251208042532.png]]

To fix that, you can remove the "Figure" part and use the `\autoref` command offered by the `hyperref` package to make everything a single link. This command works for all objects: tables, sections, equations, etc. You can also create hyperlinks using the `\href` command offered by `hyperref`. The color of the hyperlinks can be changed using the `urlcolor` option.

```latex
% this goes into the preamble of the document:
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=cyan
}

% this goes inside of the 'document' environment:
\autoref{fig:glassware} shows \href{https://www.youtube.com/watch?v=rTgj1HxmUbg}{glassware} that is completely unnecessary for our experiment and, hence, won't be used.
```

This will produce the following output:

![[Pasted image 20251208043728.png]]

The "Figure 1" now points to the first figure, and "glassware" points to a short yet mesmerizing video of an eagle's hunt.

## Text Styles

> [!tip]
> 
> The following part can be a bit overwhelming because of the amount of the information. But remember that you don't have to memorize these commands right away. Just know that you **can** do the things shown here, and if you don't remember how, just come back here and fresh up your memory.
> 
> You can also just skip this section during your first reading.

You can change the typeface to the default sans-serif or monospace typeface using the `\sffamily` and `\ttfamily` commands in the same way as we used the `\centering` command. To reset, you the `\normalfont` command; or set the typeface to serif ("roman") by using `\rmfamily`.

For instance, adding the following piece of code after the inserted image:

```latex
\sffamily
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, vestibulum ut, placerat ac, adipiscing vitae, felis.

\ttfamily
Curabitur dictum gravida mauris.

\normalfont
Nam arcu libero, nonummy eget, consectetuer id, vulputate a, magna. Donec vehicula augue eu neque
```

results in the following output:

![[Pasted image 20251208132650.png]]

You can also use the `\textsf` and `\texttt` commands if you want to make the change only to some small portion of text:

```latex
\sffamily
Lorem ipsum dolor sit amet, \textrm{consectetuer} adipiscing elit. Ut purus elit, vestibulum ut, placerat ac, adipiscing vitae, felis.

\ttfamily
Curabitur \textsf{dictum gravida} mauris.

\normalfont
\texttt{Nam arcu libero}, nonummy eget, consectetuer id, vulputate a, magna. Donec vehicula augue eu neque
```

The result:

![[Pasted image 20251208134304.png]]

The commands `\bfseries` (and `\textbf`) and `\itshape` (and `\textit`) work in the same way and make the text bold and italic, respectively.

You can change the font size using commands like `\large`, `\small`, `\tiny`, and others. The advantage of using such commands is that they scale when you change the base font size, automagically. To reset the font size, use the `\normalsize` command.

The following piece of code:

```latex
\sffamily\large
Lorem ipsum dolor sit amet, \textrm{consectetuer} adipiscing elit. Ut purus elit, vestibulum ut, placerat ac, adipiscing vitae, felis.

\ttfamily\small
Curabitur \textsf{dictum gravida} mauris.

\normalfont\normalsize
\texttt{Nam arcu libero}, nonummy eget, consectetuer id, vulputate a, magna. Donec vehicula augue eu neque

\bfseries
Nam dui ligula, fringilla a, euismod sodales, sollicitudin vel, wisi.

\itshape
Morbi auctor lorem non justo.

\normalfont
Nam lacus libero, pretium at, lobortis vitae, ultricies et, tellus.
```

yields the following output:

![[Pasted image 20251208135423.png]]

As you can notice, the effects of `\bfseries` and `\itshape` added up until we reset them using `\normalfont`.

You can use the `\footnote` command to add a footnote:

```latex
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
```

As you can notice, the `hyperref` package made these hyperlinks, too:

![[Pasted image 20251208140724.png]]

> [!info]
> 
> You can find more font styles and sizes on [Overleaf Learn](https://www.overleaf.com/learn/latex/Font_sizes%2C_families%2C_and_styles).

Finally, $\LaTeX$ gives you an ability to put a hyphen (`-`), an en-dash (`--`), an em-dash (`---`), or a minus sign (`$-$`), which are all different symbols, without leaving your editor, which is not offered in most word editors.

## Lists

As this is the methodology section of the lab report, you might want to list the steps of the procedure or the materials used using lists. Let's recreate the following two lists:

> [!example]
> 
> To make a great cup of loose-leaf tea:
> 
> 1. Prepare everything
> 	1. Warm your teapot by rinsing with hot water
> 	2. Measure water for one cup and pick your tea
> 2. Brew the tea
> 	1. Measure and add leaves
> 	2. Pour and steep
> 3. Serve and adjust
> 
> What you will need:
> 
> - Loose-leaf tea
> - Teapot, mug, or infuser
> - Kettle (for heating water)
> - Fresh water

To create an ordered list, use the `enumerate` environment:

```latex
To make a great cup of loose-leaf tea:

\begin{enumerate}
	\item Prepare everything
	\item Brew the tea
	\item Serve and adjust
\end{enumerate}
```

To break down each step, simply nest another `enumerate` environment inside:

```latex
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
```

To make an unordered list, use the `itemize` environment:

```latex
What you will need:

\begin{itemize}
	\item Loose-leaf tea
	\item Teapot, mug, or infuser
	\item Kettle (for heating water)
	\item Fresh water
\end{itemize}
```

Here is the result:

![[Pasted image 20251208142923.png]]

![[Pasted image 20251208142947.png]]

Personally, I don't like how the text before the lists is indented because it looks like part of the list that way. Whenever you want to remove an indentation, start the line with `\noindent`:

```latex
\noindent What you will need:
```

Or, because adjacent lines are interpreted as a single paragraph, you can also write

```latex
\noindent
What you will need:
```

The result:

![[Pasted image 20251208143647.png]]

---

Back to [[Example 1 - Creating Simple Documents]]