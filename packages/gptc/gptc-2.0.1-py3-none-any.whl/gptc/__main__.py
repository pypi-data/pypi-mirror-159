#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-3.0-or-later

import argparse
import json
import sys
import gptc

def main():
    parser = argparse.ArgumentParser(
        description="General Purpose Text Classifier", prog="gptc"
    )
    subparsers = parser.add_subparsers(dest="subparser_name", required=True)

    compile_parser = subparsers.add_parser("compile", help="compile a raw model")
    compile_parser.add_argument("model", help="raw model to compile")
    compile_parser.add_argument("--max-ngram-length", "-n", help="maximum ngram length", type=int, default=1)

    classify_parser = subparsers.add_parser("classify", help="classify text")
    classify_parser.add_argument("model", help="compiled model to use")
    classify_parser.add_argument("--max-ngram-length", "-n", help="maximum ngram length", type=int, default=1)
    group = classify_parser.add_mutually_exclusive_group()
    group.add_argument(
        "-j",
        "--json",
        help="output confidence dict as JSON (default)",
        action="store_true",
    )
    group.add_argument(
        "-c",
        "--category",
        help="output most likely category or `None`",
        action="store_true",
    )

    args = parser.parse_args()

    with open(args.model, "r") as f:
        model = json.load(f)

    if args.subparser_name == "compile":
        print(json.dumps(gptc.compile(model, args.max_ngram_length)))
    else:
        classifier = gptc.Classifier(model, args.max_ngram_length)

        if sys.stdin.isatty():
            text = input("Text to analyse: ")
        else:
            text = sys.stdin.read()

        if args.category:
            print(classifier.classify(text))
        else:
            print(json.dumps(classifier.confidence(text)))


if __name__ == "__main__":
    main()
