# MagicPaper

A magical extendable paper to have fun with ...

_Just like someone who said: it's not much, but it's honest work :) ._

## What's this?

It's just papers in terminal! You can create combinations of them that leads to
something interesting ...

## Let's try

It's just simple (as it is)

```py
from magic_paper import Paper

paper = Paper()
print(paper)
```

``` cmd
+---------+
|█████████|
|█████████|
|█████████|
+---------+
```

Now combine them ...

``` py
paper = Paper(right=Paper(bottom=Paper(right=Paper())))
print(paper)
```

``` cmd
+---------+---------+
|█████████|█████████|
|█████████|█████████|
|█████████|█████████|
+---------+---------+---------+
          |█████████|█████████|
          |█████████|█████████|
          |█████████|█████████|
          +---------+---------+
```

You can change sizes

```py
vertical_paper = Paper(width=3)
print(vertical_paper)

horizontal_paper = Paper(height=1)
print(horizontal_paper)

combined = Paper(width=3, bottom=Paper(height=1))
print(combined)
```

``` cmd
+---+
|███|
|███|
|███|
+---+
```

``` cmd
+---------+
|█████████|
+---------+
```

``` cmd
+---+
|███|
|███|
|███|
+---------+
|█████████|
+---------+
```

You can use `EmptyPaper` for gaps.

``` py
from magic_paper import EmptyPaper, Paper

combined = Paper(
    height=1,
    bottom=Paper(
        width=3,
        bottom=EmptyPaper(
            bottom=Paper(
                width=3,
                bottom=Paper(
                    height=1,
                    right=EmptyPaper(height=1, right=Paper(height=1), bring_back=True),
                ),
            ),
            bring_back=True,
        ),
    ),
    right=EmptyPaper(
        height=1,
        right=Paper(
            height=1,
            bottom=EmptyPaper(
                width=5,
                right=Paper(
                    width=3,
                    bottom=EmptyPaper(
                        bring_back=True,
                        bottom=Paper(
                            width=3,
                        ),
                    ),
                ),
                bring_back=True,
            ),
        ),
        bring_back=True,
    ),
)

print(combined)
```

``` cmd
+---------+         +---------+
|█████████|         |█████████|
+---+-----+         +-----+---+
|███|                     |███|
|███|                     |███|
|███|                     |███|
+---+                     +---+      



+---+                     +---+      
|███|                     |███|
|███|                     |███|
|███|                     |███|
+---------+         +---------+
|█████████|         |█████████|
+---------+         +---------+
```

Use `>>`, `<<`, `/`, `^` to create new combination of papers.

``` py
maze = (
    Paper()
    >> (
        Paper()
        / ( # Guess what this dose ...
            Paper()
            >> (
                Paper()
                >> (
                    Paper()
                    >> (
                        Paper() # <- On top of this <-
                        #                            |
                        ^ ( #----- Attach everything inside this ( ) ----
                            #                                           |
                            Paper() # <------------ this -------------  |
                            #                                        |  |
                            << Paper() # Attach this on the left of --  |
                            #                                           |
                        ) # ---------------------------------------------
                    )
                )
            )
        )
    )
)

print(maze)
```

How it's going to looks like:

``` cmd
                              ------>-------->-------
+---------+---------+         +---------+---------+ |
|█████████|█████████|         |█████████|█████████| |
|█████████|█████████|         |█████████|█████████| v
|█████████|█████████|         |█████████|█████████| |
+---------+---------+---------+---------+---------+ |
--<------ |█████████|█████████|█████████|█████████| |
        ^ |█████████|█████████|█████████|█████████| |
        | |█████████|█████████|█████████|█████████| v
        | +---------+---------+---------+---------+ |
        --------<---------<--------<---------<-------
```

Now it's time for you to imagine ...

```py
zero_six_seven = Paper(
    right=Paper(
        right=Paper(
            right=EmptyPaper(
                right=Paper(
                    right=Paper(
                        right=Paper(
                            right=EmptyPaper(
                                right=Paper(
                                    right=Paper(
                                        right=Paper(
                                            bottom=Paper(
                                                bottom=Paper(
                                                    bottom=Paper(bottom=Paper())
                                                )
                                            )
                                        )
                                    )
                                ),
                                bring_back=True,
                            ),
                            bottom=Paper(
                                bottom=Paper(
                                    bottom=Paper(
                                        bottom=Paper(
                                            left=Paper(
                                                left=Paper(
                                                    top=Paper(
                                                        top=Paper(right=Paper())
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            ),
                        )
                    )
                ),
                bring_back=True,
            ),
            bottom=Paper(
                bottom=Paper(
                    bottom=Paper(
                        bottom=Paper(
                            left=Paper(
                                left=Paper(top=Paper(top=Paper(top=Paper())))
                            )
                        )
                    )
                )
            ),
        )
    )
)
print(zero_six_seven)
```

_You will need an screen with higher width, if shape below looks wired!_

``` cmd
+---------+---------+---------+         +---------+---------+---------+         +---------+---------+---------+
|█████████|█████████|█████████|         |█████████|█████████|█████████|         |█████████|█████████|█████████|
|█████████|█████████|█████████|         |█████████|█████████|█████████|         |█████████|█████████|█████████|
|█████████|█████████|█████████|         |█████████|█████████|█████████|         |█████████|█████████|█████████|
+---------+---------+---------+         +---------+---------+---------+         +---------+---------+---------+
|█████████|         |█████████|                             |█████████|                             |█████████|
|█████████|         |█████████|                             |█████████|                             |█████████|
|█████████|         |█████████|                             |█████████|                             |█████████|
+---------+         +---------+         +---------+---------+---------+                             +---------+
|█████████|         |█████████|         |█████████|█████████|█████████|                             |█████████|
|█████████|         |█████████|         |█████████|█████████|█████████|                             |█████████|
|█████████|         |█████████|         |█████████|█████████|█████████|                             |█████████|
+---------+         +---------+         +---------+---------+---------+                             +---------+
|█████████|         |█████████|         |█████████|         |█████████|                             |█████████|
|█████████|         |█████████|         |█████████|         |█████████|                             |█████████|
|█████████|         |█████████|         |█████████|         |█████████|                             |█████████|
+---------+---------+---------+         +---------+---------+---------+                             +---------+
|█████████|█████████|█████████|         |█████████|█████████|█████████|                             |█████████|
|█████████|█████████|█████████|         |█████████|█████████|█████████|                             |█████████|
|█████████|█████████|█████████|         |█████████|█████████|█████████|                             |█████████|
+---------+---------+---------+         +---------+---------+---------+                             +---------+
```
