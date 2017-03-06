code: true
lang: tex

# Latex

## Pycode

Caveat: Don't end a pycode environment with a comment, it will cause harm.

# Caption package

The caption package has the good intention of improving the appearance of figure captions.
Unfortunately it changes the default style in a non-verbose way,
which makes it dangerous to use in documents with existing formatting rules.
Furthermore the subcaption package does not really tell that it loads the caption package behind the scenes.

## Positioning of pgfplots

Current answer: An axis environment is a special tikz node. It can be
given a name using the option [name=abc] and be referenced as such. It
can be positioned using the options `[at=(...)]` and `[anchor=...]`. It can
NOT be positioned with the positioning library for reasons unknown.

## Images in tikz/pgfplots

It is possible to add images to plots using

```
\node {\includegraphics[width=.5\linewidth]{image}}
```

or

```
\begin{axis}[width=.5\linewidth,
    enlargelimits=false,
    axis lines=none,
    ticks=none,
    scale only axis,
    axis equal image]
    \addplot graphics[xmin=0,ymin=0,xmax=320,ymax=200] {david};
\end{axis}
```

The latter is useful when more plots are added to the image. It is
however painful that the image dimensions have to be specified for each
and every image. The reason behind this is that the image is stretched
to fit into the axis. The key [axis equal image] prevents this, but
xmin,xmax,ymin,ymax still has to be specified manually, determining the
image scaling.
