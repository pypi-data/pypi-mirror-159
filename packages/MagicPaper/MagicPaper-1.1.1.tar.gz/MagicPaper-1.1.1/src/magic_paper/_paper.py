from dataclasses import dataclass, fields
from typing import TypeAlias, TypeVar

RIGHT = "right"
TOP = "top"
LEFT = "left"
BOTTOM = "bottom"


def _get_source_map(height: int = 3, width: int = 9, filled: bool = False):
    if height < 1 or width < 1:
        raise ValueError()

    return (
        (
            ((RIGHT, TOP), "+"),
            *((((TOP,), "-"),) * width),
            ((TOP, LEFT), "+"),
        ),
        *(
            (
                (
                    ((RIGHT,), "|"),
                    *((((), " " if not filled else "█"),) * width),
                    ((LEFT,), "|"),
                ),
            )
            * height
        ),
        (
            ((RIGHT, BOTTOM), "+"),
            *((((BOTTOM,), "-"),) * width),
            ((BOTTOM, LEFT), "+"),
        ),
    )


_empty_paper_map = (
    (*((((), " "),) * 11),),
    (*((((), " "),) * 11),),
    (*((((), " "),) * 11),),
    (*((((), " "),) * 11),),
    (*((((), " "),) * 11),),
)


T = TypeVar("T")


def _replace_or_append(
    input_lst: list[T], start: int, new_lst: list[T], override: bool = True
) -> None:
    stop = start + len(new_lst)
    slc = input_lst[start:stop]
    len_slc = len(slc)
    for i, item in enumerate(new_lst):
        if i < len_slc:
            if override:
                slc[i] = item
        else:
            slc.append(item)
    input_lst[start:stop] = slc


MaybePaper: TypeAlias = "Paper | None"


@dataclass(slots=True, frozen=True)
class Paper:
    """A paper."""

    right: MaybePaper = None
    """Connected paper to the right side of this one."""

    top: MaybePaper = None
    """Connected paper on the top side of this one."""

    left: MaybePaper = None
    """Connected paper to the left side of this one."""

    bottom: MaybePaper = None
    """Connected paper to the bottom side of this one."""

    height: int = 3
    """The height of paper."""

    width: int = 9
    """The width of the paper."""

    filled: bool = True
    """Indicates if the paper should be filled."""

    bring_back: bool = False
    """If this one should be behind the connected paper."""

    def _iter_style_lines(self, start=0):
        yield from enumerate(
            (
                "".join(t[1] for t in x)
                for x in _get_source_map(self.height, self.width, self.filled)
            ),
            start,
        )

    def get_style(
        self, generated_lines: list[list[str]] | None = None, x=0, y=0
    ) -> list[list[str]]:
        """Returns a list of lines where each one contains a list of chars in that line.

        It contains an style for all sub `Paper`s connected to this one
        """

        if generated_lines is None:
            generated_lines = []

        for i, bottom_line in self._iter_style_lines():
            try:
                line = generated_lines[i + y]
                if len(line) < x:
                    line.extend([" "] * (x - len(line)))

                _replace_or_append(line, x, list(bottom_line), not self.bring_back)
            except IndexError:
                generated_lines.append(([" "] * x) + list(bottom_line))

        if self.left:
            self.left.get_style(generated_lines, x - (self.left.width + 1), y)

        if self.top:
            self.top.get_style(generated_lines, x, y - (self.top.height + 1))

        if self.right:
            self.right.get_style(generated_lines, x + self.width + 1, y)

        if self.bottom:
            self.bottom.get_style(generated_lines, x, y + self.height + 1)

        return generated_lines

    def clone(self, **changes):
        """Returns a clone of this paper with new changes applied"""

        current_fields = fields(self)
        new_values = {}
        for field in current_fields:
            if field.name in changes:
                new_values[field.name] = changes[field.name]
            else:
                new_values[field.name] = getattr(self, field.name)
        return type(self)(**new_values)

    def __str__(self) -> str:
        return "\n".join("".join(line) for line in self.get_style())

    def __rshift__(self, other: "Paper") -> "Paper":
        return self.clone(right=other)

    def __lshift__(self, other: "Paper") -> "Paper":
        return self.clone(left=other)

    def __truediv__(self, other: "Paper") -> "Paper":
        return self.clone(bottom=other)

    def __xor__(self, other: "Paper") -> "Paper":
        return self.clone(top=other)


@dataclass(slots=True, frozen=True)
class EmptyPaper(Paper):
    """An empty paper."""

    bring_back: bool = True

    def _iter_style_lines(self, start=0):
        yield from enumerate(
            ("".join(t[1] for t in x) for x in _empty_paper_map),
            start,
        )


if __name__ == "__main__":
    maze = Paper() >> (
        Paper()
        / (
            Paper()
            >> (
                Paper()
                >> (
                    Paper()
                    >> (
                        Paper()  # <- On top of this <-
                        #                            |
                        ^ (  # ----- Attach everything inside this ( ) ----
                            #                                           |
                            Paper()  # <------------ this -------------  |
                            #                                        |  |
                            << Paper()  # Attach this on the left of --  |
                            #                                             |
                        )  # ---------------------------------------------
                    )
                )
            )
        )
    )

    print(maze)
