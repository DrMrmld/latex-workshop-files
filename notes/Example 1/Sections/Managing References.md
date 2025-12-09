Using labels in referencing figures, equations, etc. instead of manually inputting their number saves you a great deal of time. However, you feel the most benefit from that approach when using references and adding citations in your text. As we will see in a bit, it makes it almost effortless to add new references and even change the reference styles completely.

## References File

First, we will need to create a new file named `references.bib` in the root directory of our project. Here is an example of how the entries in that file could look:

```bibtex
@book{crchandbook,
    title = {CRC Handbook of Chemistry and Physics},
    editor = {Haynes, William M},
    edition = {95},
    year = {2014},
    publisher = {CRC Press},
    address = {Boca Raton, FL},
    chapter = {15},
}

@article{fenby1973,
  title={Excess enthalpies of dimethyl sulphoxide with chloroform, carbon tetrachloride, and benzene},
  author={Fenby, DV and Billing, GJ and Smythe, DB},
  journal={The Journal of Chemical Thermodynamics},
  volume={5},
  number={1},
  pages={49--56},
  year={1973},
  publisher={Elsevier}
}

@online{nist:propanol,
    author = {{National Institute of Standards and Technology}},
    title = {1-Propanol},
    url = {https://webbook.nist.gov/cgi/cbook.cgi?ID=71-23-8},
    urldate = {2025-09-17},
    year = {2025}
}
```

Every entry starts with `@type` which lets the bibliography engine[^1] know which styles to use for that reference. The first property is always the label that we will use to cite the reference. In this case, the labels are `crchandbook`, `fenby1973`, and `nist:propanol`. After that, the entry contains all the information needed to print the reference in the form of key-value pairs.

I understand that it might look tedious, but I will show you a trick which will, in most cases, allow you to avoid writing all of this by hand.

Suppose we want to cite [this article](https://pubs.aip.org/aapt/pte/article-abstract/57/7/454/1016319/Entropy-as-Disorder-History-of-a-Misconception) about the misconception that entropy is the same as disorder. We open up [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Entropy%20as%20Disorder%3A%20History%20of%20a%20Misconception) and find that article there. Most of the time, you will find the article. In that case, click the "Cite" button at the bottom of its entry in the search results:

![[Pasted image 20251210011125.png]]

Then, at the bottom of the pop-up, click "BibTeX", and a new page will be opened, containing the `bibtex` entry that we can just copy and paste into our `references.bib` file:

```bibtex
@article{styer2019entropy,
  title={Entropy as disorder: History of a misconception},
  author={Styer, Dan},
  journal={The Physics Teacher},
  volume={57},
  number={7},
  pages={454--458},
  year={2019},
  publisher={AIP Publishing}
}
```

If you like, of course, you can change the label.

## Adding Citations

You might have noticed that I didn't start the labels of these references with the `ref:` prefix as I did with figures, for instance. This is because the labels of the references are separate from the labels of the figures, tables, etc. They are processed by a separate program, which in our case is [`biber`](https://en.wikipedia.org/wiki/Biber_(LaTeX)).

Once you've created the `references.bib` (note the extension) file in the root directory of your project and added the four entries above into that file, you can import the `biblatex` package as follows (in the preamble of your document):

```latex
% preamble.tex
\usepackage[backend=biber, style=apa]{biblatex}
\addbibresource{references.bib}
```

The second line tells where to get the references data.

Now, go to the end of your `main.tex` file and add the following line:

```latex
\printbibliography
```

If you compile your document now, you won't see any changes. This is because it prints only the references that are cited in the document. So, go to your `conclusion.tex` file and add a citation, like so:

```latex
% conclusion.tex
Here is a citation (\cite{styer2019entropy}).
```

Here is the result:

![[Pasted image 20251210012849.png]]

Note that the `hyperref` package made that a hyperlink, which is why it is green. You can change the color by setting the `citecolor` option in the `\hypersetup` command in your preamble:

```latex
% preamble.tex
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=cyan,
    citecolor=blue
}
```

However, I wouldn't recommend using the `\cite` command. Instead, I use the `\textcite` and `\parencite` commands. As the names suggest, the former is for in-text citations, and the latter is for end-of-sentence citations:

```latex
Here is an end-of-sentence citation \parencite{styer2019entropy}. \textcite{fenby1973} found that \dots
```

Here is the result:

![[Pasted image 20251210013624.png]]

Now, suppose that, for some reason, you need to change the citation style to IEEE. Because you are using $\LaTeX$, you can just change the bibliography style to `ieee`:

```latex
% preamble.tex
\usepackage[backend=biber, style=ieee]{biblatex}
```

And here you go:

![[Pasted image 20251210013940.png]]

You can also notice that the parentheses in the first citation are gone. This is why I prefer to use `\parencite` instead of manually putting parentheses and using `\cite`.

Also, if you add another citation before the first one, normally, you would have to update all citations and references because the numbering would have changed. With $\LaTeX$, everything is updated for you, and you don't have to install and configure a separate software:

```latex
Here is a reference that would cause a lot of pain if I wasn't using \LaTeX\ \parencite{crchandbook}.

Here is an end-of-sentence citation \parencite{styer2019entropy}. \textcite{fenby1973} found that \dots
```

The result:

![[Pasted image 20251210014532.png]]

## More Options

Just a couple of details. If you look at the table of contents, you won't see the References section:

![[Pasted image 20251210015013.png]]

To add it, go to your `main.tex` file and add the following option to the `\printbibliography` command:

```latex
\printbibliography[heading=bibintoc]
```

Now, the references are there, and you can click on the label to go to them:

![[Pasted image 20251210015120.png]]

There are other options of that command, and you can find them in the [`biblatex` package documentation](https://ctan.org/pkg/biblatex).

---

Back to [[Example 1 - Creating Simple Documents]]