"""Create editable geometric SVG starting points; parameters are not observations.

Ring output is an equal-part schematic, never a chart of measured percentages.
Only use a motif when the reference contains it and target semantics support it.
"""

import argparse
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET


NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def element(parent, name, **attrs):
    return ET.SubElement(parent, f"{{{NS}}}{name}", {k: str(v) for k, v in attrs.items()})


def number(value):
    return f"{value:.6f}".rstrip("0").rstrip(".") or "0"


def color(value):
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise argparse.ArgumentTypeError("Use a six-digit hex color such as #315C7D")
    return value


def finite(value):
    result = float(value)
    if not math.isfinite(result):
        raise argparse.ArgumentTypeError("Geometry values must be finite")
    return result


def document(width, height, title, description):
    root = ET.Element(f"{{{NS}}}svg", {
        "viewBox": f"0 0 {number(width)} {number(height)}",
        "width": number(width), "height": number(height),
        "role": "img", "aria-labelledby": "motif-title motif-description",
    })
    element(root, "title", id="motif-title").text = title
    element(root, "desc", id="motif-description").text = description
    return root


def make_ring(args):
    if args.segments < 2:
        raise ValueError("A segmented ring requires at least two segments")
    if not 0 < args.inner < args.outer:
        raise ValueError("Require 0 < inner radius < outer radius")
    step = 360 / args.segments
    if not 0 <= args.gap < step:
        raise ValueError("Gap must be nonnegative and smaller than one segment's angle")
    if len(args.colors) not in (1, args.segments):
        raise ValueError("Provide one color or exactly one color per segment")
    padding = args.outer * 0.05
    center = args.outer + padding
    root = document(2 * center, 2 * center, "Segmented schematic ring",
                    "Equal schematic sectors with a transparent central hole. "
                    "No data proportions or cycle are implied. Add verified labels separately.")
    group = element(root, "g", id="segments", **{"data-segment-count": args.segments})

    def point(radius, angle):
        rad = math.radians(angle)
        return f"{number(center + radius * math.cos(rad))} {number(center + radius * math.sin(rad))}"

    for index in range(args.segments):
        start = args.start + index * step + args.gap / 2
        end = args.start + (index + 1) * step - args.gap / 2
        large = int(end - start > 180)
        outer, inner = number(args.outer), number(args.inner)
        path = (f"M {point(args.outer, start)} "
                f"A {outer} {outer} 0 {large} 1 {point(args.outer, end)} "
                f"L {point(args.inner, end)} "
                f"A {inner} {inner} 0 {large} 0 {point(args.inner, start)} Z")
        element(group, "path", id=f"segment-{index + 1}", d=path,
                fill=args.colors[index % len(args.colors)],
                **{"data-start-angle": number(start), "data-end-angle": number(end)})
    return root


def make_ribbon(args):
    w, h, tail, fold = args.width, args.height, args.tail, args.fold
    if not (w > 0 and h > 0 and 0 < tail < w / 2 and 0 < fold < min(tail, h / 2)):
        raise ValueError("Require width/height > 0, 0 < tail < width/2, and 0 < fold < min(tail, height/2)")
    pad = h * 0.1
    left, top = tail + pad, pad
    right, bottom = left + w, top + h
    root = document(w + 2 * tail + 2 * pad, h + fold + 2 * pad, "Folded ribbon",
                    "Rear tails, shaded folds, and front band. Add editable text separately "
                    "inside the recorded text-safe-area rectangle.")

    def polygon(parent, identity, points, fill):
        element(parent, "polygon", id=identity, fill=fill,
                points=" ".join(f"{number(x)},{number(y)}" for x, y in points))

    rear = element(root, "g", id="rear-tails")
    polygon(rear, "left-tail", [(left - tail, top + fold), (left + fold, top + fold),
            (left + fold, bottom + fold), (left - tail, bottom + fold),
            (left - tail / 2, top + fold + h / 2)], args.color)
    polygon(rear, "right-tail", [(right - fold, top + fold), (right + tail, top + fold),
            (right + tail / 2, top + fold + h / 2), (right + tail, bottom + fold),
            (right - fold, bottom + fold)], args.color)
    folds = element(root, "g", id="folds")
    polygon(folds, "left-fold", [(left, bottom), (left + fold, bottom),
            (left + fold, bottom + fold)], args.fold_color)
    polygon(folds, "right-fold", [(right, bottom), (right - fold, bottom),
            (right - fold, bottom + fold)], args.fold_color)
    element(root, "rect", id="front-band", x=number(left), y=number(top),
            width=number(w), height=number(h), fill=args.color)
    inset = min(h * 0.2, w * 0.1)
    element(root, "rect", id="text-safe-area", x=number(left + inset), y=number(top + inset),
            width=number(w - 2 * inset), height=number(h - 2 * inset),
            fill="none", stroke="none", **{"aria-hidden": "true"})
    return root


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="kind", required=True)
    ring = commands.add_parser("ring", help="Equal schematic sectors, not a statistical chart")
    ring.add_argument("--segments", type=int, required=True)
    ring.add_argument("--outer", type=finite, required=True)
    ring.add_argument("--inner", type=finite, required=True)
    ring.add_argument("--gap", type=finite, required=True, help="Total gap per boundary, in degrees")
    ring.add_argument("--start", type=finite, default=-90, help="Degrees clockwise from the right")
    ring.add_argument("--colors", nargs="+", type=color, required=True)
    ribbon = commands.add_parser("ribbon", help="Rear tails, folds, and a front band")
    for name in ("width", "height", "tail", "fold"):
        ribbon.add_argument(f"--{name}", type=finite, required=True)
    ribbon.add_argument("--color", type=color, required=True)
    ribbon.add_argument("--fold-color", type=color, required=True)
    for command in (ring, ribbon):
        command.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        root = make_ring(args) if args.kind == "ring" else make_ribbon(args)
    except ValueError as exc:
        parser.error(str(exc))
    ET.indent(root, space="  ")
    # Exclusive creation protects an existing component from an accidental rerun.
    with args.output.open("x", encoding="utf-8", newline="\n") as out:
        out.write(ET.tostring(root, encoding="unicode") + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
