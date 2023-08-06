from __future__ import annotations

import pathlib

import click

from zinc import codegen, openapi_conversion


@click.command()
@click.option("--input-files", type=str, required=True, help="space-delimited list of input files")
@click.option("--output-file", type=str, required=True, help="python output file.")
def main(input_files: str, output_file: str) -> None:
    specs = openapi_conversion.to_class_specs(
        {
            pathlib.Path(path).name: openapi_conversion.load_spec(path)
            for path in input_files.split(" ")
        }
    )
    pathlib.Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w+") as f:
        f.write(codegen.generate_objects(specs))


if __name__ == "__main__":
    main()
