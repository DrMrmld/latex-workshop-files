# Plan for Example 1

1. Start with the start.tex file
1. Explain what are LaTeX commands
1. Explain the document class
1. Explain preamble
1. Explain environments
1. Hello world

1. Add the title, author, and date
1. The default font size is 10pt; change it to 11pt (introducing optional arguments in commands)
1. Create sections (forget to add procedure)
1. Introduce comments by adding a comment that you will need to include references
1. Add the procedure to show the benefit of automatic numbering

1. Add the introduction using the `lipsum` package
1. Shorten the intro to 2 paragraphs
1. Add the encoding packages
1. Explain the differences between a hyphen, an en-dash, an em-dash, and a minus sign

1. Add chemical glassware to the procedure
1. Make its width equal to linewidth
1. Make its height equal to 9cm
1. Change the angle to 90 or -75
1. Place it inside of a `figure` environment and add a caption
1. Center the figure
1. Add a manual reference to the figure in the procedure section
1. Make it an automatic (built-in) reference to the figure, and add a couple of figures before it to show that it works
1. Add the `hyperref` package and show that the references are now hyperlinks
1. Set `colorlinks` to `true` and `linkcolor` to `blue`
1. Change the `\ref` command to the `\autoref` command

1. Add a list of things to do in the procedure
1. Show how to remove an indentation
1. Make the list unordered

1. Make some parts of the list bold, italic, monospaced
1. Create a hyperlink
1. Show how you can change the font size and style (sffamily, rmfamily)

1. The code is getting busy => transfer the preamble and the sections into separate files
1. Combine the Results section with the Discussion section

1. Add a table of contents
1. Make the introduction contain subsections and subsubsections
1. Show how to change fonts and set the font to TeX Gyre Schola

1. Add a pdf plot to the Results section

1. Add a simple table (only headers)
1. Add a couple of rows
1. Show the syntax *{n}{what}
1. Add vertical bars
1. Add horizontal bars
1. Center, caption, and label
1. Make the header bold
1. Increase the padding (`\arraystretch`)
1. Remove the vertical bars
1. Make the alignment lcr
1. Remove one of the horizontal bars
1. Make the center column 5 cm (`array` package)
1. Add rules from the `booktabs` package
1. Move the caption to the top
1. Add some lipsum

1. Add biblatex with apa style
1. Find and add a reference
1. Try printing the bibliography (should be empty)
1. Add a citation in the conclusion and retry printing the references
1. Show `\cite`, `\parencite`, and `\textcite`
1. Change the style to IEEE
1. Add another reference that would make it pain in the ass working with Word
1. Add the references to the table of contents

1. Add some pictures using the tikz package (you can use your plasmid drawing and physics scheme)
